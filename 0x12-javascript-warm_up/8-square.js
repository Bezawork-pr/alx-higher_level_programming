#!/usr/bin/node
const printnum = process.argv[2];
let text = '';
if (!printnum || isNaN(printnum)) {
  console.log('Missing size');
}
for (let i = 0; i < printnum; i++) {
  text += 'X';
}
for (let j = 0; j < printnum; j++) {
  console.log(text);
}
