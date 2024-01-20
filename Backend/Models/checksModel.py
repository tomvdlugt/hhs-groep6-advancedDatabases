import datetime

class ChecksModel:
    def __init__(self, momentOfCheck: datetime, healthy: bool):
        self.momentOfCheck = momentOfCheck
        self.healthy = healthy
