#!/usr/bin/node
/** Write a script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * You must do it recursively and (use function and console.log())
 * Factorial of NaN is 1 and you are not allowed to use var
 */
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Base case: Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Base case: Factorial of 0 and 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive case: n! = n * (n-1)!
  }
}

const input = parseInt(process.argv[2]); // Parse the input argument as an integer
const result = factorial(input);

console.log(result);
