$(document).ready(function () {
    var article_list = $('#article-list');

    article_list.on('mouseenter', '.articles', function () {
        $(this).find('.panel-heading').css('color', '#1AB2FF');
    });
    article_list.on('mouseleave', '.articles', function () {
        $(this).css('color', 'black');
        $(this).find('.panel-heading').css('color', 'black');
    });
    article_list.on('click', '.articles', function () {
        var link = 'http://127.0.0.1:8000/article/' + $(this).data('pk');
        $(location).attr('href', link);
    });
});
