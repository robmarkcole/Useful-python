# Image annotation
* For object detection main formats are Pascal VOC (Imagenet, XML files, saves absolute file path) and Yolo (txt files)
* The XML and images then typically need to be converted to another format for using in training, e.g. TFRecords

## Labelme
* https://github.com/wkentaro/labelme
* GUI for annotating images and exporting, easy to use
* Installed from source (`pip  install -e .`) in a venv, dont forget to `make qt5py3` before `python3 labelImg.py`
* [Tutorial for single image](https://github.com/wkentaro/labelme/tree/master/examples/tutorial)
* http://emaraic.com/blog/yolov3-custom-object-detector
* https://hackernoon.com/object-detection-in-google-colab-with-custom-dataset-5a7bb2b0e97e
* https://github.com/TannerGilbert/Tensorflow-Object-Detection-API-Train-Model

## Alternative annotation tools
* Also checkout https://rectlabel.com/ -> 1 month free trial then 3 pounds per month
* Browser annotation -> https://supervise.ly/ (managed) and https://imglab.in/ (open source)
* https://labelbox.com/
* https://labelstud.io/
* https://roboflow.ai
* https://github.com/Microsoft/VoTT (looks good)
* https://github.com/l3p-cv/lost (open source - got some docker error :-/ )
* https://github.com/opencv/cvat -> by openCV, looks well maintained and has rest API
* https://github.com/SkalskiP/make-sense -> open source, browser based