#!/usr/bin/node
/** Write a code that prints a square to the console
 * The first arguement is the size of the square and if the first
 * arguemet is not convertable to a number print 'Missing size'
 * You must use 'X', loops and console.log to print the square shape
 */
const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  let output = '';
  for (let j = 0; j < firstArg; j++) {
    output += 'X';
  }
  for (let i = 0; i < firstArg; i++) {
    console.log(output);
  }
}
