# django-htmx-refresh

This is a Django app to handle full-page reloads with HTMX.

There are two possible use-cases for this app.

## Quick start

1. django-htmx-refresh relies on the django-htmx package. You can install it with pip:

```
    pip install django-htmx
```

2. Add "django_htmx_refresh" to your INSTALLED_APPS setting:

```
    INSTALLED_APPS = [
        ...
        'django_htmx_refresh',
    ]
```

3. Include an app namespace for your project's urls:

```
    path('app_path', include(('app.urls', 'app_namespace'))),
```

### Middleware

For when you want to handle htmx requests in all the views of a particular app.

4. Create a new list in your settings called HTMX_APPS:

```
    HTMX_APPS = [
        'your_apps_here'
    ]
```

This is so our custom middleware class only affects apps we explicity define, preventing errors with other third-party apps such as the default django admin application.

**Note**: The `HtmxReseponseMiddleware` class provided with this application uses the `process_template_response` hook, meaning any view you intend to be used with this class must return a response object that implements a `render` method. Luckily Django's class-based views do this for us with `TemplateResponse`.

### Mixin

For when you want to handle htmx requests in most of your views but not necessarily all of them.

4. Import the HtmxResponseMixin and add it to your view(s).

```
    from django_htmx_refresh.mixins import HtmxResponseMixin

    class ExampleView(TemplateView, HtmxResponseMixin):
        template_name = 'template_name.html'
```
