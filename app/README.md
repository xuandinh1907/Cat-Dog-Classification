# Introduction

# Project structure

## Creating skeleton
```
mkdir app app/templates app/static app/static/images app/blueprints app/middlewares app/uploads
touch app/main.py app/dinh.py app/query.sql  app/static/script.js app/static/styles.css
touch app/blueprints/__init__.py
```
## Build a new blueprint
In this project blueprint name will be home , classify and retrain
```
export NEW_BLUEPRINT=retrain
mkdir app/blueprints/$NEW_BLUEPRINT 
touch app/blueprints/$NEW_BLUEPRINT/__init__.py app/blueprints/$NEW_BLUEPRINT/blueprint.py
echo "from .$NEW_BLUEPRINT import $NEW_BLUEPRINT" >> app/blueprints/__init__.py
echo "from .blueprint import $NEW_BLUEPRINT" > app/blueprints/$NEW_BLUEPRINT/__init__.py
printf \
"from flask import Blueprint, render_template, request\n\
\n\
$NEW_BLUEPRINT = Blueprint('$NEW_BLUEPRINT', __name__)\
\n\
@$NEW_BLUEPRINT.route('/route_name')\n\
def route_name():\n\
    return render_template('$NEW_BLUEPRINT.html') \n\
" > app/blueprints/$NEW_BLUEPRINT/blueprint.py
touch app/templates/$NEW_BLUEPRINT.html
```
## app/static
**Here we put our model with format file h5 , script.js , styles.css**

## app/templates
**Here we put classify.html , home.html , retrain.html**

## app/query.sql
**Here we store some sql queries because of convenience**

## app/uploads
**Here we store uploaded images whose names is edited uniquely**

## app/main.py
**For register blueprints and display image again in classify.html**
```
from flask import Flask, render_template , send_from_directory
from blueprints import *

app.register_blueprint(home_page)
app.register_blueprint(classify)
app.register_blueprint(home_page)

@app.route('/classify/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
```

## app/dinh.py
**For checking if the wrong is saved to db yet**
```
import requests
import psycopg2


conn = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
cur = conn.cursor()

query = f"SELECT * FROM retrain;"

cur.execute(query)

data = cur.fetchall()[-1]

wrong_label = data[1]

image_path = data[2]

print(wrong_label,image_path,sep='\n')

conn.close()
```

## app/static/script.js
```
var file = document.getElementById("image");

file.onchange = function(){
    if(file.files.length > 0)
    {
      document.getElementById('file-name').innerHTML = file.files[0].name;
    }
};
```

## app/blueprints/retrain/blueprint.py
**For getting the wrong label and the path and sending them to db**
```
from flask import Blueprint, render_template, request
import requests
import psycopg2

retrain = Blueprint('retrain', __name__)

@retrain.route('/retrain',methods=['POST','GET'])
def wrong_cases():
    label = request.form["label"]
    image_path = request.form["path"]
    
    conn = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
    cur = conn.cursor()

    query = f"INSERT INTO retrain (wrong_label,image_path) VALUES (%s,%s);"
    val = (label,image_path)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return render_template('retrain.html') 
```
## app/blueprints/classify/blueprint.py

### Import library and define necessary directories

### Load model

### Preprocess an image

### Predict & classify image

### create a random string for file name to make sure uniqe property

```
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
```

### Main part of classify and save some important variables to prepare for next step

classify = Blueprint('classify', __name__)

@classify.route('/classify', methods=['POST'])
def upload_file():

    file = request.files["image"]
    file.filename = randomString() + '.jpg'
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    print(upload_image_path)
    file.save(upload_image_path)

    label, prob = prediction(model, upload_image_path)

    prob = round((prob[0][0] * 100), 2)

    return render_template('classify.html', image_file_name = file.filename, label = label, prob = prob, path = upload_image_path)
```
