// ── Mobile menu
var mobileMenu   = document.getElementById('mobile-menu');
var mobileToggle = document.getElementById('mobile-toggle');
var closeMenu    = document.getElementById('close-menu');

function openMenu() {
    mobileMenu.classList.remove('translate-x-full');
    mobileToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
}
function closeMenuFn() {
    mobileMenu.classList.add('translate-x-full');
    mobileToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
}

if (mobileToggle) {
    mobileToggle.addEventListener('click', openMenu);
}
if (closeMenu) {
    closeMenu.addEventListener('click', closeMenuFn);
}
if (mobileMenu) {
    mobileMenu.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', closeMenuFn);
    });
}

// ── Navbar solid on scroll
var navbar = document.getElementById('navbar');
if (navbar) {
    window.addEventListener('scroll', function() {
        if (window.scrollY > 60) {
            navbar.classList.add('nav-solid');
        } else {
            navbar.classList.remove('nav-solid');
        }
    }, { passive: true });
}

// ── Scroll-reveal
var revealEls = document.querySelectorAll('.fade-up');
var observer  = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.08 });
revealEls.forEach(function(el) { observer.observe(el); });

// ── Page-load: hero
window.addEventListener('load', function() {
    setTimeout(function() {
        document.querySelectorAll('#hero .fade-up').forEach(function(el) {
            el.classList.add('is-visible');
        });
    }, 100);
});
