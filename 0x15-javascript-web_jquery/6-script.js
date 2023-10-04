// Update the text of the <header> element to "New Header!!!" when clicking on DIV#update_header
$(document).ready(function () {
  // Add a click event handler to DIV#update_header
  $('DIV#update_header').click(function () {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
