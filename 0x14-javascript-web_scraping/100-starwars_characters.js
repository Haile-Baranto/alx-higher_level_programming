#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, { json: true }, (error, response, movieData) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to retrieve movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  const characters = movieData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  // Function to retrieve and print character names
  function printCharacterName (characterUrl) {
    request(characterUrl, { json: true }, (characterError, characterResponse, characterData) => {
      if (!characterError && characterResponse.statusCode === 200) {
        console.log(characterData.name);
      } else {
        console.error(`Error retrieving character data: ${characterError}`);
      }
    });
  }

  // Iterate through character URLs and print character names
  characters.forEach(printCharacterName);
});
