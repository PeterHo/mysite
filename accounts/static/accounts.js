/**
 * Created by peter on 14/01/16.
 */

var initialize = function (navigator, user, token, urls) {
    $("#id_login").click(function () {
        navigator.id.request();
    });
    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            $.post(
                urls.login,
                {assertion: assertion, csrfmiddlewaretoken: token}
            ).done(function () {
                window.location.reload();
            }).fail(function () {
                navigator.id.logout();
            });
        },
        onlogout: function () {

        }
    });
};

window.PeterSite = {
    Accounts: {
        initialize: initialize
    }
};
