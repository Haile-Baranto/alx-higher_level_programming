// Change the text color of the <header> element to red when the user clicks on DIV#red_header
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
