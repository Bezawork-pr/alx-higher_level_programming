const $ = window.$;
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
      }
    }
  });
});
