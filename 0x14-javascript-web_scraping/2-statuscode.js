#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const requestSettings = {
  method: 'HEAD',
  url: url
};
request(requestSettings, function (err, response) {
  console.log(err || response.statusCode);
});
