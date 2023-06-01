from django.views.generic import base


class Main(base.TemplateView):
    template_name = "main/main.html"
