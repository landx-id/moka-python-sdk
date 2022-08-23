from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model

from .entity.subscription import SubscriptionEntity

class Subscription:
    @staticmethod
    def get(**kwargs) -> list[SubscriptionEntity]:
        """Send GET Request to Get all subscription entities in this business.
        (API Reference : https://api.mokapos.com/docs#operation/createSubscriptionV1)

        Returns:
            data: Array of Subscription

        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def create(*, callback_uri: str, event_id: int, **kwargs) -> SubscriptionEntity:
        """Send POST Request to Create a new subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/createSubscriptionV1)

        Args:
            - callback_uri (str): URL that will be called when the subscription is paid.
            - event_id (str): ID of the event that will be subscribed.

        Returns:
            data: Subscription Entity
        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def update(**kwargs) -> SubscriptionEntity:
        """Send PATCH Request to Update a subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/updateSubscriptionV1)

        Args:
            - callback_uri (str): URL that will be called when the subscription is paid.

        Returns:
            data: Subscription Entity
        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.patch(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def delete(subscription_id: str, **kwargs) -> str:
        """Send DELETE Request to Delete a subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/deleteSubscriptionV1)

        Returns:
            data: "Your subscription for event 1 is destroyed."
        """
        url = f"/v1/subscriptions/{subscription_id}"
        response = _APIRequestor.delete(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return response.body
        else:
            raise MokaError(response)
