# Overview
![](static/images/dog-cat-190709-800x450.jpg)

# Modeling
we use VGG16

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
vgg16 (Model)                (None, 6, 6, 512)         14714688  
_________________________________________________________________
global_average_pooling2d (Gl (None, 512)               0         
_________________________________________________________________
dense (Dense)                (None, 1)                 513       
=================================================================
Total params: 14,715,201
Trainable params: 513
Non-trainable params: 14,714,688
```

- Epochs : 5
- Train accuracy : 87%
- Validation accuracy : 89%

# Flask app
- Donwload file model_vgg.h5 [here](https://drive.google.com/file/d/1bubWtVp_2M9FtsJQ55cZficgKnWRsxEX/view?usp=sharing)
- Move file to static/model_vgg.h5
- install virtual environment by command `pip install -r requirements.txt`
- run app by command `python main.py`
- if you would like to capture wrong predictions,please create your own database by replace where necessary in `dinh.py` and also in `blueprints\retrain\blueprint.py`