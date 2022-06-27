class ProcessingError(Exception):
    def __init__(self, message):
        self.message = "Processing error has occurred: " + message
        super().__init__(self.message)
