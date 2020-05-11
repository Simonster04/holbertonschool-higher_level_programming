#!/usr/bin/node

const list = require('./100-data').list;
const mapList = list.map((x, idx) => x * idx);
console.log(list + '\n' + mapList);
