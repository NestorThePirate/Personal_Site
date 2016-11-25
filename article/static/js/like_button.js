$(document).ready(function () {
  $('.like').on('click', function (e) {
      e.preventDefault();
      var url = '/rate/' + $(this).closest('.panel-heading').data('id') + '/' + $(this).data('grade');
      var likes = $(this).closest('.panel-heading').find('.total-likes');
      var dislikes = $(this).closest('.panel-heading').find('.total-dislikes');
      $(this).closest('.panel-heading').find('.like').css({'color': 'white'});
      $(this).css({'color': '#1AB2FF'});
      $.ajax({type: 'GET',
              url: url,
              dataType: 'json',
              success: function(response){
                  likes.html(response.likes);
                  dislikes.html(response.dislikes);
              }
      });
  })
});
