#!/usr/bin/node
const numArgv = process.argv.length;
if (numArgv < 3) {
	console.log('No argument');
} else if (numArgv === 3) {
	console.log('Argument found')
} esle {
	console.log('Arguments found');
}
