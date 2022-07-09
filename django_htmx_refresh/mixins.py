from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HtmxResponseMixin(LoginRequiredMixin, TemplateResponseMixin):
    """Extend Django's default TemplateResponseMixin to handle HTMX requests."""

    def get_template_names(self):
        """Determine the application name of the request and
        if there is an HTMX instance attached to it
        to return the appropriate template."""
        app_name = resolve(self.request.path).app_name
        if self.request.htmx:
            return [f"{app_name}/partials/{self.template_name}"]
        return [f"{app_name}/{self.template_name}"]