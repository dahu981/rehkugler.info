from django.conf import settings


def site_url(request):
    return {
        'SITE_URL': settings.SITE_URL,
        'CALENDLY_URL': getattr(settings, 'CALENDLY_URL', 'https://calendly.com/markusrehkugler/info-gesprach'),
        'CALENDLY_PARAGUAY_URL': getattr(settings, 'CALENDLY_PARAGUAY_URL', 'https://calendly.com/markusrehkugler/paraguay-erstgespraech'),
    }
