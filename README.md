# Overview
![](static/images/dog-cat-190709-800x450.jpg)

# Flask app
- Donwload file model_vgg.h5 at [](https://drive.google.com/drive/u/0/folders/1ApKK64-dpqGmLmJRHg4Orjszj1E92UQ6)
- Move file to static/model_vgg.h5
- install virtual environment by command `pip install -r requirements.txt`
- run app by command `python main.py`
- if you would like to capture wrong predictions,please create your own database by replace where necessary in `dinh.py` and also in `blueprints\retrain\blueprint.py`