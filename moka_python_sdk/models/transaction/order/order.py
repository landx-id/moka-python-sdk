from dataclasses import asdict
from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List


from .entity.order_status import OrderStatusEntity
from .entity.order import OrderEntity, OrderId
from .entity.driver import DriverEntity
from .entity.sales_type import SalesTypeEntity
from .entity.auto_accept import AutoAcceptEntity

class Order:
    @staticmethod
    def get_status(
        *,
        outlet_id: int,
        application_order_id: str,
        **kwargs
    ) -> List[OrderStatusEntity]:
        """Send GET Request to Get status of specific order.
        (API Reference : https://api.mokapos.com/docs#operation/getOrderStatusV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - application_order_id (str): ID of the order that will be searched.

        Returns:
            data: Array status of order
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/orders/{application_order_id}/status"
        response = _APIRequestor.get(url, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[OrderStatusEntity], data=response.body['data'])
        else:
            raise MokaError(response)
    
    @staticmethod
    def create(
        *,
        outlet_id: str,
        order_entity: OrderEntity,
        **kwargs
    ) -> List[OrderId]:
        
        """Send POST Request to Create a new order.
        (API Reference : https://api.mokapos.com/docs#operation/createOrderV1)

        Args:
            - outlet_id (str): ID of the outlet that will be searched.
            - order_entity (OrderEntity): Order Entity
        
        Returns:
            data: ID of the order
        """
        url = f"/v1/outlets/{outlet_id}/advanced_orderings/orders"
        body = asdict(order_entity)
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[OrderId], data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def cancel(
        *,
        outlet_id: str,
        application_order_id: str,
        cancel_reason: str,
        **kwargs
    ) -> List[OrderId]:
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
        body = {
            "cancel_reason": cancel_reason
        }
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=List[OrderId], data=response.body['data'])
        else:
            raise MokaError(response)

    @staticmethod
    def generate_sales_type(outlet_id: str, **kwargs) -> List[SalesTypeEntity]:
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
            return _to_model(model=List[SalesTypeEntity], data=response.body['data'])
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
            return _to_model(model=AutoAcceptEntity, data=response.body['data'])
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
        body = {
            "auto_accept_status": status
        }
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=AutoAcceptEntity, data=response.body['data'])
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
        body = {
            "name": driver_name,
            "license_plate": driver_license_plate,
            "phone_number": driver_phone_number
        }
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=DriverEntity, data=response.body['data'])
        else:
            raise MokaError(response)


