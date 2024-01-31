allowedExtensions = {"jpg","png"}

Create TABLE UploadedImages (
imageId int IDENTITY(1,1) PRIMARY KEY, originalName varchar(255), uuidName  varchar(255), extension varchar(10), 
healthy int, plant_disease  varchar(255), uploadDate  datetime,  processedDate  datetime null);
-- create new image

INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate, processedDate) 
VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 1, 'Blight_Early', GetDate());