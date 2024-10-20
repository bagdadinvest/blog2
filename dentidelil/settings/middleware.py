# custom_toolbar_middleware.py
from django.conf import settings
from debug_toolbar.middleware import DebugToolbarMiddleware

class CustomDebugToolbarMiddleware(DebugToolbarMiddleware):
    def __call__(self, request):
        # Check if the user is authenticated and is a superuser or admin
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            # Enable Debug Toolbar
            return super().__call__(request)
        else:
            # If the user is not authorized, simply pass through the request
            response = self.get_response(request)
            return response

