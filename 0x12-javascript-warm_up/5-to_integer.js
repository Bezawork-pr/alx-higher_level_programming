#!/usr/bin/node
const argument = Math.floor(process.argv[2]);
console.log(isNaN(argument) ? 'Not a number' : `My number: ${argument}`);
