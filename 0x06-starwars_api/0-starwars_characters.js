#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    displayCharacters(characters, 0);
  }
});

function displayCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        displayCharacters(characters, index + 1);
      }
    }
  });
}
