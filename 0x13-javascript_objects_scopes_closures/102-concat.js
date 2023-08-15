#!/usr/bin/node

/**
 * Write a script that concats 2 files.
 *      The first argument is the file path of the first source file
        The second argument is the file path of the second source file
        The third argument is the file path of the destination
 */
const fs = require('fs');

const args = process.argv.slice(2);
if (args.length !== 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const [file1, file2, destination] = args;

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}: ${err.message}`);
      process.exit(1);
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destination, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destination}: ${err.message}`);
        process.exit(1);
      }
      console.log(`Concatenated data has been written to ${destination}`);
    });
  });
});
