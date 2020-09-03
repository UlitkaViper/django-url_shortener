$(document).ready(function () {
    $('#textarea').on('input', function (e) {
        this.style.height = '0px';
        this.style.height = (this.scrollHeight + 6) + 'px';
    });
    var csrf_token = $("input[name=csrfmiddlewaretoken]")
    $("body").on("click", ".Delete", function () {
        var delete_button = $(this)
        $.ajax({
            url: '/delete/' + $(this).closest('div').attr('id'),
            type: 'POST',
            data: {
                id: $(this).closest('div').attr('id'),
                csrfmiddlewaretoken: csrf_token.val(),
                func: $(this).text()
            },
            success: function (response) {
                delete_button.parents('div').remove()
            }
        });

    });
    $(".url-field").on("click", ".my_button", function () {
        if (!isNullOrWhitespace($(".url_to_short").val())) {
            $.ajax({
                url: '/',
                type: 'POST',

                data: {
                    full_url: $(".url_to_short").val(),
                    csrfmiddlewaretoken: csrf_token.val(),
                },
                success: function (response) {
                    if (!response.error) {
                        $(".result-url").html("<p>Your short link:</p>\
                        <h4>"+ response.shorten_url + "</h4>")
                    }
                    else {
                        $(".result-url").html("<p>" + response.error + "</p>")
                    }


                }
            });
        }

    });

    function isNullOrWhitespace(input) {
        return !input || !input.trim();
    }
});