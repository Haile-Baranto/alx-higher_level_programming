#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./webpage_to_file.js <url> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  fs.writeFileSync(filePath, body, 'utf-8');
});
