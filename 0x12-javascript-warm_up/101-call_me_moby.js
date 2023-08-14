#!/usr/bin/node
/**
 * Write a function that executes x times a function.
 * The function must be visible from outside
 * Prototype: function (x, theFunction)
 * You are not allowed to use var
 */
// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}
// Export the function
module.exports.callMeMoby = callMeMoby;
