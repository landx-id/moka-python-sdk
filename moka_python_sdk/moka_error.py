class MokaError(Exception):
    """Error that will be given when status code != 200."""

    def __init__(self, response):
        super(MokaError, self).__init__(response.body["meta"]["error_message"])

        meta = response.body["meta"]
        self.status_code = meta["code"]
        self.error_code = meta["error_type"]
        self.title = meta["error_message"]
