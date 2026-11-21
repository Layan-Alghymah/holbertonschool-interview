#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${movieId}/`, { json: true }, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    return;
  }

  const characters = body.characters;

  function printCharacter (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], { json: true }, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        console.log(body.name);
      }
      printCharacter(index + 1);
    });
  }

  printCharacter(0);
});
