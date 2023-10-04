// Add a new <li> element with the text "Item" to the UL.my_list when clicking on DIV#add_item
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li>Item</li>');

    $('ul.my_list').append(newItem);
  });
});
