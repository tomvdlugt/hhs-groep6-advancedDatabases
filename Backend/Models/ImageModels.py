allowedExtensions = {"jpg","png"}

class UploadedFileRules:
    def __init__(self):
        self.allowedFileTypes = allowedExtensions;

## simple model
# originalName: orignal full name of the file
# uuidName: given uuid to the file
# extension: seperated extension to the file
# healthy: 0 = unprocessed, 1 = healthy, 2 = not healthy, 3 intended to be unidentified, but not yet implemented
# 
class NewImageModel:
    def __init__(self, originalName: str, uuidName: str, extension: str, healthy: int, giventime = None):
        self.originalName = originalName;
        self.uuidName = uuidName;
        self.extension = extension;
        self.healthy = healthy;
        if(giventime != None):
            self.giventime = giventime;

class ProcessedModel:
    def __init__(self, originalName: str, uuidName: str, extension: str, healthy: int):
        self.originalName = originalName;
        self.uuidName = uuidName;
        self.extension = extension;
        self.healthy = healthy;