#!/usr/bin/node
/** Write a script that prints x times “C is fun” where x is first arguement
 * If the first arguement is not convertable to int print “Missing number of occurrences”
 * Must use loops, console.log max of twice
 * Not allowed to use var
 */
const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
