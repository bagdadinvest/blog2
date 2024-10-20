# urls.py
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path  # Use path and re_path instead of url
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.images.views.serve import ServeView
from wagtail.core import urls as wagtail_urls
from django.shortcuts import redirect
from pages.views import language_switch_redirect
from search import views as search_views
from wagtail_feeds.feeds import BasicFeed, BasicJsonFeed, ExtendedFeed, ExtendedJsonFeed

# Custom error handlers


# Language blog URLs for redirect logic
LANGUAGE_BLOG_URLS = {
    'en': '/en/our-blogs/',
    'fr': '/fr/nos-blogs/',
    'es': '/es/nuestros-blogs/',
    'ar': '/ar/home-ar/blogs-ar/',
    'de': '/de/blogs-de/',
    'pl': '/pl/nasze-blogi/',
    'tr': '/tr/bloglarimiz/',
}

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Django admin URL
    path('i18n/', include('django.conf.urls.i18n')),  # Language change URL
    path('documents/', include(wagtaildocs_urls)),  # Wagtail document handling
    path('sitemap.xml', sitemap),  # Sitemap handling
    path('rosetta/', include('rosetta.urls')),  # Rosetta translation URLs
    path('switch-language/', language_switch_redirect, name='switch_language_redirect'),

    # URLs for custom apps
    path('websites/', include("websites.urls")),  # Websites app URLs
    path('topblogs/', include('topblogs.urls')),  # TopBlogs app URLs
]

# Add i18n patterns to handle localization of URLs
urlpatterns += i18n_patterns(
    path('admin/', include(wagtailadmin_urls)),  # Wagtail admin panel
    path('users/', include('users.urls')),  # User and account URLs
    path('accounts/', include('allauth.urls')),  # Authentication URLs
    path('search/', search_views.search, name='search'),  # Search functionality

    # Blog feeds
    path('blog/feed/basic', BasicFeed(), name='basic_feed'),
    path('blog/feed/extended', ExtendedFeed(), name='extended_feed'),
    path('blog/feed/basic.json', BasicJsonFeed(), name='basic_json_feed'),
    path('blog/feed/extended.json', ExtendedJsonFeed(), name='extended_json_feed'),

    # Serve images
    re_path(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),

    # Fallback to Wagtail's page serving mechanism
    path('', include(wagtail_urls)),  # Serve Wagtail pages at the root URL
)

# Only include static and media file handling in DEBUG mode
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic.base import RedirectView

    # Serve static files
    urlpatterns += staticfiles_urlpatterns()

    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Handle favicon
    urlpatterns += [
        path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico', permanent=True)),
    ]

    # Enable debug toolbar if installed
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
