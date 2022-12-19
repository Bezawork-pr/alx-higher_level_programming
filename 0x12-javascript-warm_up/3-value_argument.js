#!/usr/bin/node
const argument = process.argv;
if (argument[2]) {
  console.log(argument[2]);
} else if (!argument[2]) {
  console.log('No argument');
}
