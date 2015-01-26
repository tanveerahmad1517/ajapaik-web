(function () {
    'use strict';
    /*global $ */
    /*global docCookies */
    $(document).ready(function () {
        if (!docCookies.hasItem('ajapaik_agreed_to_cookies')) {
            $('#cookie-notice-container').show();
        } else {
            $('#cookie-notice-container').hide();
        }
    });
    window.setEUCookie = function () {
        docCookies.setItem('ajapaik_agreed_to_cookies', true, 'Fri, 31 Dec 9999 23:59:59 GMT', '/',
            'ajapaik.ee', false);
        $('#cookie-notice-container').hide();
    };
}());