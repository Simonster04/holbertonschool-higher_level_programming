#!/usr/bin/node

if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2]) {
  console.log(process.argv[2] + ' is undefinded');
} else if (process.argv[3]) {
  console.log('undefinded is ' + process.argv[2]);
} else {
  console.log('undefinded is undefinded');
}
