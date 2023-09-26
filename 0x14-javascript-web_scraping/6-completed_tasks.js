#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const completedTask = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTask[todo.userId]) {
        completedTask[todo.userId] = 1;
      } else {
        completedTask[todo.userId]++;
      }
    }
  });

  console.log(completedTask);
});