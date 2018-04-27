# Tidy HTML Pelican Plugin

A pelican plugin that makes the final output HTML more tidy using the [Node.js](https://nodejs.org) library [`pretty`](https://github.com/jonschlinkert/pretty).

## Installation

You will need to have [Node.js](https://nodejs.org) installed along with the [`pretty`](https://github.com/jonschlinkert/pretty) and [`minimist`](https://github.com/substack/minimist) libraries.

## Instructions

Add `pelican-plugin-tidy-html` to your plugins list in `pelicanconf.py` after installing.

## Credits

*   [`yuicompressor` Pelican plugin](https://github.com/getpelican/pelican-plugins/tree/master/yuicompressor): Used as a reference on how to obtain the output filepaths for the HTML files to use for post-processing.

*   [How to read and write a file in Node.js](http://en.proft.me/2016/03/20/how-read-and-write-file-nodejs/): Used when figuring out the proper way to read and write files using [Node.js](https://nodejs.org).

## License

This plugin is released under the [GNU AFFERO GENERAL PUBLIC LICENSE](./LICENSE).

