__author__ = 'julien'
from django.conf import settings

# Choix des templates
# Desktop Browser   = Desktop Template
# Mobile Browser    = Mobile Template
class MobileMiddleware(object):
    def process_request(self, request):
        subdomain = request.META.get('HTTP_HOST', '').split('.')
        if 'm' in subdomain:
            settings.TEMPLATE_DIRS = settings.MOBILE_TEMPLATE_DIRS
        else:
            settings.TEMPLATE_DIRS = settings.DESKTOP_TEMPLATE_DIRS