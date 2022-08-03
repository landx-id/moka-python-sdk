from dataclasses import asdict
from moka_python_sdk._api_requestor import _APIRequestor
from moka_python_sdk.moka_error import MokaError
from moka_python_sdk.models._to_model import _to_model
from typing import List

from .entity.oauth import OAuthEntity

class OAuth:
    @staticmethod
    def exchange_token(
        *,
        grant_type: str,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
        refresh_token: str,
        **kwargs
    ) -> OAuthEntity:
        """Send POST Request to Exchange token.
        (API Reference : https://api.mokapos.com/docs#operation/exchangeToken)

        Args:
            - grant_type (str): Grant type {authorization_code, refresh_token}
            - client_id (str): Client ID
            - client_secret (str): Client Secret
            - code (str): Code
            - redirect_uri (str): Redirect URI
            - refresh_token (str): Refresh Token
                
        Returns:
            data: OAuth Entity
        """
        url = "/oauth/token"
        body = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "redirect_uri": redirect_uri,
            "refresh_token": refresh_token,
        }
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return _to_model(model=OAuthEntity, data=response.body)
        else:
            raise MokaError(response)
    
    @staticmethod
    def get_access_token(
        *,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
        **kwargs
    ) -> OAuthEntity:
        """Send POST Request to Get access token.
        (API Reference : https://api.mokapos.com/docs#operation/exchangeToken)

        Args:
            - client_id (str): Client ID
            - client_secret (str): Client Secret
            - refresh_token (str): Refresh Token

        Returns:
            data: OAuth Entity
        """
        return OAuth.exchange_token(
            grant_type="authorization_code",
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=None,
            **kwargs
        )
    
    @staticmethod
    def refresh_token(
        *,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        **kwargs
    ) -> OAuthEntity:
        """Send POST Request to Refresh token.
        (API Reference : https://api.mokapos.com/docs#operation/exchangeToken)

        Args:
            - client_id (str): Client ID
            - client_secret (str): Client Secret
            - refresh_token (str): Refresh Token
                
            Returns:
                data: OAuth Entity
        """
        return OAuth.exchange_token(
            grant_type="refresh_token", 
            client_id=client_id, 
            client_secret=client_secret, 
            refresh_token=refresh_token, 
            code=None,
            redirect_uri=None,
            **kwargs
        )
    
    @staticmethod
    def revoke_token(
        *,
        client_id: str,
        client_secret: str,
        token: str,
        **kwargs
    ) -> bool:
        """Send POST Request to Revoke token.
        (API Reference : https://api.mokapos.com/docs#operation/revokeToken)

        Args:
            - client_id (str): Client ID
            - client_secret (str): Client Secret
            - token (str): Token
                
        Returns:
            data: None
        """
        url = "/oauth/revoke"
        body = {
            "client_id": client_id,
            "client_secret": client_secret,
            "token": token,
        }
        response = _APIRequestor.post(url, body=body, **kwargs)
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            raise MokaError(response)
