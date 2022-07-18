from django.urls import resolve
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.base import ContextMixin


class HtmxResponseMixin(TemplateResponseMixin, ContextMixin):
    """Extend Django's default TemplateResponseMixin to handle HTMX requests."""

    def get_template_names(self):
        """Determine the application name of the request and
        if there is an HTMX instance attached to it
        to return the appropriate template."""
        app_name = resolve(self.request.path).app_name
        return [f"{app_name}/{self.template_name}"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            context["base_template"] = "partial.html"
        else:
            context["base_template"] = "base.html"
        return context