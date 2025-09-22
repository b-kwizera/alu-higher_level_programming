#!/usr/bin/node
// Class Rectangle with constructor initializing width and height
// If w or h is not a positive integer, create an empty object
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
