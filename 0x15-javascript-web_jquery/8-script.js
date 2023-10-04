// Fetch and list Star Wars movie titles from an API in UL#list_movies
$(document).ready(function () {
  // Make an AJAX GET request and handle the response
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json')
    .done(function (data) {
      $.each(data.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    })
    .fail(function () {
      $('#list_movies').append('<li>Error fetching movie data.</li>');
    });
});
