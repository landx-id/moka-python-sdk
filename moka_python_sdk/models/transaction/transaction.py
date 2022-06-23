from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from models._to_model import _to_model

from .entity.transaction import TransactionEntity

class Transaction:
    @staticmethod
    def show(
        *,
        outlet_id: int,
        per_page: int,
        since: float,
        until: float,
        time_filter: str,
        include_promo: bool,
        reorder_type: str,
        **kwargs
    ) -> TransactionEntity:
        """Send GET Request to Get all sales transactions.
        (API Reference : https://api.mokapos.com/docs#operation/showLatestTransactionsV3)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of records per page.
            - since (float): Start date in DD/MM/YYYY format
            - until (float): End date in DD/MM/YYYY format
            - time_filter (str): Type of fitler to be used by start and end parameters {created_at, updated_at, synchronized_at}
            - include_promo (bool): Include promo transactions in the result.
            - reorder_type (str): Sort results in ascending or descending order {ASC, DESC}
                
        Returns:
            data: Transaction data
        """
        url = f"/v3/outlets/{outlet_id}/reports/get_latest_transactions"
        params = {
            "per_page": per_page,
            "since": since,
            "until": until,
            "time_filter": time_filter,
            "include_promo": include_promo,
            "reorder_type": reorder_type,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=TransactionEntity, data=response.body['data'])
        else:
            raise MokaError(response)