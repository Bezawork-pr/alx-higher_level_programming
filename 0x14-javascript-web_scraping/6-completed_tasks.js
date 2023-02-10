#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
const dict = {};
let id = 1;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].userId === id && todos[i].completed === true) {
        count++;
        if (i === todos.length - 1) { dict[id] = count; }
      } else if (todos[i].userId === id && todos[i].completed === false) {
        if (i === todos.length - 1) { dict[id] = count; }
        continue;
      } else if (todos[i].userId !== id || i === todos.length - 1) {
        dict[id] = count;
        count = 0;
        i--;
        id++;
      }
    }
  }
  console.log(dict);
});
