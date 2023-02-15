#!/usr/bin/node
exports.esrever = function (list) {
	const myList = [];
	for (let i = list.lenght - 1; i >= 0; i--) {
		myList.push(list[i]);
	}
	return myList;
};
