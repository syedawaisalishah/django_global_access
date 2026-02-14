from django.conf import settings

class GlobalAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        # Allow all hosts if not set
        if not settings.ALLOWED_HOSTS:
            settings.ALLOWED_HOSTS = ['*']

    def __call__(self, request):
        response = self.get_response(request)
        return response
