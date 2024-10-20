from django.urls import path
from django_distill import distill_path
from django.shortcuts import render
from wagtail.core.models import Page

# Function to render pages based on the static HTML template structure
def render_static_page(request, template_name):
    # `template_name` should match the path within `pages/static/`
    return render(request, f'pages/static/{template_name}.html')

# Function to get all live URLs for the English locale from Wagtail
def get_english_page_urls():
    # Query all live, publicly accessible pages with the English locale
    pages = Page.objects.live().public().filter(locale__language_code='en')

    # Yield the relative URL for each page
    for page in pages:
        # `page.url_path` gives the path relative to the root without the domain
        # Ensure the path is correctly formatted (e.g., `/en/our-blogs/`)
        yield (page.url_path,)

# Generate urlpatterns dynamically based on the URLs from `get_english_page_urls()`
urlpatterns = []

for url_path in get_english_page_urls():
    # Extract the template name from the URL path
    # Example: "/en/our-blogs/" -> "our-blogs/index"
    template_name = url_path[0].strip('/').replace('/', '/index')
    
    # Add the `distill_path` for each dynamic URL
    urlpatterns.append(
        distill_path(
            url_path[0],  # URL pattern like `/en/our-blogs/`
            render_static_page,  # View function
            name=template_name.replace('/', '_'),  # Unique name for each path
            kwargs={'template_name': template_name}  # Pass template path
        )
    )

# Configuration for django-distill: using a dynamic URL generator
DISTILL_URLS = [(pattern.name, get_english_page_urls, pattern.name) for pattern in urlpatterns]
