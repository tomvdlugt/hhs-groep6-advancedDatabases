"""
simple model
originalName: original full name of the file
uuidName: given uuid to the file
extension: seperated extension to the file
healthy: 0 = unprocessed, 1 = healthy, 2 = not healthy, 3 intended to be unidentified, but not yet implemented
"""
import datetime
class NewImageModel:
    def __init__(self, originalName: str, uuidName: str, extension: str, healthy: int, plant_disease: str, uploadDate: datetime= None):
        self.originalName = originalName;
        self.uuidName = uuidName;
        self.extension = extension;
        self.healthy = healthy;
        self.plant_disease = plant_disease;
        if(uploadDate != None): # is a nullable value, chosing not to get it will not return it.
            self.uploadDate = uploadDate;

class ProcessedModel:
    def __init__(self, originalName: str, uuidName: str, extension: str, healthy: int, plant_disease: str, uploadDate: datetime, processedDate: datetime):
        self.originalName = originalName;
        self.uuidName = uuidName;
        self.extension = extension;
        self.healthy = healthy;
        self.plant_disease = plant_disease;
        self.uploadDate = uploadDate;
        self.processedDate = processedDate; # not nullable in this model, either its new, or its never there to begin with!
