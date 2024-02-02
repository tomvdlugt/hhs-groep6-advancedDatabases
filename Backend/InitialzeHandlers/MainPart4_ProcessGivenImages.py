from Handler.FileHandler import FileHandler as FileHandler_Class; ## required to parse out proper directory
from Models.ImageModels import NewImageModel, ALLOWEDEXTENSIONS, ALLOWEDBACKENDEXTENSIONS, INCOMINGFOLDER, CHECKEDFOLDER, PROCESSEDFOLDER

class ProcessImages:
    @classmethod
    def MainPart4_Method_CheckIncoming(cls):
        # Import necessary libraries
        incomingFileDirectory = INCOMINGFOLDER;
        # give incoming files in an array
        filesIncoming = FileHandler_Class.GetAllFilesInDirectory(INCOMINGFOLDER);

        for arrayFileInstance in filesIncoming:
            fileAccepted = False;
            for givenExtension in ALLOWEDEXTENSIONS:
               if(arrayFileInstance[arrayFileInstance.find("."):].lower().replace(".","") == givenExtension):
                  fileAccepted = True;
                  break;

            if not fileAccepted:
               print("Possible malicious filetype detected, breaking off run to protect the system.");
               FileHandler_Class.RemoveFile(incomingFileDirectory+arrayFileInstance)
               raise Exception(f"Given file for the model is not allowed, removed the file prematurely. Filename that was given: {arrayFileInstance}");
        # Checking complete
        # Checking files complete, proceed to connect to the Database 
        from databaseConnector import DatabaseConnector;
        from DAO.checkDao import ChecksDao
        connection_Class = DatabaseConnector(); 
        connection_Class.connect();
        checksDao_Class = ChecksDao(connection_Class)
        print("")
        print("Before processing the files");
        print("");
        connection_Class.executeReadQuery("select * from dbo.UploadedImages");
        print("");
        # Process the new files    
        #stap 3
        for arrayFileInstance in filesIncoming:
            newImageModel = FileHandler_Class.MoveIncommingToChecked(arrayFileInstance, INCOMINGFOLDER, CHECKEDFOLDER);
            insertIntoImages = f"INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate)";
            insertIntoImages = f"{insertIntoImages}VALUES('{newImageModel.originalName}','{newImageModel.uuidName}',";
            insertIntoImages = f"{insertIntoImages}'{newImageModel.extension}','{newImageModel.healthy}',";
            insertIntoImages = f"{insertIntoImages}'{newImageModel.plant_disease}',GetDate())";
            connection_Class.executeQuery(insertIntoImages);
    

        print("")
        print("Before processing the files");
        print("");
        connection_Class.executeReadQuery("select * from dbo.UploadedImages");
        print("");

        import tensorflow as tf
        # load mainpart 3 = trained model
        # load image model
        
