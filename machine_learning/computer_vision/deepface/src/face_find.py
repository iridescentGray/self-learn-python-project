from pprint import pprint

from deepface import DeepFace

# 除了传递路径，也可以传一个 Numpy 数组
# 因为一张图片可能包含多张人脸，所以返回的是一个列表，列表的每个元素是字典
results = DeepFace.find(
    img_path="machine_learning/computer_vision/deepface/data/face/yu2.jpg",
    db_path="machine_learning/computer_vision/deepface/data/db",
)
pprint(results)
