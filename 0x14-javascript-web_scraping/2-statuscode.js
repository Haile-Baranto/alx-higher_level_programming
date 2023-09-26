#!/usr/bin/node
/**
 * The script displays the status code of GET method using request module.
 * The first argument is the URL to request (GET)
 * Format "code: <status code>"
 */

const request = require('request');

// Check if a URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node getStatus.js <URL>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2];
request.get(url, (error, Response) => {
  if (error) {
    console.error(error);
  }

  // Access the response status code
  const statusCode = Response.statusCode;
  console.log(`code: ${statusCode}`);
});
