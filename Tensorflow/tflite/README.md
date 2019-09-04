## TFlite
* Tflite is an alternative interpreter that requires optimised models, read -> https://www.tensorflow.org/lite/guide
* Regular tf models are converted to tflite -> https://www.tensorflow.org/lite/convert/

## Models
* List of pretrained tflite models -> https://www.tensorflow.org/lite/models

## Microcontrollers
* https://www.tensorflow.org/lite/microcontrollers/overview
* https://learn.adafruit.com/tensorflow-lite-for-microcontrollers-kit-quickstart

## Pi
* Following https://www.tensorflow.org/lite/guide/python on pi4 I hit:
```
pi@pi-4:~/tflite $ python3 label_image.py   --model_file /tmp/mobilenet_v1_1.0_224.tflite   --label_file /tmp/labels.txt   --image /tmp/grace_hopper.bmp
Traceback (most recent call last):
  File "label_image.py", line 27, in <module>
    from tflite_runtime import Interpreter
ImportError: cannot import name 'Interpreter' from 'tflite_runtime' (/home/pi/.local/lib/python3.7/site-packages/tflite_runtime/__init__.py)
```