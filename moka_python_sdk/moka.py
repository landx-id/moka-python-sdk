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

        self.PaymentMethod = param_injector.instantiate_payment_methods()
        self.Payment = param_injector.instantiate_payment()
        self.Balance = param_injector.instantiate_balance()
        self.Bank = param_injector.instantiate_bank()
        self.PaymentLink = param_injector.instantiate_payment_link()
        self.Disbursements = param_injector.instantiate_disbursements()