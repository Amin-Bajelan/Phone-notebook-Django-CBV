from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'phone_notebook/index.html'