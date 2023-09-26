#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  // Iterate through the tasks and count completed tasks by user
  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  // Print the completed tasks count for each user
  console.log(JSON.stringify(completedTasksByUser, null, 2));
});
