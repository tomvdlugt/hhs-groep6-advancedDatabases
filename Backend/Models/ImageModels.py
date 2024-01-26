allowedExtensions = {"jpg","png"}

class UploadedFileRules:
    def __init__(self):
        self.allowedFileTypes = allowedExtensions;

class NewImageModel:
    def __init__(self, originalName, uuidName, extension):
        self.originalName = originalName;
        self.healthy = uuidName;
        self.extension = extension;
