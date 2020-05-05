#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  process.argv.forEach((val, index) => {
    if (index === 2) {
      console.log(`${val}`);
    }
  });
}
