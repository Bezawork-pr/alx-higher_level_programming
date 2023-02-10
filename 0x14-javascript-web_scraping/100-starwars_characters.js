#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
const request = require('request');
request(url, (err, body) => {
  if (err) throw err;
  const getBody = JSON.parse(body.body).characters;
  getBody.forEach(element => {
    request(element, (err, body) => {
      if (err) throw err;
      console.log(JSON.parse(body.body).name);
    });
  });
});
