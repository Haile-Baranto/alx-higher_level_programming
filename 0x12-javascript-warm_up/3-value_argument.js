#!/usr/bin/node
/** prints the first arguemet passed from command line
 * Not allowed to use var and length
 */
const args = process.argv.slice(2);
let count = 0;
for (count of args) {
  count++;
}
if (count === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
