# Overview
![](static/images/classify_dog_1.jpg)

# Flask app
- Donwload file model_vgg.h5 at [](https://drive.google.com/open?id=1bubWtVp_2M9FtsJQ55cZficgKnWRsxEX)
- Move file to static/model_vgg.h5
- install virtual environment by command `pip install -r requirements.txt`
- run app by command `python main.py`
- if you would like to capture wrong predictions,please create your own database by replace where necessary in `dinh.py` and also in `blueprints\retrain\blueprint.py`