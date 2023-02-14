#!/usr/bin/node
const numArgv = process.argv.lenght;
if (numArgv < 3) { console.log('No argument'); } else if (numArgv === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
