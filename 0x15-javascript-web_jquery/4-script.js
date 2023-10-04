// Toggle the class of the <header> element between "red" and "green" when clicking on DIV#toggle_header
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
