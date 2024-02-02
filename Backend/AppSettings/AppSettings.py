from Handler.FileHandler import FileHandler as FH_C; ## required to parse out proper directory
ALLOWEDEXTENSIONS = {"jpg","png"}
ALLOWEDBACKENDEXTENSIONS = {"jpg","png", "h5"}
ROOTPATH = FH_C.GetProjectRoot();
DATAFOLDER = ROOTPATH + FH_C.ParseDirectoryPath("/Data");
IMAGESFOLDER = DATAFOLDER + FH_C.ParseDirectoryPath("/Images");
TRAINEDMODEL = DATAFOLDER + FH_C.ParseDirectoryPath("/TrainedModel");
INCOMINGFOLDER =  IMAGESFOLDER + FH_C.ParseDirectoryPath("/Incoming");
CHECKEDFOLDER = IMAGESFOLDER + FH_C.ParseDirectoryPath("\\Checked");
PROCESSEDFOLDER = IMAGESFOLDER + FH_C.ParseDirectoryPath("/Processed");
