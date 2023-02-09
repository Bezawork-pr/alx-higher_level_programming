#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const writeTo = process.argv[3];
const readFrom = process.argv[2];
request(readFrom, (err, body) => {
  if (err) throw err;
  fs.writeFile(writeTo, body.body, (err) => {
    if (err) { console.log(err); }
  });
});
