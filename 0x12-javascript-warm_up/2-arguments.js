#!/usr/bin/node
const argument = process.argv;
if (argument[2] && !argument[3]) {
  console.log('Argument found');
} else if (!argument[2]) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
