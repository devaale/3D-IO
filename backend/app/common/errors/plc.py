class PlcError(Exception):
    def __init__(self, message):
        self.message = "Plc error has occurred: " + message
        super().__init__(self.message)