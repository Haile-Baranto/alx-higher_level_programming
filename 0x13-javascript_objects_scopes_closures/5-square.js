#!/usr/bin/node
const Rectangle = require('./4-rectangle'); // import Rectangle class
/**
 * The class Squre inhertis from Rectangle class of 4-rectangle.js
 * The constructor takes one arguement called size and rectangle constructor is
 * called using  super()
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
