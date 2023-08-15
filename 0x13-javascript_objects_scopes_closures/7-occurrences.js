#!/usr/bin/node

/**
 * The function returns number of occurences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }

  return count;
};
