const fs = require('fs');
const assets =  '../assets/js/vendor/';

if (!fs.existsSync(assets)){
    fs.mkdirSync(assets);
}

fs.createReadStream('./node_modules/foundation-sites/dist/js/foundation.min.js')
  .pipe(fs.createWriteStream(assets + 'foundation.min.js'));
fs.createReadStream('./node_modules/jquery/dist/jquery.min.js')
  .pipe(fs.createWriteStream(assets + 'jquery.min.js'));
