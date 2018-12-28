$("#order").on('click', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: window.location.href + 'order/',

        success: (result) => {
            $("#users").prepend(result);
            $("#noone").addClass('is-hidden');
        },

        error: (result) => {
            alert('Произошла ошибка');
        }
    });
});