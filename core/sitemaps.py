from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    i18n = True

    def items(self):
        return ['core:home', 'core:datenschutz', 'core:impressum']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'core:home':
            return 1.0
        return 0.3
