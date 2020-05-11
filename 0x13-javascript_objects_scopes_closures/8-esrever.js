#!/usr/bin/node

module.exports.esrever = function (list) {
  const last = list.length;
  const aux = [];
  for (let i = (last - 1); i >= 0; i--) {
    aux.push(list[i]);
  }
  return aux;
};
