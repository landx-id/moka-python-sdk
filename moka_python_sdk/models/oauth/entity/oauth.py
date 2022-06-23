from dataclasses import dataclass

@dataclass
class OAuthEntity:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    created_at: int
