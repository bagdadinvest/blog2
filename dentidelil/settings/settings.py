from django.conf import settings

class BrotliExcludeMiddleware:
    """
    Custom middleware to exclude specific file types (e.g., images) from Brotli compression.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for a media file
        if request.path.startswith(settings.MEDIA_URL):
            # Do not apply Brotli compression for media files
            return self.get_response(request)
        return self.get_response(request)
