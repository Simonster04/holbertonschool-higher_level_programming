#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  list.forEach(element => {
    if (searchElement === element) {
      cont += 1;
    }
  });
  return cont;
};
