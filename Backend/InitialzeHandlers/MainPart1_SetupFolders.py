from AppSettings.AppSettings import *;

class Setup:
    
    """
    Build the folder structure if applicable.
    """
    @classmethod
    def MainPart1_Directories(cls):
        allPaths = {DATAFOLDER, IMAGESFOLDER, INCOMINGFOLDER, CHECKEDFOLDER, PROCESSEDFOLDER, TRAINEDMODEL}
        print("Main directory given: " + ROOTPATH);
        print("Checking DataFolder Structure...")
        FH_C.CheckDirectoryCollectionIntegrity(allPaths);
        print("DataFolder Checking complete.")
        
    """
    Build the start
    """
    @classmethod
    def MainPart2_TestDatabaseConnection(cls):
        testUserName = "ReadonlyUsers";
        testUserPassword = "123321Pl@nt";
        directDatabase = "PlantenZiektenHerkenner";
        testQuery_1 = "INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate) ";
        testQuery_2 = "VALUES('test', 'test', 'jpg', 0, 'test', GetDate())";
        testQuery_Full = testQuery_1 + testQuery_2;
        testReadQuery_Full = "SELECT * from dbo.UploadedImages";
        #query = "INSERT INTO dbo.checks (moment_of_check, healthy, plant_disease) VALUES (?, ?, ?)"
        #params = (checksModel.momentOfCheck, checksModel.healthy, checksModel.plant_disease)
        """
        The tests are divided up into 2 users by 3 checks
        check 1: Is the user connected?
        check 2: Is the user allowed to read results?
        check 3: Is the user allowed to insert data?
        Admin should pass all 3, readonly user just the first 2.
        These are self contained tests, close when done.
        """
        from Handler.DatabaseHandler import DatabaseConnector as DB_C;
        connection_Class = DB_C(); 
        print("");    
        # Test user - Readonly
        connectionSuccess = connection_Class.connect_test(testUserName, testUserPassword, directDatabase);
        if(connectionSuccess == False):
            raise Exception("Failed to get a database connection");
        if connection_Class.executeQuery(testReadQuery_Full) == False:
            raise Exception("Failed to get proper results, check the test user");
        if connection_Class.executeQuery(testQuery_Full) == True:
            raise Exception("Readonly user holds to many rights, breaking off test.");
        connection_Class.close();
        # Test user - admin
        connectionSuccess = connection_Class.connect();
        if(connectionSuccess == False):
            raise Exception("Failed to get a database connection");
        if connection_Class.executeQuery(testReadQuery_Full) == False:
            raise Exception("Failed to get proper results, check the test user");
        if connection_Class.executeQuery(testQuery_Full) == True:
            raise Exception("Readonly user holds to many rights, breaking off test.");
        connection_Class.close();
    

        
    """
    Build the start
    """
    @classmethod
    def MainPart3_TrainModel(cls):
        print("");
        # If no model is detected, create it.
        # Set to use it afterwards
    
        
    
