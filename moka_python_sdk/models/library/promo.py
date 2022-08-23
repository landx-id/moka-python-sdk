from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.promo import PromoEntity

class Promo:
    @staticmethod
    def get(
        *,
        outlet_id: int,
        active: bool,
        per_page: int,
        **kwargs
    ) -> dict:
        """Send GET Request to Get all promos on the outlet that the user has access.
        (API Reference : https://api.mokapos.com/docs#operation/listPromosV1)
        
        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - active (bool): Include active promos in the result.
            - per_page (int): Number of elements per page.
        
        Returns:
            data: Promo data
        """
        url = f"/v1/outlets/{outlet_id}/promos"

        params = {
            "active": active,
            "per_page": per_page,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[PromoEntity], data=response.body['data'])
        else:
            raise MokaError(response)