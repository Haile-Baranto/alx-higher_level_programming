#!/usr/bin/node
const oldSquare = require('./5-square');
/**
 * The class square extends from class square of 5-square.js
 * Instane method charPrint(c) prints the square using charachter 'c'
 * If c is undefined, use the character X to print the square.
 */

class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let cWideth = '';
    for (let i = 0; i < this.width; i++) {
      cWideth += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(cWideth);
    }
  }
}
module.exports = Square;
