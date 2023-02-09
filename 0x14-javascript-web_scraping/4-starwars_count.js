#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).films;
    for (let i = 0; i < films.length; i++) {
      count++;
    }
    console.log(count);
  }
});
