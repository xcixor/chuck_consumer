import requests


class ApiConsumer(object):

    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes/'

    def build_url(self, path=None, query=None, query_param=None):
        """Build url from given parameters

        Args:
            path (string, optional): additional path for base_url. Defaults to None.
            query (string, optional): keyword to query API. Defaults to None.
            query_param (string, optional): the item to search for. Defaults to None.

        Returns:
            string: the url constructed with provided parameters.
        """
        url = self.base_url
        if path:
            url += path
        if query and query_param:
            url += f'?{query}={query_param}'
        return url

    def get_categories(self):
        """Fetches categories from the API

        Returns:
            list: list of found categories.
        """
        url = self.build_url('categories')
        result = requests.get(url)
        categories = result.json()
        return categories

    def search_content(self, query_param):
        """Searches the API for a given query

        Args:
            query_param (string): [the item to search for]

        Returns:
            dict: response with found items.
        """
        url = self.build_url(path='search', query='query', query_param=query_param)
        result = requests.get(url)
        content = result.json()
        return content
