#!/usr/bin/node
// Class Square that inherits from Square of 5-square.js
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint(c) {
    const char = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
