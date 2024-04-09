from pprint import pprint

import cv2
from deepface import DeepFace

print("-------------------------------分析图片---------------------------------")
image = cv2.imread(r"machine_learning/computer_vision/deepface/data/face/yu1.jpg")
# defalut analyze actions=("emotion", "age", "gender", "race")
results = DeepFace.analyze(image, detector_backend="mtcnn", enforce_detection=False)

pprint(results)

print("-------------------------------绘制分析结果---------------------------------")
for result in results:
    age = result["age"]
    emotion = result["dominant_emotion"]
    gender = result["dominant_gender"]
    race = result["dominant_race"]
    region = result["region"]

    # 绘制人脸矩形
    cv2.rectangle(
        image,
        (region["x"], region["y"]),
        (region["x"] + region["w"], region["y"] + region["h"]),
        (255, 0, 0),
        1,
    )
    # 绘制文字，该函数接收 9 个参数
    # 参数一: 原始图像；参数二: 绘制的文字内容；参数三: 在什么位置开始绘制
    # 参数四: 字体；参数五: 文字大小，等于字体的基础大小乘上传入的值，比如传入 1.5 表示放大 1.5 倍
    # 参数六: 文字颜色；参数七: 文字的线条粗细；
    # 参数八: 线条类型，可取值为 cv2.LINE_4、cv2.LINE_8 分别表示 8 邻接连接线、4 邻接连接线
    #        但是更推荐使用 cv2.LINE_AA，它是反锯齿连接线，背后采用了高斯滤波
    cv2.putText(
        image,
        f"age: {age}, emotion: {emotion}, gender: {gender}, race: {race}",
        (region["x"] - 600, region["y"] - 500),
        cv2.MARKER_CROSS,
        2.5,
        (300, 1, 300),
        1,
        cv2.LINE_AA,
    )

cv2.imshow("...", image)
cv2.waitKey(0)
