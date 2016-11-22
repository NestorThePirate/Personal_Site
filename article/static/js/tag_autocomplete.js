$(document).ready(function(){
    $('.insert-tag').autocomplete({
        source: 'tag/tag_autocomplete',
        minLength: 2
    })
});
