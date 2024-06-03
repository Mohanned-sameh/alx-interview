#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(url, (error, response, body) => {
  for (const film of JSON.parse(body).results) {
    if (film.episode_id === parseInt(id)) {
      for (const character of film.characters) {
        request(character, (error, response, body) => {
          console.log(JSON.parse(body).name);
        });
      }
    }
  }
});
