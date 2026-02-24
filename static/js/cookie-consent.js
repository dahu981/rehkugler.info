(function () {
    'use strict';

    var COOKIE_NAME = 'cookie_consent';
    var COOKIE_DAYS = 365;

    // ── Cookie helpers ──

    function getCookie(name) {
        var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? match[2] : null;
    }

    function setCookie(name, value, days) {
        var d = new Date();
        d.setTime(d.getTime() + days * 86400000);
        document.cookie = name + '=' + value
            + ';expires=' + d.toUTCString()
            + ';path=/;SameSite=Lax;Secure';
    }

    // ── Banner show / hide ──

    var banner = document.getElementById('cookie-consent');
    if (!banner) return;

    function showBanner() {
        setTimeout(function () {
            banner.classList.remove('translate-y-full');
            banner.classList.add('translate-y-0');
        }, 800);
    }

    function hideBanner() {
        banner.classList.remove('translate-y-0');
        banner.classList.add('translate-y-full');
        setTimeout(function () {
            banner.remove();
        }, 600);
    }

    // ── Consent actions ──

    function acceptAll() {
        setCookie(COOKIE_NAME, 'all', COOKIE_DAYS);
        hideBanner();
        loadAnalytics();
    }

    function acceptNecessary() {
        setCookie(COOKIE_NAME, 'necessary', COOKIE_DAYS);
        hideBanner();
    }

    // ── Analytics loader ──

    function loadAnalytics() {
        var scripts = document.querySelectorAll('script[data-consent="analytics"]');
        scripts.forEach(function (blocked) {
            var s = document.createElement('script');
            Array.prototype.slice.call(blocked.attributes).forEach(function (attr) {
                if (attr.name !== 'type' && attr.name !== 'data-consent') {
                    s.setAttribute(attr.name, attr.value);
                }
            });
            if (blocked.textContent) {
                s.textContent = blocked.textContent;
            }
            blocked.parentNode.replaceChild(s, blocked);
        });
    }

    // ── Initialization ──

    var consent = getCookie(COOKIE_NAME);

    if (!consent) {
        showBanner();
    } else if (consent === 'all') {
        banner.remove();
        loadAnalytics();
    } else {
        banner.remove();
    }

    // ── Event listeners ──

    var btnAll = document.getElementById('cookie-accept-all');
    var btnNecessary = document.getElementById('cookie-accept-necessary');

    if (btnAll) btnAll.addEventListener('click', acceptAll);
    if (btnNecessary) btnNecessary.addEventListener('click', acceptNecessary);
})();
