## Yolo
* https://pjreddie.com/darknet/yolo/
* Python wrapper -> https://github.com/madhawav/YOLO3-4-Py (first `xcode-select --install`) -> Getting error `Library not loaded: libdarknet.so`

## Tiny YOLOv3
We have a very small model as well for constrained environments, yolov3-tiny.

## Yolo with openCV
* [Call Yolo from CopenCV]()

## Yolo on pi
* Using pjreddie version (including yolov3-tiny) I hit [this issue](https://github.com/pjreddie/darknet/issues/823) - recommended to use [AlexeyAB version](https://github.com/AlexeyAB/darknet)
* https://github.com/cristianpb/object-detection/blob/master/backend/yolo_detection.py

## Yolo on Jetson Nano 
* https://pysource.com/2019/08/29/yolo-v3-install-and-run-yolo-on-nvidia-jetson-nano-with-gpu/

## Yolo face
* [Yolo for faces only, run on CPU](https://github.com/iitzco/faced)

## Yolo vs others
* [Read](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/)
```
    If I know I need to detect small objects and speed is not a concern, I tend to use Faster R-CNN.
    If speed is absolutely paramount, I use YOLO.
    If I need a middle ground, I tend to go with SSDs.
```

## References
* [Yolo v3 paper](https://arxiv.org/pdf/1804.02767.pdf)
* [Streamlit demo](https://github.com/streamlit/demo-self-driving)
* Yolo v3 is used in [Deepstack object detection](https://python.deepstack.cc/object-detection)