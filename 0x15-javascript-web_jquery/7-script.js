// Fetch and display a Star Wars character's name from an API in DIV#character
$(document).ready(function () {
  // Make an AJAX GET request and handle the response
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .done(function (data) {
      $('DIV#character').text(data.name);
    })
    .fail(function () {
      $('#character').text('Error fetching character data.');
    });
});
