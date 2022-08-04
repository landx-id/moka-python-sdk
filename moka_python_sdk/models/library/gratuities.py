from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.gratuities import GratuitiesEntity

class Gratuities:
    @staticmethod
    def get(
        *,
        outlet_id: int,
        page: int,
        per_page: int,
        since: float = None,
        until: float = None,
        include_deleted: bool,
        **kwargs
    ) -> dict:
        """Send GET Request to Get all gratuities on the outlet that the user has access.
        (API Reference : https://api.mokapos.com/docs#operation/listGratuitiesV1)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - page (int): Page number.
            - per_page (int): Number of elements per page.
            - since (float): The initial range of time in Epoch format
            - until (float): The final range of time in Epoch format
            - include_deleted (bool): Include deleted gratuities in the result.
            
        Returns:
            data: Gratuities data
        """
        url = f"/v1/outlets/{outlet_id}/gratuities"

        params = {
            "page": page,
            "per_page": per_page,
            "since": since,
            "until": until,
            "include_deleted": include_deleted,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=GratuitiesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
