# Overview
![](static/images/dog-cat-190709-800x450.jpg)

In this project,I'll write an algorithm whether to classify images contain either a dog or a cat.This is easy for humans,dogs and cats.Your computer will find a bit more difficult.

- Deep Blue beat Kasparov at chess in 1997
- Watson beat the brightest trivia minds at Jeopardy in 2011
- Can you tell Fido from Mittens in 2013 ?

# The Asirra data set
Web services are often protected with a challenge that's supposed to be easy for people to solve,but difficult for computers.Such a challenge is often called a [CAPTCHA](http://www.captcha.net/) (Completely Automated Public Turing test to tell Computers and Humans Apart) or HIP (Human Interactive Proof).HIPs are used for many purposes,such as to reduce email and blog spam and prevent brute-force attacks on web site passwords.

Asirra (Animal Species Image Recognition for Restricting Access) is a HIP that works by asking users to identify photographs of cats and dogs.This task is difficult for computers,but studies have shown that people can accomplish it quickly and accurately.Many even think it's fun! Here is an example of the Asirra interface:

Asirra is unique because of its partnership with [petfinder.com](https://www.petfinder.com/),the world's largest site devoted to finding homes for homeless pets.They've provided Microsoft Research with over three million images of cats and dogs,manually classified by people at thousands of animal shelters across the United States.Kaggle is fortunate to offer a subset of this data for fun and research

# Data
![](static/images/woof_meow.jpg)

The training archive contains 25,000 images of dogs and cats.

Download dataset [here](https://www.kaggle.com/c/dogs-vs-cats/data)

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