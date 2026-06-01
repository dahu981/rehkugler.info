from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

LAST_MODIFIED = {
    'core:home': datetime(2026, 6, 1),
    'core:py_strukturberatung': datetime(2026, 5, 15),
    'core:py_investieren': datetime(2026, 5, 15),
    'core:py_immobilien': datetime(2026, 5, 15),
    'core:py_leben': datetime(2026, 5, 15),
    'core:py_videos': datetime(2026, 5, 15),
    'core:py_download_eas': datetime(2026, 5, 15),
    'core:py_download_steuern': datetime(2026, 5, 15),
    'core:datenschutz': datetime(2026, 2, 24),
    'core:impressum': datetime(2026, 2, 24),
}


class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    i18n = True

    def items(self):
        return [
            'core:home', 'core:datenschutz', 'core:impressum',
            'core:py_strukturberatung', 'core:py_investieren',
            'core:py_immobilien', 'core:py_leben', 'core:py_videos',
            'core:py_download_eas', 'core:py_download_steuern',
        ]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return LAST_MODIFIED.get(item)

    def priority(self, item):
        if item == 'core:home':
            return 1.0
        if item.startswith('core:py_'):
            return 0.7
        return 0.3
