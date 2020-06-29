## NVIDIA
* All hardware -> https://developer.nvidia.com/buy-jetson
* [Jetson projects](https://developer.nvidia.com/embedded/community/jetson-projects)
* [good blog - Jetson hacks](https://www.jetsonhacks.com/)

## Jetson nano
* Jetson nano $100 -> https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/jetson-nano/
* 128 CUDA cores GPU, ARM CPU, 4GB RAM, no wifi
* Supports pytorch (currently 1.1) and tensorflow
* Getting started course -> https://courses.nvidia.com/courses/course-v1:DLI+C-RX-02+V1/about
* [Hello world with Jetpack](https://github.com/dusty-nv/jetson-inference#hello-ai-world)
* [Jetson nano is supported by Balena](https://www.balena.io/docs/reference/hardware/devices/) -> prospect of deploying apps to fleet of Jetsons. Example app [OCR](https://github.com/ricktorzynski/balena-ocr-tesseract-docker)
* [Process up to 8 streams concurrently, at 1080p and 30 frames-per-second with a resnet10 model](https://github.com/Azure-Samples/NVIDIA-Deepstream-Azure-IoT-Edge-on-a-NVIDIA-Jetson-Nano)
* [Run classification at 75 FPS with ResNet-18](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-camera-2.md)
* [Live object detection with Mobilenet-V2 in 10 lines of python](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-example-2.md)

## NVIDIA Jetson Xavier NX Developer Kit
* https://developer.nvidia.com/embedded/jetson-xavier-nx-devkit
* https://www.jetsonhacks.com/2020/05/16/nvidia-jetson-xavier-nx-developer-kit/

## Jetson AGX Xavier
* Higher end dev kit $699
* https://developer.nvidia.com/embedded/jetson-agx-xavier-developer-kit
* 512-core Volta GPU, 16 GB

## Jetson TX2
* Mid range $400
* [Buy the dev kit](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
* 8 GB, wifi

## Jetpack SDK: build AI apps
* https://developer.nvidia.com/embedded/jetpack
* JetPack SDK is the most comprehensive solution for building AI applications - bundles all required dev tools
* Python or C++

## deepstream-sdk: streaming analytics toolkit
* https://developer.nvidia.com/deepstream-sdk
* SDK is in C but has python bindings -> https://github.com/NVIDIA-AI-IOT/deepstream_python_apps
* DeepStream SDK delivers a complete streaming analytics toolkit for AI-based video and image understanding, as well as multi-sensor processing

## Projects
* [Count vehicles, people (javascript)](https://github.com/opendatacam/opendatacam)
* [Security camera with Raspberry pi and NVIDIA Jetson platforms (python)](https://github.com/dataplayer12/homesecurity)
* [Push object data to Azure](https://www.hackster.io/pjdecarlo/intelligent-closed-circuit-tv-with-azure-and-nvidia-jetson-6df06f)
* [Jetson kubernetes cluster](https://medium.com/jit-team/building-a-gpu-enabled-kubernets-cluster-for-machine-learning-with-nvidia-jetson-nano-7b67de74172a)
* [3D printed case](https://cults3d.com/en/3d-model/tool/jetson-nano-case)
* [Pothole detector](https://github.com/JordanMicahBennett/Smart-Ai-Pothole-Detector------Powered-by-Tensorflow-TensorRT-on-Google-Colab-and-or-Jetson-Nano)
* [Face recognition with dlib](https://medium.com/@ageitgey/build-a-hardware-based-face-recognition-system-for-150-with-the-nvidia-jetson-nano-and-python-a25cb8c891fd)
* [Run Yolo - on nano only yolov3-tiny](https://pysource.com/2019/08/29/yolo-v3-install-and-run-yolo-on-nvidia-jetson-nano-with-gpu/?unapproved=1323&moderation-hash=175e57f50e7350d7d591c5db18ba8fbb#comment-1323)
* [Monitor Jetson CPU usage etc](https://github.com/rbonghi/jetson_stats)
* [Detect significant changes in a camera feed to save bandwidth](https://www.hackster.io/smellslikeml/saving-bandwidth-with-anomaly-detection-16eb67)
* Azure custom vision model deployment via [Docker on Jetson nano](https://medium.com/microsoftazure/running-a-gpu-enabled-azure-custom-vision-docker-container-on-a-nvidia-jetson-nano-db8747b00b4f) (flask app)

## In production
* [AWS IoT Greengrass on Jetson Nano](https://info.nvidia.com/deploy-ai-with-aws-ml-iot-services-on-nvidia-jetson-nano.html?ondemandrgt=yes) and [this repo](https://github.com/mahendrabairagi/AWS_ML_At_Edge_With_NVIDIA_Jetson_Nano)

## TensorRT
* https://developer.nvidia.com/tensorrt
* A deep learning inference optimizer and runtime - up to 40x faster than CPU-only platforms
* TensorRT Inference Server is a containerized microservice that maximizes GPU utilization and runs multiple models 
* Optimize neural network models trained in all major frameworks

## CUDA
* NVIDIA’s parallel programming model