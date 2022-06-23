class MokaResponse:
    """Response that will be returned by the API Server."""

    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"{self.status_code} {self.headers} {self.body}"