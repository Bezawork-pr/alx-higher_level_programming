#!/usr/bin/node
const numbers = process.argv;
const firstNumber = numbers[2];
const secondNumber = numbers[3];
function myFunction (firstNumber, secondNumber) {
  if (!firstNumber || !secondNumber) {
    console.log('NaN');
  } else {
    console.log(+firstNumber + +secondNumber);
  }
}
myFunction(firstNumber, secondNumber);
