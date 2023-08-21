# deepface

A Lightweight Face Recognition and Facial Attribute Analysis (Age, Gender, Emotion and Race) Library

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.12 deepface
    pyenv activate deepface
    python -m pip install --upgrade pip
    cd machine_learning/deepface
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Related documents

    deepface-github：https://github.com/serengil/deepface

## project

## 注释：人脸检测器

"opencv"：最轻量级的人脸检测器，使用不基于深度学习技术的 haar-cascade 算法，因此速度很快，但准确率较低。而为了使 OpenCV 正常工作，需要正面图像，如果脸侧了一下或者局部发生遮挡，准确率就会受到影响。此外也不擅长对眼睛的检测，容易导致对齐问题。目前 DeepFace 使用的默认检测器就是 OpenCV。

"dlib"：该检测器在后台使用 hog 算法，与 OpenCV 类似，它也不是基于深度学习的，但它的检测和对齐分数相对较高。

"ssd"：单次检测器，它是一种流行的基于深度学习的检测器，但性能可与 OpenCV 相媲美。只是 SSD 不支持面部特征点，并且依赖于 OpenCV 的眼睛检测模块来对齐，因此尽管其检测性能很高，但对准分数仅为平均水平。

"mtcnn"：基于深度学习的人脸检测器，并带有面部特征点，所以它的检测和对齐得分都很高但是，但速度比 OpenCV，SSD 和 Dlib 慢。另外 MTCNN 是一种多任务级联卷积神经网络的人脸检测算法，能够同时实现人脸检测、关键点定位和人脸对齐等功能。其对于大尺寸人脸的检测效果较好，并且模型规模相对于 RetinaFace 的较小。

"retinaface"：一种基于卷积神经网络的人脸检测算法，具有高精度的特点，被公认为是最先进的人脸检测算法，但需要很高的计算能力。相比 MTCNN，检测小尺寸人脸的效果更好。

## uninstall

    pyenv virtualenv-delete deepface
