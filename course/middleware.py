# myapp/middleware.py

from django.http import JsonResponse

class AuthRequiredMiddleware:
    """
    Middleware to ensure the user is authenticated for protected routes.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = [
            '/course',
            '/admin',         # Allow admin
            '/static',        # Static files
        ]

    def __call__(self, request):
        path = request.path

        # if not request.user.is_authenticated and not any(path.startswith(p) for p in self.public_paths):
        #     return JsonResponse({'error': 'Unauthorized'}, status=403)

        return self.get_response(request)
