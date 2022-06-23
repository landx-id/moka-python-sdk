
import base64
import requests
from .network import MokaResponse
from moka_python_sdk._config import production_api_url, staging_api_url


class _APIRequestor:
    @staticmethod
    def get(url, **kwargs):
        return _APIRequestor._request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return _APIRequestor._request("POST", url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return _APIRequestor._request("PATCH", url, **kwargs)
    
    @staticmethod
    def delete(url, **kwargs):
        return _APIRequestor._request("DELETE", url, **kwargs)

    @staticmethod
    def _request(
        method,
        url,
        api_key,
        secret_key,
        production=False,
        http_client=requests,
        headers={},
        body={},
        params={},
    ):
        """Send HTTP Method to given url
        Args:
            - method (str): HTTP Method that will be send
            - url (str): URL Directory that will be searched (not including base_url)
            - **api_key (string): API Key from xfers instance. Default to config if not provided
            - **base_url (string): Base url of the API. Default to config if not provided
            - **http_client (HTTPClientInterface): HTTP Client that adhere to HTTPClientInterface. Default to config if not provided
            - **headers: Headers of the request
            - **body: Body of the request. Only used on POST and PATCH request
            - **params: Parameters of the request. Only used on GET request
        """
        base_url = production_api_url if production else staging_api_url
        url = base_url + url

        headers = _APIRequestor._add_default_headers(api_key, secret_key, headers)
        if method == "GET":
            resp = http_client.request(method, url, headers=headers, params=params)
        else:
            resp = http_client.request(method, url, headers=headers, json=body)
        return MokaResponse(resp.status_code, resp.headers, resp.json())

    @staticmethod
    def _add_default_headers(api_key, secret_key, headers):
        headers["Content-type"] = "application/vnd.api+json"
        headers["Authorization"] = f"Basic {_APIRequestor._generate_auth(api_key, secret_key)}"
        return headers

    @staticmethod
    def _generate_auth(api_key, secret_key):
        auth_pair = api_key + ":" + secret_key
        auth_base64 = base64.b64encode(auth_pair.encode())
        return auth_base64.decode("utf-8")
