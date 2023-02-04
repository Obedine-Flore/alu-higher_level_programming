#!/usr/bin/node
function factorise (num) {
	if (isNan(num) || num < 0) {
		return 1;
	} else if (num === 0) {
		return 1;
	} else {
		return num * factorial(num - 1);
	}
}
const arg = parseInt(process.argv[2]);
console.log(factorise(arg));
