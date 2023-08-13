from pprint import pprint
# deep 库的所有功能都在 deep.DeepFace 子模块下面
from deepface import DeepFace

# 传入两张图片即可进行对比
result = DeepFace.verify("machine_learning/deepface/data/face/yu1.jpg", "machine_learning/deepface/data/face/yu2.jpg")
pprint(result)