#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const arg = process.argv[2];
const starwarUrl = url + arg + '/';
request(starwarUrl, (err, res, body) => {
  console.log(err || JSON.parse(body).title);
});
