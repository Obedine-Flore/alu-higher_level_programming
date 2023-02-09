#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
	if (!error) {
		const results = JSON.parse(body).results;
		console.log(results.reduce((coint, movie) => {
			return movie.characters.find((character) => character.endWidth('/18/'))
			? count + 1
			: count;
		}, 0));
	}
});
