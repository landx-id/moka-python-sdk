from inspect import isclass, signature


from .models.merchant.merchant import Merchant
from .models.report.report import Report
from .models.oauth.oauth import OAuth
from .models.library import Library
from .models.transaction import Transaction
import inspect

class _MokaParamInjector:
    """Builder class to inject parameters (api_key, base_url, http_client) to feature class"""

    def __init__(self, params):
        self.params = params

    def instantiate_merchant(self) -> Merchant:
        return self.instantiate(Merchant)

    def instantiate_library(self) -> Library:
        return self.instantiate(Library)

    def instantiate_oauth(self) -> OAuth:
        return self.instantiate(OAuth)

    def instantiate_report(self) -> Report:
        return self.instantiate(Report)
    
    def instantiate_transaction(self) -> Transaction:
        return self.instantiate(Transaction)

    def instantiate(self, injected_class):
        """Inject every static method in `injected_class` with provided parameters.

        Args:
            - injected_class (class): Class that will be injected

        Return:
            injected_class
        """
        params = self.params

        injected_class = type(
            injected_class.__name__,
            injected_class.__bases__,
            dict(injected_class.__dict__),
        )
        for keys, value in vars(injected_class).items():
            if type(value) == staticmethod and not keys.startswith("_"):
                _MokaParamInjector._inject_function(
                    injected_class, params, keys, value
                )
            if inspect.isclass(value) and not keys.startswith("_"):
                setattr(injected_class, keys, self.instantiate(value))
        
        return injected_class

    @staticmethod
    def _inject_function(injected_class, params, func_name, func_value):
        """Inject `func_name` function with params"""
        api_key, secret_key, production, http_client = params
        attr = func_value.__func__

        def inject_func_with_api_key(*args, **kwargs):
            kwargs["api_key"] = api_key
            kwargs["secret_key"] = secret_key
            kwargs["production"] = production
            kwargs["http_client"] = http_client
            result = attr(*args, **kwargs)
            return result

        inject_func_with_api_key.__signature__ = signature(attr)
        setattr(injected_class, func_name,
                staticmethod(inject_func_with_api_key))
