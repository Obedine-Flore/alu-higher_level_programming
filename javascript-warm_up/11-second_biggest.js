#!/usr/bin/node
const argCount = process.argv.length;
const num = [];
switch (argCount) {
	case 2:
	case 3:
		console.log(0);
		break;
	default:
		for (let i =2, i < argCount; i++) {
			numbers.push(process.argv[i]);
		}
		numbers.sort((a, b) => b - a);
		console.log(numbers[1]);
		break;
}
