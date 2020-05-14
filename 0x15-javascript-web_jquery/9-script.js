$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('#hello').append('<li>' + data.hello);
    }
  });
});
