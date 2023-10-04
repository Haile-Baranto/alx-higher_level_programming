// Fetch and display the French translation of "hello" in DIV#hello
$(document).ready(function () {
  // Fetch the translation of "hello" and display it in DIV#hello
  $.get('https://fourtonfish.com/hellosalut/?lang=fr')
    .done(function (data) {
      $('DIV#hello').text(data.hello);
    })
    .fail(function () {
      $('DIV#hello').text('Error fetching translation.');
    });
});
