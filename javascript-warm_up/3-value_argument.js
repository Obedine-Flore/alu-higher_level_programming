#!/usr/bin/node
const firstArgv = process.argv[2];
if (firstArgv == null) {
	console.log('No comment');
} else {
	console.log(firstArgv);
}
