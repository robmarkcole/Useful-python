## Pytorch
* https://pytorch.org/
* Python, but also has a C++ interface
* PyTorch provides two high-level features: (1) Tensor computing (like NumPy) with strong acceleration via graphics processing units (GPU). (2) Deep neural networks built on a tape-based autodiff system
* There are two popular pytorch wrappers, fastai and pytorch-lightning
* Good idea to use colab as torch already installed and has GPU
* Pytorch saved models have the file extension `.pt`

## Hub
* https://pytorch.org/hub/
* Various models that can be easily imported and deployed
* Example deplyed model ([DeepLabV3 image segmentation](https://pytorch.org/hub/pytorch_vision_deeplabv3_resnet101/)) -> https://github.com/davidefiocco/streamlit-fastapi-model-serving

## pytorch-lightning
* https://github.com/PyTorchLightning/pytorch-lightning
* TLDR: Lightning is a way to organize your PyTorch code to decouple the science code from the engineering. It's more of a PyTorch style-guide than a framework. Cuts down boilerplate code.
* [Getting started with mnist](https://www.learnopencv.com/getting-started-with-pytorch-lightning/)
* [How To Tag Any Image Using Deep Learning](https://towardsdatascience.com/how-to-tag-any-image-using-deep-learning-84a0dc2e03c2)
* [object-detection-with-pytorch-lightning - kaggle](https://www.kaggle.com/artgor/object-detection-with-pytorch-lightning)
* [Surface Crack Classification](https://github.com/mtszkw/surface-crack)

## Face
* https://github.com/timesler/facenet-pytorch

## Object detection
* https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection
* detr -> https://github.com/facebookresearch/detr
* Yolo v5

## Medical imaging
* https://github.com/perone/medicaltorch/
* Fastai notebooks https://www.kaggle.com/c/rsna-intracranial-hemorrhage-detection/discussion/114214

## Serve using flask
* https://github.com/avinassh/pytorch-flask-api
* https://medium.com/datadriveninvestor/deploy-your-pytorch-model-to-production-f69460192217
* https://imadelhanafi.com/posts/train_deploy_ml_model/ (https://github.com/imadelh/ML-web-app)

## Train and deploy via sagemaker
* https://docs.aws.amazon.com/sagemaker/latest/dg/pytorch.html

## Deploy on azure
* [Efficient Serverless deployment of PyTorch models on Azure](https://medium.com/pytorch/efficient-serverless-deployment-of-pytorch-models-on-azure-dc9c2b6bfee7)

## References
* https://github.com/ritchieng/the-incredible-pytorch
* https://github.com/bharathgs/Awesome-pytorch-list