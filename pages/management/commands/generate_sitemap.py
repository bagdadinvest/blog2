from django.core.management.base import BaseCommand
from django.http import HttpRequest
from wagtail.contrib.sitemaps.views import sitemap
import os

class Command(BaseCommand):
    help = 'Generates a static sitemap.xml file.'

    def handle(self, *args, **kwargs):
        # Create a request object with the required metadata
        request = HttpRequest()
        request.method = 'GET'
        request.META['HTTP_HOST'] = 'localhost'  # Replace with your domain
        request.META['SERVER_PORT'] = '8080'  # Set the port, usually '80' for HTTP or '443' for HTTPS

        # Get sitemap content
        response = sitemap(request)
        sitemap_content = response.content.decode('utf-8')

        # Define the path to save the sitemap
        sitemap_path = os.path.join('static', 'sitemap.xml')
        os.makedirs(os.path.dirname(sitemap_path), exist_ok=True)

        # Write the sitemap content to a file
        with open(sitemap_path, 'w') as sitemap_file:
            sitemap_file.write(sitemap_content)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {sitemap_path}'))
