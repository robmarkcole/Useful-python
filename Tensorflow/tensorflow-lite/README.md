## TFlite
* Tflite is an alternative interpreter that requires optimised models, read -> https://www.tensorflow.org/lite/guide
* [Runs on linux, Android or iOS](https://www.tensorflow.org/lite/guide/inference#supported_platforms)
* To quickly start executing TensorFlow Lite models with Python, you can install just the TensorFlow Lite interpreter, instead of all TensorFlow packages. This interpreter-only package is a fraction the size of the full TensorFlow package and includes the bare minimum code required to run inferences with TensorFlow Lite
* Examples -> https://github.com/tensorflow/examples/tree/master/lite
* [Comparison of TF, TF Lite, and TF Lite quant models](https://medium.com/towards-artificial-intelligence/testing-tensorflow-lite-image-classification-model-e9c0100d8de3)
* [Example project showing how we can compare TensorFlow and TensorFlow Lite models](https://github.com/frogermcs/TFLite-Tester)

## Models
* List of pretrained tflite models -> https://www.tensorflow.org/lite/models
* Facenet (face recognition) -> https://github.com/Kao1126/EdgeTPU-FaceNet

## Pi
* Python guide (runs `label_image.py`, successfully tested on pi3, also on Mac on 6 Oct 2019) ->  https://www.tensorflow.org/lite/guide/python
* Example using picamera (successfully tested on pi3 on 6 Oct 2019) -> https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi
* Object detection -> https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/TFLite_detection_webcam.py

## Microcontrollers
* https://www.tensorflow.org/lite/microcontrollers/overview
* https://learn.adafruit.com/tensorflow-lite-for-microcontrollers-kit-quickstart