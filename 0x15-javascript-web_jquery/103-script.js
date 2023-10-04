$(document).ready(() => {
  const translate = () => {
    const languageCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, data => {
      $('DIV#hello').text(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(event => {
    if (event.keyCode === 13) translate();
  });
});
