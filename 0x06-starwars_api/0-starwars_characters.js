#!/usr/bin/node
const request = require('request');
const end = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${end}`;
request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const res = JSON.parse(body);
  const stars = res.characters;
  for (let i = 0; i < stars.length; i++) {
    request(stars[i], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
