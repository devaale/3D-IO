class DetectionError(Exception):
    def __init__(self, message):
        self.message = "Detection error has occurred: " + message
        super().__init__(self.message)
