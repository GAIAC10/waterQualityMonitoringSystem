(function(a, e, c, d) {
    var b = a("#contact-form");
    b.submit(function(f) {
        a(".form-group").removeClass("has-error");
        a(".help-block").remove();
        var g = {
            name: a('input[name="form-name"]').val(),
            email: a('input[name="form-email"]').val(),
            subject: a('input[name="form-subject"]').val(),
            message: a('textarea[name="form-message"]').val()
        };
        a.ajax({
            type: "POST",
            url: "contact-form.php",
            data: g,
            dataType: "json",
            encode: true
        }).done(function(h) {
            if (!h.success) {
                if (h.errors.name) {
                    a("#name-field").addClass("has-error");
                    a("#name-field").find(".col-lg-10").append('<span class="help-block">' + h.errors.name + "</span>")
                }
                if (h.errors.email) {
                    a("#email-field").addClass("has-error");
                    a("#email-field").find(".col-lg-10").append('<span class="help-block">' + h.errors.email + "</span>")
                }
                if (h.errors.subject) {
                    a("#subject-field").addClass("has-error");
                    a("#subject-field").find(".col-lg-10").append('<span class="help-block">' + h.errors.subject + "</span>")
                }
                if (h.errors.message) {
                    a("#message-field").addClass("has-error");
                    a("#message-field").find(".col-lg-10").append('<span class="help-block">' + h.errors.message + "</span>")
                }
            } else {
                b.html('<div class="alert alert-success">' + h.message + "</div>")
            }
        }).fail(function(h) {
            console.log(h)
        });
        f.preventDefault()
    })
}(jQuery, window, document));