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


// ===============================================
// Cookie Consent Library
// ===============================================
function initCookieConsent() {
  import('https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@3.0.1/dist/cookieconsent.umd.js')
    .then(() => {
      CookieConsent.run({
        guiOptions: {
          consentModal: {
            layout: 'box',
            position: 'bottom right',
            equalWeightButtons: true,
            flipButtons: false,
          },
          preferencesModal: {
            layout: 'box',
            position: 'right',
            equalWeightButtons: true,
            flipButtons: false,
          },
        },
        categories: {
          necessary: {
            readOnly: true,
            enabled: true,
          },
          functionality: {},
        },
        language: {
          default: 'de',
          autoDetect: 'browser',
          translations: {
            de: {
              consentModal: {
                title: "Hallo Reisende, es ist Kekszeit!",
                description: "Wir verwenden notwendige Cookies, um unsere Website zu betreiben. Weitere Cookies werden verwendet, um Inhalte zu personalisieren und Funktionen bereitzustellen.",
                acceptAllBtn: "Alle akzeptieren",
                acceptNecessaryBtn: "Nur notwendige akzeptieren",
                showPreferencesBtn: "Einstellungen verwalten",
                footer: "<a href='/datenschutz'>Datenschutz</a>"
              },
              preferencesModal: {
                title: "Präferenzen für die Zustimmung",
                acceptAllBtn: "Alle akzeptieren",
                acceptNecessaryBtn: "Nur notwendige akzeptieren",
                savePreferencesBtn: "Einstellungen speichern",
                closeIconLabel: "Modal schließen",
                sections: [
                  {
                    title: "Verwendung von Cookies",
                    description: "Wir verwenden Cookies, um Ihre Erfahrung auf unserer Website zu verbessern. Sie können Ihre Cookie-Einstellungen jederzeit ändern."
                  },
                  {
                    title: "Streng notwendige Cookies <span class=\"cc__badge cc__badge--primary\">Immer aktiv</span>",
                    description: "Diese Cookies sind notwendig, damit die Website funktioniert und können in unseren Systemen nicht ausgeschaltet werden.<br><br><strong>cookie_consent</strong>: Speichert den Zustimmungsstatus des Benutzers für Cookies auf der aktuellen Domäne.<br><strong>csrftoken</strong>: Wird verwendet, um Anfragen vor CSRF-Angriffen zu schützen.<br><strong>sessionid</strong>: Eindeutige Session-ID zur Identifizierung Ihrer Browser-Sitzung.",
                    linkedCategory: "necessary"
                  },
                  {
                    title: "Funktionalitäts-Cookies",
                    description: "Diese Cookies ermöglichen es der Website, verbesserte Funktionalität und Personalisierung zu bieten.<br><br><strong>django_language</strong>: Speichert die vom Benutzer ausgewählte Sprache auf der Website.",
                    linkedCategory: "functionality"
                  },
                  {
                    title: "Weitere Informationen",
                    description: "Für Fragen zu unserer Cookie-Richtlinie und Ihren Wahlmöglichkeiten lesen Sie bitte unsere <a class=\"cc__link\" href='/datenschutz'>Datenschutzerklärung</a>."
                  }
                ]
              }
            },
            es: {
              consentModal: {
                title: "¡Hola viajero, es hora de las cookies!",
                description: "Utilizamos cookies necesarias para operar nuestro sitio web. Se utilizan cookies adicionales para personalizar el contenido y proporcionar funciones.",
                acceptAllBtn: "Aceptar todo",
                acceptNecessaryBtn: "Aceptar solo las necesarias",
                showPreferencesBtn: "Gestionar preferencias",
                footer: "<a href='/datenschutz'>Política de privacidad</a>"
              },
              preferencesModal: {
                title: "Preferencias de consentimiento",
                acceptAllBtn: "Aceptar todo",
                acceptNecessaryBtn: "Aceptar solo las necesarias",
                savePreferencesBtn: "Guardar preferencias",
                closeIconLabel: "Cerrar modal",
                sections: [
                  {
                    title: "Uso de cookies",
                    description: "Utilizamos cookies para mejorar su experiencia en nuestro sitio web. Puede cambiar su configuración de cookies en cualquier momento."
                  },
                  {
                    title: "Cookies estrictamente necesarias <span class=\"cc__badge cc__badge--primary\">Siempre activas</span>",
                    description: "Estas cookies son necesarias para que el sitio web funcione y no se pueden desactivar en nuestros sistemas.<br><br><strong>cookie_consent</strong>: Almacena el estado de consentimiento del usuario para las cookies en el dominio actual.<br><strong>csrftoken</strong>: Se utiliza para proteger contra ataques de falsificación de solicitudes entre sitios.<br><strong>sessionid</strong>: ID de sesión único para identificar su sesión de navegador.",
                    linkedCategory: "necessary"
                  },
                  {
                    title: "Cookies de funcionalidad",
                    description: "Estas cookies permiten al sitio web proporcionar funcionalidad mejorada y personalización.<br><br><strong>django_language</strong>: Almacena el idioma seleccionado por el usuario en el sitio web.",
                    linkedCategory: "functionality"
                  },
                  {
                    title: "Más información",
                    description: "Para preguntas sobre nuestra política de cookies y sus opciones, por favor lea nuestra <a class=\"cc__link\" href='/datenschutz'>Política de privacidad</a>."
                  }
                ]
              }
            }
          }
        }
      });

      const cookieSettingsButton = document.getElementById('cookie-settings');
      if (cookieSettingsButton) {
        cookieSettingsButton.addEventListener('click', function (event) {
          event.preventDefault();
          CookieConsent.showPreferences();
        });
      }
    })
    .catch((error) => console.error('Cookie Consent konnte nicht geladen werden:', error));
}

// ── Init Cookie Consent
initCookieConsent();