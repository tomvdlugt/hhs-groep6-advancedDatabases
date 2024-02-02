
-- Insert new image
INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate) 
VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 1, 'Blight_Early', GetDate());

-- insert processed image
INSERT INTO UploadedImages (originalName, uuidName, extension, healthy, plant_disease, uploadDate, processedDate) 
VALUES ('TestImage.jpg', 'banaanuid', 'jpg', 1, 'Blight_Early', uploadDate, GetDate());