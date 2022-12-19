#!/usr/bin/node
const number = process.argv[2];
function myFunction (number) {
  if (!number) {
    return 1;
  } else if (number < 0) {
    return -1;
  } else if (number === 0) {
    return 1;
  } else {
    return (number * myFunction(number - 1));
  }
}
console.log(myFunction(number));
