import requests


class ApiConsumer(object):

    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes/'

    def build_url(self, path=None, query=None, query_param=None):
        url = self.base_url
        if path:
            url += path
        if query and query_param:
            url += f'?{query}={query_param}'
        return url

    def get_categories(self):
        url = self.build_url('categories')
        result = requests.get(url)
        categories = result.json()
        return categories

    def search_content(self, query_param):
        url = self.build_url(path='search', query='query', query_param=query_param)
        result = requests.get(url)
        content = result.json()['result']
        return content
