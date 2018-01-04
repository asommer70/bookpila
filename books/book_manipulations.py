from django.conf import settings
# from wand.image import Image
import PyPDF2
import os

def get_pdf_cover(book):
    tmp_file_name = settings.MEDIA_ROOT + book.upload.name + '_page1.pdf'
    image_file_name = book.upload.name + '.jpg'

    # Read the PDF and get the first page.
    pdf_file = book.upload.open()
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)

    # Create a new PDF of just the first page.
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    temp_pdf = open(tmp_file_name, 'wb')
    writer.write(temp_pdf)

    # Close out the files.
    temp_pdf.close()
    book.upload.close()

    # Convert the single page PDF to an image.
    os.system("/usr/local/bin/convert -density 300 {} {}".format(tmp_file_name, settings.MEDIA_ROOT + image_file_name))

    # Remove the one page PDF.
    os.remove(tmp_file_name)

    return settings.MEDIA_URL + image_file_name
