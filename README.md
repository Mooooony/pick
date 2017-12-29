# pick
This implementation of U-net([U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/)) is originnally realized by [zhixuhao](https://github.com/zhixuhao/un).
## Data
Data stored in data directory is processed by ```data.py``` script. This script just loads images and saves them into npydata directory as Numpy binary format file.
## Train
run ``` python train.py --epoch n ```. "n" is the number of epochs.
## Predict
```predict.py``` loads test data and makes prediction on them. The result is stored in ```results``` directory.  
