# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from apps.log_views import action_log_view  # Import the view from log_views.py

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),  # Add this line
    path("", include("websites.urls")),  # Websites app URLs
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('action-log/', action_log_view, name='action_log'),  # Moved outside the admin/ path
    path('accounts/', include('allauth.urls')),
    path('apps/', include("apps.urls")),  # Main app URLs for 'apps'
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls')),  # Rosetta for translation management
    path('cms/', include(wagtailadmin_urls)),  # Wagtail admin URLs
    path('documents/', include(wagtaildocs_urls)),  # Wagtail document management
    path('wag/', include(wagtail_urls)),  # Wagtail site pages
    path('topblogs/', include('topblogs.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),  # Django Debug Toolbar
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
