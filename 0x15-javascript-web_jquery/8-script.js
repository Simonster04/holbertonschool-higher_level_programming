$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      for (const i of data.results) {
        $('#list_movies').append('<li>' + i.title);
      }
    }
  });
});
