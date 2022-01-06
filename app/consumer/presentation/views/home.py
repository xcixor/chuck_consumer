from django.views.generic import TemplateView
from consumer.utils import ApiConsumer


util = ApiConsumer()


class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = util.get_categories()
        return context
