#!/usr/bin/node

/** The module defines class Rectangle with constructor which
 *  takes the arguements "w and h" to intialize height and width of rectangle
 * If either h or w <= 0 returns empty object
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
