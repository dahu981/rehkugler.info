import re


class StaticCacheMiddleware:
    """Add Cache-Control headers to static file responses."""

    STATIC_RE = re.compile(r'\.(css|js|woff2|webp|png|jpg|jpeg|ico|svg)$', re.IGNORECASE)

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self.STATIC_RE.search(request.path):
            response['Cache-Control'] = 'public, max-age=31536000, immutable'
        return response
