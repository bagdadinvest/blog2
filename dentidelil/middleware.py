# middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

LANGUAGE_BLOG_URLS = {
    'en': '/en/our-blogs/',
    'fr': '/fr/nos-blogs/',
    'es': '/es/nuestros-blogs/',
    'ar': '/ar//home-ar/blogs-ar/',
    'de': '/de/-blogs-de/',
    'pl': '/pl/nasze-blogi/',
    'tr': '/tr/bloglarimiz/',
}

class LanguageRedirectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and 'language' in request.POST:
            language = request.POST.get('language')
            if language in LANGUAGE_BLOG_URLS:
                redirect_url = LANGUAGE_BLOG_URLS[language]
                return redirect(redirect_url)
        return None

# yourapp/middleware.py

from django.shortcuts import render
from django.conf import settings
import logging

# Set up logging for debugging
logger = logging.getLogger(__name__)

class CatchAllExceptionsMiddleware:
    """
    Middleware to catch all unhandled exceptions and show a custom error page.
    If the user is a superuser and DEBUG is True, show Django's native debug page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Process the request normally
            response = self.get_response(request)
            return response
        except Exception as exception:
            # Handle any unhandled exception that occurs during request processing
            return self.process_exception(request, exception)

    def process_exception(self, request, exception):
        # Log the error for debugging purposes
        logger.error(f"Unhandled exception: {exception}", exc_info=True)

        # If the user is a superuser and DEBUG is enabled, raise the exception to show the native Django debug screen
        if request.user.is_authenticated and request.user.is_superuser and settings.DEBUG:
            raise exception

        # Render the custom error page for all other users
        return render(request, 'errors/page-404.html', status=500)
