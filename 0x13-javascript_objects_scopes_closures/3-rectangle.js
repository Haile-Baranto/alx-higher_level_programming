#!/usr/bin/node

/** The module defines class Rectangle with constructor which
 *  takes the arguements "w and h" to intialize height and width of rectangle
 *  The class also defines an instance method called print() that prints the
 *      rectangle using 'X'
 * If either h or w <= 0 returns empty object
 *
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xWideth = '';
    for (let i = 0; i < this.width; i++) {
      xWideth += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(xWideth);
    }
  }
}
module.exports = Rectangle;
