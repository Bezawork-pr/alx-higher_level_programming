#!/usr/bin/node
link = process.argv[2];
async function getStatus() {
  const response = await fetch(link);
  console.log(response.status);
}
getStatus();

