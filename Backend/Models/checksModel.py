from datetime import datetime

class ChecksModel:
    def __init__(self, healthy: bool, plant_disease: int):
        self.momentOfCheck = datetime.now()
        self.healthy = healthy
        self.plant_disease = plant_disease
