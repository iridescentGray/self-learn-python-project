import exifread

with open("1.png", "rb") as f:
    # 直接可以拿到里面的信息，内容非常多
    exif = exifread.process_file(fh=f)


for tag in exif.keys():
    print(f"Key: {tag},  value: {exif[tag]}")


# 这里我们选一些常用的，里面的 value 我们需要转成字符串
# 不转成字符串的话看起来会比较费劲
print("图片宽度:", str(exif["EXIF ExifImageWidth"]))
print("图片高度:", str(exif["EXIF ExifImageLength"]))
