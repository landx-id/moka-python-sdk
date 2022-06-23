from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from .entity.subscription import SubscriptionEntity
from models._to_model import _to_model

class Subscription:
    @staticmethod
    def get(**kwargs):
        """Send GET Request to Get all subscription entities in this business.
        (API Reference : https://api.mokapos.com/docs#operation/createSubscriptionV1)

        Returns:
            data: Array of Subscription

        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body)
        else:
            raise MokaError(response)
    
    @staticmethod
    def create(**kwargs):
        """Send POST Request to Create a new subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/createSubscriptionV1)

        Args:
            - callback_uri (str): URL that will be called when the subscription is paid.
            - event_id (str): ID of the event that will be subscribed.

        Returns:
            data: Subscription data
        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def update(**kwargs):
        """Send PATCH Request to Update a subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/updateSubscriptionV1)

        Args:
            - callback_uri (str): URL that will be called when the subscription is paid.

        Returns:
            data: Subscription data
        """
        url = f"/v1/subscriptions"
        response = _APIRequestor.patch(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SubscriptionEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def delete(**kwargs):
        """Send DELETE Request to Delete a subscription entity.
        (API Reference : https://api.mokapos.com/docs#operation/deleteSubscriptionV1)

        Returns:
            data: "Your subscription for event 1 is destroyed."
        """
        url = f"/v1/subscriptions/{kwargs['subscription_id']}"
        response = _APIRequestor.delete(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return response.body
        else:
            raise MokaError(response)