from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def datenschutz(request):
    return render(request, 'core/datenschutz.html')


def impressum(request):
    return render(request, 'core/impressum.html')


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        '',
        'Disallow: /admin/',
        '',
        f'Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')
