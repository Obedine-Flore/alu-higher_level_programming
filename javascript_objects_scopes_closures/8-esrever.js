#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const output = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    output.push(list[i]);
  }
  return output;
};
