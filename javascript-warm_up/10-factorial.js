#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorise (num) { let factorial = 1; for (let i = 1; i <= num; i++) { factorial *= i; } return factorial; } console.log(factorise(num));
