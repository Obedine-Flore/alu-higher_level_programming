#!/usr/bin/node
const Tectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
};

