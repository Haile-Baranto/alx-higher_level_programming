$(document).ready(function () {
  // Add a click event handler to DIV#red_header
  $('DIV#red_header').click(function () {
    // Add the "red" class to the <header> element
    $('header').addClass('red');
  });
});
