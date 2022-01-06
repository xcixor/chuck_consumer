from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
from consumer.utils import ApiConsumer


util = ApiConsumer()


class GetCategoryContentView(View):

    def get(self, request, **kwargs):
        query_param = self.kwargs['query_param']
        result = util.search_content(query_param)
        is_ajax = self.request.META.get(
            'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return JsonResponse(result)
        return HttpResponse(result)