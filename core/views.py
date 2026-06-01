import logging

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LeadCaptureForm

logger = logging.getLogger(__name__)

RESOURCE_LABELS = {
    'eas': 'EAS-Leitfaden (Paraguay)',
    'steuern': 'Steuer-Leitfaden (Paraguay)',
}


def _notify_lead(email, resource):
    label = RESOURCE_LABELS.get(resource, resource)
    try:
        send_mail(
            subject=f'Neuer Download: {label}',
            message=f'{email} hat den {label} heruntergeladen.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
    except Exception:
        logger.exception('Lead-Benachrichtigung konnte nicht gesendet werden')


def home(request):
    return render(request, 'core/home.html')


def datenschutz(request):
    return render(request, 'core/datenschutz.html')


def impressum(request):
    return render(request, 'core/impressum.html')


# --- Paraguay Landing Pages ---

def py_strukturberatung(request):
    return render(request, 'core/paraguay/strukturberatung.html')


def py_investieren(request):
    return render(request, 'core/paraguay/investieren.html')


def py_immobilien(request):
    return render(request, 'core/paraguay/immobilien.html')


def py_leben(request):
    return render(request, 'core/paraguay/leben.html')


def py_videos(request):
    return render(request, 'core/paraguay/videos.html')


# --- Paraguay Downloads ---

def py_download_eas(request):
    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.resource = 'eas'
            lead.save()
            _notify_lead(lead.email, lead.resource)
            return redirect('core:py_download_eas_success')
    else:
        form = LeadCaptureForm()
    return render(request, 'core/paraguay/download_eas.html', {'form': form})


def py_download_eas_success(request):
    return render(request, 'core/paraguay/download_success.html', {
        'resource_title': 'EAS Paraguay – Der Praxisleitfaden',
        'download_file': 'downloads/EAS-Paraguay-Leitfaden.pdf',
    })


def py_download_steuern(request):
    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.resource = 'steuern'
            lead.save()
            _notify_lead(lead.email, lead.resource)
            return redirect('core:py_download_steuern_success')
    else:
        form = LeadCaptureForm()
    return render(request, 'core/paraguay/download_steuern.html', {'form': form})


def py_download_steuern_success(request):
    return render(request, 'core/paraguay/download_success.html', {
        'resource_title': 'Steuern in Paraguay – Das Wichtigste im Überblick',
        'download_file': 'downloads/Steuern-Paraguay-Handout.pdf',
    })


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        '',
        'Disallow: /admin/',
        '',
        '# AI Crawlers',
        'User-agent: GPTBot',
        'Allow: /',
        'Disallow: /admin/',
        '',
        'User-agent: ChatGPT-User',
        'Allow: /',
        '',
        'User-agent: Google-Extended',
        'Allow: /',
        '',
        'User-agent: PerplexityBot',
        'Allow: /',
        '',
        'User-agent: ClaudeBot',
        'Allow: /',
        '',
        'User-agent: OAI-SearchBot',
        'Allow: /',
        '',
        'User-agent: Applebot-Extended',
        'Allow: /',
        '',
        f'Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def llms_txt(request):
    from django.conf import settings
    site_url = getattr(settings, 'SITE_URL', f'{request.scheme}://{request.get_host()}')
    content = f"""# Markus Rehkugler – Struktur schafft Klarheit

> Markus Rehkugler ist Immobilienexperte, Dipl.-Sachverständiger (DIA) und Unternehmerbegleiter mit über 25 Jahren Erfahrung. Er lebt und arbeitet zwischen Deutschland und Paraguay und berät Unternehmer, Investoren und Eigentümer an der Schnittstelle von Immobilien, Unternehmensstruktur und persönlicher Transformation.

## Über Markus Rehkugler

Markus Rehkugler ist Dipl.-Finanzwirt (FH) und Dipl.-Sachverständiger (DIA) für Immobilienbewertung. Seit über 25 Jahren bewertet er Immobilien, berät Eigentümer und Investoren und arbeitet an der Schnittstelle von Zahlen, Strukturen und Entscheidungen. Seit 2019/2020 lebt er zwischen Deutschland und Paraguay, mit eigenen Gesellschaften, Steuerpflichten und operativer Erfahrung vor Ort. Als Präsident des Directorio einer paraguayischen Immobiliengesellschaft kennt er den Markt aus erster Hand.

## Immobilienberatung Deutschland

- Verkehrswertgutachten und Sachverständigenbewertungen
- Strukturierte Immobilienberatung für Eigentümer, Investoren und Profis
- Website: [REHKUGLER Immobilien](https://www.rehkugler.info)

## Paraguay – Struktur & Orientierung

Strukturierte Einordnung für deutsche Unternehmer und Investoren, die Paraguay ernsthaft prüfen: Gesellschaftsformen (EAS, S.A., S.R.L.), Steuern (Territorialprinzip, IRE, IVA, IDU, IRP), Bankfähigkeit, Kapitalfluss und Residencia.

- [Strukturberatung Paraguay]({site_url}/paraguay/strukturberatung/)
- [Investieren in Paraguay]({site_url}/paraguay/investieren/)
- [Immobilien in Paraguay]({site_url}/paraguay/immobilien/)
- [Leben in Paraguay]({site_url}/paraguay/leben/)
- [Videos]({site_url}/paraguay/videos/)

## Transformation & Unternehmerbegleitung

Begleitung für Unternehmer in komplexen Situationen – finanziell, strukturell oder innerlich. Analytische Reflexion und strukturiertes Denken statt schneller Lösungen.

- Website: [Transformation Guide](https://www.markus-rehkugler.de)

## Kontakt

- E-Mail: mr@markus-rehkugler.info
- WhatsApp: +49 151 66555888
- Calendly: https://calendly.com/markusrehkugler/info-gesprach

## Links

- [Startseite]({site_url}/)
- [Impressum]({site_url}/impressum/)
- [Datenschutz]({site_url}/datenschutz/)

## Optional

- [REHKUGLER Immobilien](https://www.rehkugler.info) – Gutachten & Bewertung Deutschland
- [Transformation Guide](https://www.markus-rehkugler.de) – Unternehmerbegleitung
- [Immo-Gutachter](https://www.immo-gutachter.info) – Sachverständigenportal
"""
    return HttpResponse(content.strip(), content_type='text/plain; charset=utf-8')
