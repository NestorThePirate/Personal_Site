$(document).ready(function () {
    $('.answer').on('click', function (e) {
        e.preventDefault();
        var form = $('#comment_box').clone(true);
        if ($(this).parent().find('.comment_form').is(':hidden')) {
            form.find('.parent').val($(this).parent().data('pk'));
            $(this).parent().find('.comment_form').append(form).fadeIn('slow');
            $(this).text('Отменить');
        }
        else {
            $(this).parent().find('.comment_form').fadeOut('slow');
            $(this).parent().find('#comment_box').remove();
            $(this).text('Ответить');
        }
    });

    $('.answer-button').on('click', function (e) {
        e.preventDefault();
        var form = $(this).parent();
        var url = '/article/' + $('.article').data('pk');
        $.ajax({
            type: 'POST',
            url: url,
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                alert(response.error);
            },
            error: function (xhr, errmsg, err) {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});
