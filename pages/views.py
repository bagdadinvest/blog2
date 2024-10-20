# views.py in your 'pages' app
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect
import logging

# Set up logging for debugging
logger = logging.getLogger(__name__)

def unified_error_view(request, exception=None, status_code=500):
    """
    Unified error view to handle 404, 500, and other HTTP errors.
    Shows custom error page for normal users and native Django debug page for superusers.
    """
    # Check if the user is authenticated and is a superuser, and if DEBUG is True
    if request.user.is_authenticated and request.user.is_superuser and settings.DEBUG:
        # Raise the exception to trigger Django's debug screen in development
        if exception:
            raise exception

    # Log the exception for debugging purposes
    logger.error(f"Error encountered: {exception}, Status Code: {status_code}")

    # Render the custom error page for all users
    return render(request, 'errors/custom_error.html', status=status_code)

def set_language(request):
    """View to change the user's preferred language and update session accordingly."""
    if request.method == 'POST':
        language = request.POST.get('language')
        next_url = request.POST.get('next', '/')

        # Log the POST data for debugging purposes
        logger.debug(f"POST data: {request.POST}")

        # Validate the language input
        if language and language in dict(settings.LANGUAGES):
            logger.info(f"Switching to language: {language}")
            # Activate and set the selected language
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language
        else:
            logger.warning(f"Invalid language selection: {language}")
            # Redirect to the homepage with a message or handle error

        return HttpResponseRedirect(next_url)
    else:
        logger.error(f"Invalid request method: {request.method}")
        return redirect('home')  # Replace 'home' with your homepage route

def language_switch_redirect(request):
    """Redirect user to the appropriate blog index page when language is switched."""
    language = request.POST.get('language')
    redirect_url = LANGUAGE_BLOG_URLS.get(language, '/')
    return redirect(redirect_url)
