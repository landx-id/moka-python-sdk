class MokaError(Exception):
    """Error that will be given when status code != 200."""

    def __init__(self, response):
        super(MokaError, self).__init__(response.body["errors"][0]["detail"])

        error = response.body["errors"][0]
        self.status_code = response.status_code
        self.error_code = error["code"]
        self.title = error["title"]
        self.errors = response.body.get("errors", None)
