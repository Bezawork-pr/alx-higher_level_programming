#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
const request = require('request');
function getCharacter (url) {
  return new Promise(function (resolve, reject) {
    request(url, (err, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}
async function asyncCall (url) {
  const result2 = await getCharacter(url);
  const obj = JSON.parse(result2.body).name;
  console.log(obj);
}
request(url, (err, body) => {
  if (err) throw err;
  const getBody = JSON.parse(body.body).characters;
  for (let i = 0; i < getBody.length; i++) {
    (async function () {
      await asyncCall(getBody[i]);
    })();
  }
});
