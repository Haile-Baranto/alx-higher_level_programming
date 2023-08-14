#!/usr/bin/node
/** Write a program that prints "My number: <first argument converted in integer>"
 * if first arguements is convertable to int else print "Not a number"
 * Not allowed to use try/catch and var
 */
const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArg);
}
