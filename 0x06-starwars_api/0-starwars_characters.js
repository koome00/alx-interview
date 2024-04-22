#!/usr/bin/node
const request = require('request');
const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.alx-tools.com/';
request(filmURL + filmNum, async (err, res, body) => {
  if (err) return console.error(err);
  const charURLList = JSON.parse(body).characters;
  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
