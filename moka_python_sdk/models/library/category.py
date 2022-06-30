from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from models._to_model import _to_model
from typing import List

from entity.category import CategoryEntity

class Category:
    @staticmethod
    def get(
        *,
        outlet_id: int,
        page: int,
        per_page: int,
        since: float,
        until: float,
        include_deleted: bool,
        **kwargs
    ) -> dict:
        """Send GET Request to Get all categories on the outlet that the user has access.
        (API Reference : https://api.mokapos.com/docs#tag/Categories)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - page (int): Page number.
            - per_page (int): Number of records per page.
            - since (float): Start date in DD/MM/YYYY format
            - until (float): End date in DD/MM/YYYY format
            - include_deleted (bool): Include deleted categories in the result.
            
        Returns:
            data: Category data
        """
        url = f"/v1/outlets/{outlet_id}/categories"

        params = {
            "page": page,
            "per_page": per_page,
            "since": since,
            "until": until,
            "include_deleted": include_deleted,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[CategoryEntity], data=response.body['data'])
        else:
            raise MokaError(response)
