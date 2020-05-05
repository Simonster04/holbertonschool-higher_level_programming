#!/usr/bin/node

let fact = 1;
if (!process.argv[2]) {
  console.log(fact);
} else {
  for (let x = 1; x <= parseInt(process.argv[2]); x++) {
    fact *= x;
  }
  console.log(fact);
}
