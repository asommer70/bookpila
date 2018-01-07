const fs = require('fs');
const https = require('https');

const assets =  '../assets/js/vendor/';

if (!fs.existsSync(assets)){
    fs.mkdirSync(assets);
}

fs.createReadStream('./node_modules/foundation-sites/dist/js/foundation.min.js')
  .pipe(fs.createWriteStream(assets + 'foundation.min.js'));
fs.createReadStream('./node_modules/jquery/dist/jquery.min.js')
  .pipe(fs.createWriteStream(assets + 'jquery.min.js'));

const epubMinUrl = 'https://raw.githubusercontent.com/futurepress/epub.js/master/build/epub.min.js';
const epubMinFile = fs.createWriteStream(assets + 'epub.min.js');
const epubMinReq = https.get(epubMinUrl, function(response) {
  response.pipe(epubMinFile);
});

const epubUrl = 'https://raw.githubusercontent.com/futurepress/epub.js/master/build/epub.js';
const epubFile = fs.createWriteStream(assets + 'epub.js');
const epubReq = https.get(epubUrl, function(response) {
  response.pipe(epubFile);
});

const zipUrl = 'https://raw.githubusercontent.com/futurepress/epub.js/master/build/libs/zip.min.js';
const zipFile = fs.createWriteStream(assets + 'zip.min.js');
const zipReq = https.get(zipUrl, function(response) {
  response.pipe(zipFile);
});
