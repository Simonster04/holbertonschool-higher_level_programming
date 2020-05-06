#!/usr/bin/node

if (!process.argv[3]) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map((num) => parseInt(num));
  list.sort(function (a, b) {
    return a - b;
  });
  console.log(list.reverse()[1]);
}
