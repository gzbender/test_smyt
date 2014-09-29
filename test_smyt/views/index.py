# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from test_smyt.models import generated_models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['models'] = generated_models.models.keys()
        return context

index = IndexView.as_view()
