#!/usr/bin/node
/** Write script that concatinate two arguements passed to it
 * in the form "1st arg + is + 2nd arg".
 * Not allowed to use var
 */
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
