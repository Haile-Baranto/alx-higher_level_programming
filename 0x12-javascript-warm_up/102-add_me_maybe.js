#!/usr/bin/node
/**
 * Write a function that increments and calls a function.
 * The function must be visible from outside
 * Prototype: function (number, theFunction)
 * You are not allowed to use var} number
 */
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

// Export the function
module.exports.addMeMaybe = addMeMaybe;
