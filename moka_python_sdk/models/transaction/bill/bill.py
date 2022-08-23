from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.bill import BillEntity, BillData

class Bill:
    @staticmethod
    def get(
        *,
        outlet_id: int,
        page: int,
        per_page: int,
        sort: str = None,
        start: str = None,
        end: str = None,
        last_pull: str = None,
        statuses: str = None,
        dine_in_only: bool = True,
        deep: bool = True,
        **kwargs
    ) -> dict:
        """Send GET Request to Get a bill.
        (API Reference : https://api.mokapos.com/docs#operation/listBillsV1)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - page (int): Page number.
            - per_page (int): Number of records per page.
            - sort (str): Sort results in ascending or descending order {ASC, DESC}
            - start (str): Start date in DD/MM/YYYY format
            - end (str): End date in DD/MM/YYYY format
            - last_pull (str): Last pull date in DD/MM/YYYY format
            - statuses (str): Comma separated list of bill statuses {paid, unpaid, void, refunded, partial_refunded, partial_paid}
            - dine_in_only (bool): Filter results to only dine-in bills.
            - deep (bool): Include related objects in the result.
            
        Returns:
            data: Bill data
        """
        url = f"/v1/outlets/{outlet_id}/sync_bills/"
        params = {
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "start": start,
            "end": end,
            "last_pull": last_pull,
            "statuses": statuses,
            "dine_in_only": dine_in_only,
            "deep": deep,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=BillData, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def get_detail(
        *,
        outlet_id: int,
        bill_id: int,
        **kwargs
    ) -> dict:
        """Send GET Request to Get a bill.
        (API Reference : https://api.mokapos.com/docs#operation/listBillByIDV1)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - bill_id (int): ID of the bill that will be searched.
            
        Returns:
            data: Detail Bill data
        """
        url = f"/v1/outlets/{outlet_id}/sync_bills/{bill_id}"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=BillEntity, data=response.body['data'])
        else:
            raise MokaError(response)