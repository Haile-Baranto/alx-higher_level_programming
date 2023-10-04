// Fetch and display translations of "Hello" based on the user-entered language code
$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code from INPUT#language_code
    const languageCode = $('INPUT#language_code').val();

    // Make an AJAX GET request to fetch the translation
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      // Display the translation of "Hello" in DIV#hello
      $('#hello').text(data.hello);
    });
  });
});
