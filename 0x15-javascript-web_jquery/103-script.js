const $ = window.$;
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    getLang();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      getLang();
    }
  });
});
function getLang () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $.get(
    url + $.param({ lang: $('INPUT#language_code').val() }),
    function (data) {
      $('DIV#hello').html(data.hello);
    }
  );
}
