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
