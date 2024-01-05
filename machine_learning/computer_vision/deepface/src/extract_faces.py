from deepface import DeepFace
import cv2


im = cv2.imread(r"machine_learning/computer_vision/deepface/data/face/3.jpg")

# 除了传递路径，也可以传一个 Numpy 数组
# 因为一张图片可能包含多张人脸，所以返回的是一个列表，列表的每个元素是字典
results = DeepFace.extract_faces(
    im, detector_backend="retinaface", enforce_detection=False
)


for result in results:
    facial_area = result["facial_area"]
    cv2.rectangle(
        im,
        (facial_area["x"], facial_area["y"]),
        (facial_area["x"] + facial_area["w"], facial_area["y"] + facial_area["h"]),
        (0, 255, 0),
        1,
    )

cv2.imshow("1", im)
cv2.waitKey(0)
