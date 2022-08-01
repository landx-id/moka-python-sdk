from os import stat
from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.merchant import (
    BusinessInfo, BusinessSetting, CustomerEntity,
    LoyaltyEntity, OutletEntity, UserInfo,
    UserQuota
)

class Merchant:
    @staticmethod
    def show_business_info(
        **kwargs
    ) -> BusinessInfo:
        """
        Returns the merchant's business information
        (API Reference: https://api.mokapos.com/docs#operation/showBusinessInformationV1)
        """
        url = "v1/businesses"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=BusinessInfo, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def get_business_checkout_setting(
        *,
        business_id: int,
        **kwargs
    ) -> BusinessInfo:
        """
        Retrieve the checkout settings of a business
        (API Reference: https://api.mokapos.com/docs#operation/getBusinessCheckoutSettingsV1)
        """
        url = f"v1/businesses/{business_id}/checkout_settings"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=BusinessSetting, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def get_list_customer(
        *,
        business_id: int,
        mobile_device: int,
        page: int,
        per_page: int,
        since: float = None,
        until: float = None,
        include_deleted: bool,
        include_loyalty: bool,
        **kwargs
    ) -> CustomerEntity:
        """
        Returns all customers on the outlet that the user has access to
        (API Reference: https://api.mokapos.com/docs#operation/listCustomersV1)
        """
        url = f"v1/businesses/{business_id}/customers"
        params = {
            "mobile_device": mobile_device,
            "page": page,
            "per_page": per_page,
            "since": since,
            "until": until,
            "include_deleted": include_deleted,
            "include_loyalty": include_loyalty
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=CustomerEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_loyalty_program(
        *,
        business_id: int,
        **kwargs
    ) -> List[LoyaltyEntity]:
        """
        Returns all the loyalties programs of a merchant
        (API Reference: https://api.mokapos.com/docs#operation/showLoyaltyProgramV1)
        """
        url = f"v1/businesses/{business_id}/loyalties/programs"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[LoyaltyEntity], data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def get_list_outlets(
        *,
        business_id: int,
        **kwargs
    ) -> OutletEntity:
        """
        Returns current user outlets information
        (API Reference: https://api.mokapos.com/docs#operation/listOutletsInformationV1)

        """
        url = f"v1/businesses/{business_id}/outlets"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=OutletEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_user_info(
        **kwargs
    ) -> UserInfo:
        """
        Returns current user information that logged in
        (API Reference: https://api.mokapos.com/docs#operation/showUserInformation)

        """
        url = "v1/profile/self"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=UserInfo, data=response.body)
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_quota(
        **kwargs
    ) -> UserQuota:
        """
        Returns remaining quota of an outlet when calling certain API.
        (API Reference: https://api.mokapos.com/docs#operation/showQuotaInformationV1)

        """
        url = "v1/quotas"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=UserQuota, data=response.body["data"])
        else:
            raise MokaError(response)