#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    console.log(body);
  }
}).pipe(fs.createWriteStream(process.argv[3], 'utf8'));
