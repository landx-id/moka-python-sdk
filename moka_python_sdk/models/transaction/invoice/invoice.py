from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model

from .entity.invoice import InvoiceEntity, InvoiceData

class Invoice:
    @staticmethod
    def report(
        *,
        outlet_id: str,
        per_page: int = 10,
        page: int = 1,
        start: float = None,
        end: float = None,
        time_filter: str = None,
        reorder_type: str = None,
        **kwargs
    ) -> InvoiceEntity:
        """Send GET Request to Get invoices.
        (API Reference : https://api.mokapos.com/docs#operation/reportInvoicesV3)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - per_page (int): Number of items per page.
            - page (int): Page number.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format
            - time_filter (str): Type of fitler to be used by start and end parameters {created_at, updated_at, synchronized_at}
            - reorder_type (str): Sort results in ascending or descending order {ASC, DESC}

        Returns:
            data: Array invoices
        """
        url = f"/v3/outlets/{outlet_id}/reports/invoices"
        body = {
            "per_page": per_page,
            "page": page,
            "start": start,
            "end": end,
            "time_filter": time_filter,
            "reorder_type": reorder_type,
        }
        response = _APIRequestor.get(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=InvoiceEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def report_detail(
        *,
        outlet_id: str,
        invoice_id: str,
        **kwargs
    ) -> InvoiceEntity:
        """Send GET Request to Get invoice detail.
        (API Reference : https://api.mokapos.com/docs#operation/reportInvoiceDetailV3)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - invoice_id (str): ID of the invoice that will be searched.
        
        Returns:
            data: Invoice detail
        """
        url = f"/v3/outlets/{outlet_id}/invoices/{invoice_id}"
        body = {
            "invoice_id": invoice_id,
        }
        response = _APIRequestor.get(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=InvoiceData, data=response.body['data'])
        else:
            raise MokaError(response)
        


