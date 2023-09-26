#!/usr/bin/node

/**
 * Star Wars Movie Title Retriever
 *
 * This script retrieves the title of a Star Wars movie based on the provided movie ID
 * using the Star Wars API.
 *
 * Usage: ./3-starwars_title.js <movie_id>
 *
 *   - <movie_id>: The ID of the Star Wars movie you want to retrieve the title for.
 *
 * Example:
 *   To retrieve the title of Star Wars Episode IV (A New Hope):
 *   ./3-starwars_title.js 1
 */

const request = require('request');

// Check if a movie ID argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1); // Exit with an error code
}

// Extract the movie ID from the command-line argument
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send an HTTP GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1); // Exit with an error code
  }

  // Check if the API returned a successful response (status code 200)
  if (response.statusCode === 200) {
    // Parse the JSON response body to extract movie data
    const movieData = JSON.parse(body);

    // Print the movie title
    console.log(`Title: ${movieData.title}`);
  } else {
    console.error(`Error: Unable to retrieve movie data. Status code: ${response.statusCode}`);
    process.exit(1); // Exit with an error code
  }
});
