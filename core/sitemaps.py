from django.contrib.sitemaps import Sitemap
from django.urls import reverse


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

    def priority(self, item):
        if item == 'core:home':
            return 1.0
        if item.startswith('core:py_'):
            return 0.7
        return 0.3
