#!/usr/bin/node
const printnum = process.argv[2];
if (!printnum) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < printnum; i++) {
  console.log('C is fun');
}
