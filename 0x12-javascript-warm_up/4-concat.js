#!/usr/bin/node
const argument = process.argv;
if (argument[2] && argument[3]) {
  console.log(argument[2] + ' is ' + argument[3]);
} else if (!argument[2] && argument[3]) {
  console.log('undefined is ' + argument[3]);
} else if (argument[2] && !argument[3]) {
  console.log(argument[2] + ' is undefined');
} else if (!argument[2] && !argument[3]) {
  console.log('undefined is undefined');
}
