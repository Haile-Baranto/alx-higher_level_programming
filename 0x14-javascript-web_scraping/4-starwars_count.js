#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? acc + 1 : acc, 0);
    console.log(count);
  }
});
