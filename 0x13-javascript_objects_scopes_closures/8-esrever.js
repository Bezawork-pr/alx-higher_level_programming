#!/usr/bin/node
exports.esrever = function (list) {
  const myreverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myreverse.push(list[i]);
  }
  return myreverse;
};
