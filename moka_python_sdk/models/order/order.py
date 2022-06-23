from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from models._to_model import _to_model

from .entity.order_status import OrderStatusEntity
from .entity.order import OrderEntity
from .entity.driver import DriverEntity
from .entity.sales_type import SalesTypeEntity
from .entity.auto_accept import AutoAcceptEntity

class Order:
    @staticmethod
    def get(*, outlet_id: str, application_id: str, **kwargs) -> list[OrderStatusEntity]:
        """Send GET Request to Get status of specific order.
        (API Reference : https://api.mokapos.com/docs#operation/getOrderStatusV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - application_order_id (str): ID of the order that will be searched.

        Returns:
            data: Array status of order
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/orders/{application_id}/status"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=OrderEntity, data=response.body)
        else:
            raise MokaError(response)
    
    @staticmethod
    def create(**kwargs):
        """Send POST Request to Create a new order.
        (API Reference : https://api.mokapos.com/docs#operation/createOrderV1)

        Path Parameters:
            - outlet_id (str): ID of the outlet that will be searched.
        
        Args:
            - customer_name (str): Name of the customer.
            - customer_phone_number (str): Phone number of the customer.
            - sales_type_id (int): ID of the sales type.
            - sales_type_name (str): Name of the sales type.
            - client_created_at (str): Date and time of the order.
            - application_order_id (str): ID of the order.
            - payment_type (str): Payment type of the order.
            - note (str): Note of the order.
            - complete_order_notification_url (str): URL of the complete order notification.
            - accept_order_notification_url (str): URL of the accept order notification.
            - cancel_order_notification_url (str): URL of the cancel order notification.
            - assign_expedition_notification_url (str): URL of the assign expedition notification.
            - discount_id (int): ID of the discount.
            - discount_type (str): Type of the discount.
            - discount_amount (str): Amount of the discount.
            - discount_guid (str): GUID of the discount.
            - discount_name (str): Name of the discount.
            - order_items (list): List of order items.
                - item_id (int): ID of the item.
                - item_name (str): Name of the item.
                - quantity (int): Quantity of the item.
                - item_variant_id (int): ID of the item variant.
                - item_variant_name (str): Name of the item variant.
                - note (str): Note of the item.
                - item_price_library (int): Price of the item.
                - category_id (int): ID of the category.
                - category_name (str): Name of the category.
                - item_discount_id (int): ID of the item discount.
                - item_discount_type (str): Type of the item discount.
                - item_discount_amount (str): Amount of the item discount.
                - item_discount_guid (str): GUID of the item discount.
                - item_discount_name (str): Name of the item discount.
                - item_modifiers (list): List of item modifiers.
                    - item_modifier_id (int): ID of the item modifier.
                    - item_modifier_name (str): Name of the item modifier.
                    - item_modifier_option_id (int): ID of the item modifier option.
                    - item_modifier_option_name (str): Name of the item modifier option.
                    - item_modifier_option_price (int): Price of the item modifier option.
        
        Returns:
            data: ID of the order
        """
        url = f"/v1/outlets/{kwargs['outlet_id']}/advanced_orderings/orders"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=OrderEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def cancel(*, outlet_id: str, application_order_id: str, **kwargs) -> OrderEntity:
        """Send POST Request to Cancel an order.
        (API Reference : https://api.mokapos.com/docs#operation/cancelOrderV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - application_order_id (str): ID of the order that will be searched.
            - cancel_reason (str): Reason of the cancel.

        Returns:
            data: ID of the order
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/orders/{application_order_id}/cancel"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=OrderEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def generate_sales_type(outlet_id: str, **kwargs) -> SalesTypeEntity:
        """Send POST Request to Generate a sales type.
        (API Reference : https://api.mokapos.com/docs#operation/generateSalesTypeV2)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
        
        Returns:
            data: Sales type
        """
        url = f"/v2/outlets/{outlet_id}/advanced_orderings/generate_sales_type"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=SalesTypeEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def get_auto_accept(outlet_id: str, **kwargs) -> AutoAcceptEntity:
        """Send GET Request to Get auto accept.
        (API Reference : https://api.mokapos.com/docs#operation/getAutoAcceptV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.

        Returns:
            data: Auto accept
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/auto_accept"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=AutoAcceptEntity, data=response.body)
        else:
            raise MokaError(response)
    
    @staticmethod
    def set_auto_accept(*, outlet_id: str, status: bool, **kwargs) -> AutoAcceptEntity:
        """Send POST Request to Set auto accept.
        (API Reference : https://api.mokapos.com/docs#operation/setAutoAcceptV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - status (bool): Status of the auto accept.

        Returns:
            data: Auto accept
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/auto_accept"
        response = _APIRequestor.post(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=AutoAcceptEntity, data=response.body)
        else:
            raise MokaError(response)

    @staticmethod
    def update_order_driver(
        *,
        outlet_id: str,
        application_order_id: str,
        driver_name: str,
        driver_license_plate: str,
        driver_phone_number: str,
        **kwargs
    ) -> DriverEntity:
        """Send POST Request to Update order driver.
        (API Reference : https://api.mokapos.com/docs#operation/updateOrderDriverV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - application_order_id (str): ID of the order that will be searched.
            - driver_name (str): Name of the driver.
            - driver_license_plate (str): License plate of the driver.
            - driver_phone_number (str): Phone number of the driver.

        Returns:
            data: ID of the order
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/orders/{application_order_id}/drivers"
        data = {
            "name": driver_name,
            "license_plate": driver_license_plate,
            "phone_number": driver_phone_number
        }
        response = _APIRequestor.post(url, body=data, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=DriverEntity, data=response.body)
        else:
            raise MokaError(response)


