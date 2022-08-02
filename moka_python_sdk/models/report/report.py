from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.report import (
    CategorySalesEntity, CollectorSalesEntity, ModifierSalesEntity,
    DiscountSalesEntity, TaxSalesEntity, GratuitySalesEntity,
    ServerSalesEntity, ItemSalesEntity, SalesSummaryEntity,
    PaymentMethodsEntity
)

class Report:
    @staticmethod
    def show_category_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> CategorySalesEntity:
        """Send GET Request to Show category sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#tag/Category-Sales)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Category data
        """
        url = f"/v2/outlets/{outlet_id}/reports/category_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=CategorySalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def get_collector_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> CollectorSalesEntity:
        """Send GET Request to Show collector sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showCollectorSalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Collector data
        """
        url = f"/v2/outlets/{outlet_id}/reports/collector_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=CollectorSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_modifier_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> ModifierSalesEntity:
        """Send GET Request to Show modifier sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showModifierSalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Modifier data
        """
        url = f"/v2/outlets/{outlet_id}/reports/modifier_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=ModifierSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_discount_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> DiscountSalesEntity:
        """Send GET Request to Show discount sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showDiscountSalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Discount data
        """
        url = f"/v2/outlets/{outlet_id}/reports/discount_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=DiscountSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def show_tax_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> TaxSalesEntity:
        """Send GET Request to Show tax sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showTaxSalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Tax data
        """
        url = f"/v2/outlets/{outlet_id}/reports/tax_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=TaxSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def show_gratuity_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> GratuitySalesEntity:
        """Send GET Request to Show gratuity sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showGratuitySalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Gratuity data
        """
        url = f"/v2/outlets/{outlet_id}/reports/gratuity_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=GratuitySalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
        
    @staticmethod
    def show_server_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> ServerSalesEntity:
        """Send GET Request to Show server sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showServerSalesV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Server data
        """
        url = f"/v2/outlets/{outlet_id}/reports/server_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=ServerSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def show_item_sales(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> ItemSalesEntity:
        """Send GET Request to Get Show item sales for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showItemSalesV3)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Item data
        """
        url = f"/v3/outlets/{outlet_id}/reports/item_sales"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=ItemSalesEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def show_sales_summary(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> SalesSummaryEntity:
        """Send GET Request to Show sales summary for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showSalesSummaryV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Sales summary data
        """
        url = f"/v2/outlets/{outlet_id}/reports/sales_summary"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SalesSummaryEntity, data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def show_payment_methods(
        *,
        outlet_id: int,
        per_page: int,
        start: float = None,
        end: float = None,
        **kwargs
    ) -> PaymentMethodsEntity:
        """Send GET Request to Show payment methods for selected date range on the selected outlet.
        (API Reference : https://api.mokapos.com/docs#operation/showPaymentMethodsV2)

        Args:
            - outlet_id (int): ID of the outlet that will be searched.
            - per_page (int): Number of elements per page.
            - start (float): Start date in DD/MM/YYYY format
            - end (float): End date in DD/MM/YYYY format

        Returns:
            data: Payment methods data
        """
        url = f"/v2/outlets/{outlet_id}/reports/payment_methods"

        params = {
            "per_page": per_page,
            "start": start,
            "end": end,
        }
        response = _APIRequestor.get(url, params=params, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=PaymentMethodsEntity, data=response.body['data'])
        else:
            raise MokaError(response)