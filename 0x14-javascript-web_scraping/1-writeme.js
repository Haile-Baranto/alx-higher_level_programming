#!/usr/bin/node
/**
 * Write string to  file
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */

const fs = require('fs');

// Check if both arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writeToFile.js <file_path> <string_to_write>');
  process.exit(1); // Exit with an error code
}

// Extract command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  }
});
