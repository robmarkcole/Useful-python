## Object detection DL models
### R-CNN
* [R-CNN and Fast/Faster/Mask R-CNN and YOLO](https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html)
* [Mask_RCNN Github](https://github.com/matterport/Mask_RCNN) and [kaggle usage](https://www.kaggle.com/c/data-science-bowl-2018/discussion/56326)
* [Building a Custom Mask RCNN model with Tensorflow Object Detection](https://towardsdatascience.com/building-a-custom-mask-rcnn-model-with-tensorflow-object-detection-952f5b0c7ab4)
* [Splash of Color: Instance Segmentation with Mask R-CNN and TensorFlow](https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46)

### YOLO
* [YOLO](https://pjreddie.com/darknet/yolo/)
* [How to implement a YOLO (v3) object detector from scratch in PyTorch](https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/)

### Other
* [A PyTorch Implementation of Single Shot MultiBox Detector](https://github.com/amdegroot/ssd.pytorch)
* [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
* [Building a Toy Detector with Tensorflow Object Detection API](https://towardsdatascience.com/building-a-toy-detector-with-tensorflow-object-detection-api-63c0fdf2ac95)
* [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](https://github.com/charlesq34/pointnet)
* https://modeldepot.io/

### Annotation tools
* http://www.robots.ox.ac.uk/~vgg/software/via/ - free html tool
* https://github.com/tzutalin/labelImg python with QT gui
* [Rectlabel for Mac](https://rectlabel.com/) - paid after 2 week trial, creates xml files
```xml
<annotation>
    <folder>Pictures</folder>
    <filename>dog.bmp</filename>
    <size>
        <width>249</width>
        <height>287</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>dog</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <difficult>0</difficult>
        <bndbox>
            <xmin>25</xmin>
            <ymin>15</ymin>
            <xmax>213</xmax>
            <ymax>263</ymax>
        </bndbox>
    </object>
</annotation>
```
