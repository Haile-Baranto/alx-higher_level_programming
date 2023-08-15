#!/usr/bin/node
/**
 * Write a script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 *
 * Your script must import dict from the file 101-data.js
 * In the new dictionary:
 *    A key is a number of occurrences
 *    A value is the list of user ids
 * Print the new dictionary at the end
 */
const data = require('./101-data');
const initialDict = data.dict;

const reversedDict = {};
for (const userId in initialDict) {
  const occurrences = initialDict[userId];
  if (!reversedDict[occurrences]) {
    reversedDict[occurrences] = [];
  }
  reversedDict[occurrences].push(userId);
}

console.log(reversedDict);
