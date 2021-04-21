"""
ApiKey in Query auth plugin for HTTPie.

(C) Dj Walker-Morgan 2021

Includes MIT licensed code from Colin Bounouar
at https://github.com/Colin-b/requests_auth
"""
from httpie.plugins import AuthPlugin
import requests 
from urllib.parse import parse_qs, urlsplit, urlunsplit, urlencode


__version__ = '0.0.1'
__author__ = 'Dj Walker-Morgan'
__licence__ = 'BSD'

class QueryApiKey(requests.auth.AuthBase):
    """Describes an API Key requests authentication."""

    def __init__(self, api_key: str, query_parameter_name: str = None):
        """
        :param api_key: The API key that will be sent.
        :param query_parameter_name: Name of the query parameter. "api_key" by default.
        """
        self.api_key = api_key
        if not api_key:
            raise Exception("API Key is mandatory.")
        self.query_parameter_name = query_parameter_name or "api_key"

    def _add_parameters(self,initial_url: str, extra_parameters: dict) -> str:
        """
        Add parameters to an URL and return the new URL.
        :param initial_url:
        :param extra_parameters: dictionary of parameters name and value.
        :return: the new URL containing parameters.
        """
        scheme, netloc, path, query_string, fragment = urlsplit(initial_url)
        query_params = parse_qs(query_string)
        query_params.update(
            {
                parameter_name: [parameter_value]
                for parameter_name, parameter_value in extra_parameters.items()
            }
        )

        new_query_string = urlencode(query_params, doseq=True)

        return urlunsplit((scheme, netloc, path, new_query_string, fragment))

    def __call__(self, r):
        r.url = self._add_parameters(r.url, {self.query_parameter_name: self.api_key})
        return r

class ApiKeyQueryAuthPlugin(AuthPlugin):

    name = 'ApiKeyQuery auth'
    auth_type = 'apikey'
    description = ''

    def get_auth(self, username, password):
        return QueryApiKey(query_parameter_name=username, api_key=password)
        