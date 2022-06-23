from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from .entity.subscription import SubscriptionEntity
from models._to_model import _to_model

class Subscription:
    @staticmethod
    def get(**kwargs):
        """Send GET Request to Get all events available in MOKA
        (API Reference : https://api.mokapos.com/docs#operation/getEventsV1)

        Returns:
            data: Array of Events

        """
        url = f"/v1/events"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body)
        else:
            raise MokaError(response)
