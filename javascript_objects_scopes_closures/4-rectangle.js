#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w == null || h == null) return null;
    if (w <= 0 || h <= 0) return null;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rotwid = this.width;
    this.width = this.height;
    this.height = rotwid;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
