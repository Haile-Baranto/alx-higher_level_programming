#!/usr/bin/node
/** Write a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
const args = process.argv.slice(2); // remove first two elements
function add (a, b) {
  return a + b;
}
const sum = add(parseInt(args[0]), parseInt(args[1]));
console.log(sum);
