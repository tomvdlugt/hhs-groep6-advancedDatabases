allowedExtensions = {"jpg","png"}

Create TABLE Images
(
    imageId int IDENTITY(1,1) PRIMARY KEY,
    originalName varchar(255) ,
    uuidName  varchar(255),
    extension varchar(10),
    disease  varchar(255),
    uploadDate  datetime,
    processedDate  datetime null
);
-- create new image
INSERT INTO customer (originalName, uuidName, extension, disease, uploadDate, processedDate) 
VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 'Blight_Early', GetDate());