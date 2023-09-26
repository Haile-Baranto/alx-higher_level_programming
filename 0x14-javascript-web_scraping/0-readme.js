#!/usr/bin/node
// The module reads the content of a file if file exists otherwise print the error

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: ./read-file.js <file-path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) return console.error(error);
  console.log(data);
});
