let argv = require('minimist')(process.argv.slice(2));
let pretty = require('pretty');
let fs = require('fs');

let htmlFilePath = argv.html;

fs.readFile(htmlFilePath, function (err, data) {
    if (err) return console.error(err);
    let htmlPrettyString = pretty(data.toString(), {ocd: false});
    fs.writeFile(htmlFilePath, htmlPrettyString, function (err) {
        if (err) return console.log(err);
    });
});
