from pprint import pprint

# deep 库的所有功能都在 deep.DeepFace 子模块下面
from deepface import DeepFace
import cv2


print("-------------------------------对比两张图片---------------------------------")
result = DeepFace.verify(
    "machine_learning/deepface/data/face/yu1.jpg",
    "machine_learning/deepface/data/face/yu2.jpg",
)
pprint(result)

"""
{
    'detector_backend': 'opencv',
    'distance': 0.1402283383349574,
    'facial_areas': {'img1': {'h': 329, 'w': 329, 'x': 176, 'y': 27},
                    'img2': {'h': 272, 'w': 272, 'x': 159, 'y': 64}}, # facial_areas：由矩形表示的面部区域，x、y 表示矩形的左上顶点的坐标
    'model': 'VGG-Face',
    'similarity_metric': 'cosine',
    'verified': True   # verified：表示比对结果，即两张图片上的人是否为同一人
}

"""
print("-------------------------------矩形描绘---------------------------------")


rect_img1 = result["facial_areas"]["img1"]
rect_img2 = result["facial_areas"]["img2"]
im1 = cv2.imread("machine_learning/deepface/data/face/yu1.jpg")
im2 = cv2.imread("machine_learning/deepface/data/face/yu2.jpg")
cv2.rectangle(
    im1,
    (rect_img1["x"], rect_img1["y"]),
    (rect_img1["x"] + rect_img1["w"], rect_img1["y"] + rect_img1["h"]),
    (0, 255, 0),
    3,
)
cv2.rectangle(
    im2,
    (rect_img2["x"], rect_img2["y"]),
    (rect_img2["x"] + rect_img2["w"], rect_img2["y"] + rect_img2["h"]),
    (255, 0, 0),
    3,
)
cv2.imshow("1", im1)
cv2.imshow("2", im2)
cv2.waitKey(0)  # 阻塞
