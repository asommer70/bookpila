from django.conf import settings
# import ebooklib
# from ebooklib import epub
import zipfile
from lxml import etree
import PyPDF2
import os

def get_pdf_cover(book):
    """Creates an image from the first page of a PDF file in media/ and returns the media url for the file."""
    tmp_file_path = settings.MEDIA_ROOT + book.upload.name + '_page1.pdf'
    image_file_name = book.upload.name + '.jpg'

    # Read the PDF and get the first page.
    pdf_file = book.upload.open()
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)

    # Create a new PDF of just the first page.
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    temp_pdf = open(tmp_file_path, 'wb')
    writer.write(temp_pdf)

    # Close out the files.
    temp_pdf.close()
    book.upload.close()

    # Convert the single page PDF to an image.
    os.system("/usr/local/bin/convert -density 300 {} {}".format(tmp_file_path, settings.MEDIA_ROOT + image_file_name))

    # Remove the one page PDF.
    os.remove(tmp_file_path)

    return settings.MEDIA_URL + image_file_name


def get_epub_cover(book):
    """Saves the cover image from an ePub file to media/ and returns the media url for the file."""
    file_path = settings.MEDIA_ROOT + book.upload.name
    cover_meta = None
    image_href = None

    # Setup the XML namespace.
    ns = {
        'n':'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg':'http://www.idpf.org/2007/opf',
        'dc':'http://purl.org/dc/elements/1.1/'
    }

    # Read the container.xml file from the zip archive.
    zip = zipfile.ZipFile(file_path)
    txt = zip.read('META-INF/container.xml')
    tree = etree.fromstring(txt)

    # Get the path to the meta file and the root directory for the files.
    cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path', namespaces=ns)[0]
    base_path = cfname.split('/')[0]

    # Grab the metadata block from the contents metafile.
    cf = zip.read(cfname)

    # Find the name of the cover item in the metadata.
    tree = etree.fromstring(cf)
    for meta in tree.xpath('/pkg:package/pkg:metadata', namespaces=ns)[0]:
        if 'name' in meta.attrib:
            if meta.attrib['name'] == 'cover':
                cover_meta = meta.attrib['content']

    # Find the path to the cover image.
    for item in tree.xpath('/pkg:package/pkg:manifest', namespaces=ns)[0]:
        if 'id' in item.attrib:
            if item.attrib['id'] == cover_meta:
                image_href = item.attrib['href']

    # Extract the cover image from the zip file.
    img = zip.read(base_path + '/' + image_href)
    img_file = open(file_path + '.jpg','wb')
    img_file.write(img)
    img_file.close()

    return settings.MEDIA_URL + book.upload.name + '.jpg'
