from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LeadCaptureForm


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
        f'Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def llms_txt(request):
    from django.conf import settings
    site_url = getattr(settings, 'SITE_URL', f'{request.scheme}://{request.get_host()}')
    content = f"""# Rehkugler Immobilienbewertung

> Zertifizierte Immobiliengutachten nach §194 BauGB – unabhängig, gerichtsfest, deutschlandweit.

## Über Markus Rehkugler

Markus Rehkugler ist zertifizierter Immobiliengutachter und erstellt Verkehrswertgutachten für private und gewerbliche Immobilien. Schwerpunkte sind Erbschaft, Scheidung, Finanzierung, Kauf/Verkauf und Vermögensbewertung.

## Leistungen

- **Verkehrswertgutachten**: Rechtssichere Bewertung nach §194 BauGB, anerkannt bei Gerichten, Finanzämtern und Banken.
- **Kurzgutachten**: Kompakte Werteinschätzung für private Entscheidungen.
- **Sonderfälle**: Erbbaurecht, Nießbrauch, Wohnrecht, Denkmalschutz, Bauschäden.

## Bewertungsanlässe

- Erbschaft & Schenkung – Gutachten zur steuerlichen Bewertung
- Scheidung – Gerichtsfeste Verkehrswertgutachten
- Kauf & Verkauf – Unabhängige Marktbewertung
- Finanzierung – Beleihungswertgutachten für Banken
- Vermögen & Unternehmen – Bilanzielle Immobilienbewertung

## Häufige Fragen

- **Was kostet ein Verkehrswertgutachten?** Die Kosten hängen von Immobilientyp, Lage und Komplexität ab. Eine individuelle Einschätzung erfolgt nach Erstanfrage.
- **Wie lange dauert ein Gutachten?** In der Regel 2–4 Wochen nach Objektbesichtigung und Unterlageneingang.
- **Wird das Gutachten vor Gericht anerkannt?** Ja. Alle Gutachten entsprechen den Vorgaben des §194 BauGB und sind gerichtsfest.

## Kontakt

- Website: {site_url}
- E-Mail: info@rehkugler.info

## Links

- Startseite: {site_url}/
- Gutachten: {site_url}/gutachten/
- Bewertungsanlässe: {site_url}/anlaesse/
- Sonderfälle: {site_url}/sonderfaelle/
- Profil: {site_url}/profil/
- Kontakt: {site_url}/kontakt/
- Impressum: {site_url}/impressum/
- Datenschutz: {site_url}/datenschutz/
"""
    return HttpResponse(content.strip(), content_type='text/plain; charset=utf-8')
