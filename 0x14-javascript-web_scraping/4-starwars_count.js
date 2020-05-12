#!/usr/bin/node

const WedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    let cont = 0;
    for (let i = 0; i < JSON.parse(body).results.length; i++) {
      for (let j = 0; j < JSON.parse(body).results[i].characters.length; j++) {
        if (JSON.parse(body).results[i].characters[j] === WedgeAntilles) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
