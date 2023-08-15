#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // import Rectangle class
/**
 * The class Squre inhertis from Rectangle class of 4-rectangle.js
 * The constructor takes one arguement called size and rectangle constructor is
 * called using  super()
 */

class Squre extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Squre;
