#!/usr/bin/node
const argsCount = process.argv.length;
const num = [];
switch (argsCount) {
	case 2:
	case 3:
		console.log(0);
		break;
	default:
		for (let i =2, i < argsCount; i++) {
			nums.push(process.argv[i]);
		}
		nums.sort((a, b) => b - a);
		console.log(nums[1]);
		break;
}
