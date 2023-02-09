#!/usr/bin/node
const fs = require('fs');
const writeTo = process.argv[2];
const readFrom = process.argv[3];
fs.writeFile(writeTo, readFrom, (err) => {
  if (err) { console.log(err); }
});
