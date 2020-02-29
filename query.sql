# Create table to contain wrong predicton images
CREATE TABLE retrain (
    id SERIAL PRIMARY KEY,
    wrong_label TEXT,
    image_path TEXT
);

# Query to save to database
query = f"INSERT INTO retrain (wrong_label,image_path) VALUES (%s,%s);"
val = (label,image_path)

# Alter data type of column
ALTER TABLE retrain 
ALTER COLUMN base64_image VARCHAR;

# connect database 
psql mariana postgres

# Drop table retrain
DROP TABLE retrain ;