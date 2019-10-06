## TFlite
* Tflite is an alternative interpreter that requires optimised models, read -> https://www.tensorflow.org/lite/guide
* To quickly start executing TensorFlow Lite models with Python, you can install just the TensorFlow Lite interpreter, instead of all TensorFlow packages. This interpreter-only package is a fraction the size of the full TensorFlow package and includes the bare minimum code required to run inferences with TensorFlow Lite

## Models
* List of pretrained tflite models -> https://www.tensorflow.org/lite/models

## Pi

* Benchmarking script (`label_image.py `) -> https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/examples/python/
* Example using picamera -> https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi

* Following https://www.tensorflow.org/lite/guide/python on pi4 I hit:
```
pi@pi-4:~/tflite $ python3 label_image.py   --model_file /tmp/mobilenet_v1_1.0_224.tflite   --label_file /tmp/labels.txt   --image /tmp/grace_hopper.bmp
Traceback (most recent call last):
  File "label_image.py", line 27, in <module>
    from tflite_runtime import Interpreter
ImportError: cannot import name 'Interpreter' from 'tflite_runtime' (/home/pi/.local/lib/python3.7/site-packages/tflite_runtime/__init__.py)
```

## Microcontrollers
* https://www.tensorflow.org/lite/microcontrollers/overview
* https://learn.adafruit.com/tensorflow-lite-for-microcontrollers-kit-quickstart