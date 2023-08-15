#!/usr/bin/node

let counter = 0;
/**
 *
 * LoMe function prints the number of arguments already printed and
 * the new argument value. (see example below)
 *
 * Prototype: exports.logMe = function (item)
 * Output format: <number arguments already printed>: <current argument value>} item
 */
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
