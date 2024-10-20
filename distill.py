from django.urls import path
from django_distill import distill_path
from wagtail.core.models import Page

# Function to retrieve all English page URLs
def get_english_pages():
    # Retrieves all live and public English pages
    english_pages = Page.objects.live().public().filter(locale__language_code='en')
    for page in english_pages:
        yield (page.url,)

# Define your urlpatterns
urlpatterns = [
    # Specify the pages to export using distill_path and pass the URL generator
    distill_path('', 'myapp.views.home', name='home', distill_func=get_english_pages),
    distill_path('our-blogs/', 'myapp.views.blog', name='blog', distill_func=get_english_pages),
    distill_path('our-blogs/<slug:slug>/', 'myapp.views.blog_detail', name='blog_detail', distill_func=get_english_pages),
]

# Specify the DISTILL_URLS configuration for exporting static pages
DISTILL_URLS = [
    ('home', get_english_pages, 'home'),
    ('blog', get_english_pages, 'blog'),
    ('blog_detail', get_english_pages, 'blog_detail'),
]
