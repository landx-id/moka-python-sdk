import requests
from ._moka_param_injector import _MokaParamInjector
from .network import HTTPClientInterface


class Moka:
    """Moka instance. Initialize this with your API Key and Secret Key."""

    def __init__(
        self,
        api_key,
        secret_key,
        production=False,
        http_client: HTTPClientInterface = requests,
    ):
        injected_params = (api_key, secret_key, production, http_client)
        param_injector = _MokaParamInjector(injected_params)

        self.Merchant = param_injector.instantiate_merchant()
        self.Library = param_injector.instantiate_library()
        self.Oauth = param_injector.instantiate_oauth()
        self.Report = param_injector.instantiate_report()
        self.Transaction = param_injector.instantiate_transaction()
