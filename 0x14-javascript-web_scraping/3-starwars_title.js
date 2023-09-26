#!/usr/bin/node

const request = require('request');

// Check if a movie ID argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send an HTTP GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
