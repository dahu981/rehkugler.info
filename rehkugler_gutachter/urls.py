from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView

from core.sitemaps import StaticSitemap

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('robots.txt', include('core.urls_robots')),
    path('llms.txt', include('core.urls_llms')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^de/(?P<path>.*)$', lambda request, path: RedirectView.as_view(url='/%(path)s' % {'path': path}, permanent=True)(request)),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
