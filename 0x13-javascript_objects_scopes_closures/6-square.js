#!/usr/bin/node
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    let myprint = '';
    let myChar;
    if (c) {
      myChar = c;
    } else {
      myChar = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      myprint += myChar;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(myprint);
    }
  }
};
