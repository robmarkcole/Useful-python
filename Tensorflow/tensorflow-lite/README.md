## TFlite
* Tflite is an alternative lightweight tf interpreter that requires optimised models, read -> https://www.tensorflow.org/lite/guide
* Basically targetted at Android & iOS, but also [runs on Mac, Windows, linux](https://www.tensorflow.org/lite/guide/inference#supported_platforms)
* [Comparison of TF, TF Lite, and TF Lite quant models](https://medium.com/towards-artificial-intelligence/testing-tensorflow-lite-image-classification-model-e9c0100d8de3)
* [Example project showing how we can compare TensorFlow and TensorFlow Lite models](https://github.com/frogermcs/TFLite-Tester)

## Models
* List of pretrained tflite models (notably no face recognition) -> https://www.tensorflow.org/lite/models
* Facenet (face recognition) -> https://github.com/Kao1126/EdgeTPU-FaceNet

## Pi
* Python guide (runs `label_image.py`, successfully tested on pi3, also on Mac on 6 Oct 2019) ->  https://www.tensorflow.org/lite/guide/python
* Example using picamera (successfully tested on pi3 on 6 Oct 2019) -> https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi
* Object detection -> https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/TFLite_detection_webcam.py

## EdgeTPU
* https://blogs.sap.com/2020/02/11/containerizing-a-tensorflow-lite-edge-tpu-ml-application-with-hardware-access-on-raspbian/

## Microcontrollers
* https://www.tensorflow.org/lite/microcontrollers/overview
* https://learn.adafruit.com/tensorflow-lite-for-microcontrollers-kit-quickstart