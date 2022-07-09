from django.urls import resolve
from django.conf import settings

class HtmxResponseMiddleware(object):
    def __init__(self, get_response):
        """This method requires a get_response argument."""
        self.get_response = get_response

    def __call__(self, request):
        """This method is called every time a request is made."""
        return self.get_response(request)

    def process_template_response(self, request, response):
        """This special method is a middleware hook, which is called every time a view is finished executing."""
        app_name = resolve(request.path).app_name
        if app_name in settings.HTMX_APPS:
            if request.htmx:
                response.template_name = f"{app_name}/partials/{response.template_name[0]}"
            else:
                response.template_name = f"{app_name}/{response.template_name[0]}"
        return response
        
