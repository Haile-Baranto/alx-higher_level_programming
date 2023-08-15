#!/usr/bin/node
const fs = require('fs');

// Get the file paths from command-line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Check if files exist, are valid, and if a destination is provided
if (
  fs.existsSync(fileA) &&
  fs.statSync(fileA).isFile() &&
  fs.existsSync(fileB) &&
  fs.statSync(fileB).isFile() &&
  fileC !== undefined
) {
  // Read the contents of the source files
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);

  // Write the concatenated content to the destination file
  fs.writeFileSync(fileC, fileAContent + fileBContent);

  // Print a success message
  console.log(`Concatenated data has been written to ${fileC}`);
} else {
  // Display a usage error message
  console.error('Usage: ./concat.js <file1> <file2> <destination>');
}
