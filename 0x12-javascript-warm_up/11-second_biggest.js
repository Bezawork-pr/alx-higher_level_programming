#!/usr/bin/node
const argument = process.argv.slice(2);
const mylength = argument.length;
let temp;
if (mylength === 0 || mylength === 1) {
  console.log(0);
} else {
  for (let j = 0; j < argument.length; j++) {
    for (let i = 0; i < argument.length - j - 1; i++) {
      if (argument[i] > argument[i + 1]) {
        temp = argument[i];
        argument[i] = argument[i + 1];
        argument[i + 1] = temp;
      }
    }
  }
  console.log(argument[mylength - 2]);
}
