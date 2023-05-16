# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pathlib

import requests

IMAGES_STORE = f"{str(pathlib.Path.home())}/Downloads/get_cartoon"


class MhgChapterPipeline:
    def process_item(self, item, spider):
        # 如果获取了图片链接，进行如下操作
        web_image_items = item["web_image_items"]
        if web_image_items:
            # 准备文件夹
            local_file_path = f'{IMAGES_STORE}/{item["name"]}'
            if not os.path.exists(local_file_path):
                os.makedirs(local_file_path)

            # 获取每一个图片链接
            for key, value in web_image_items.items():
                image_file_name = f"{str(key)}.jpeg"
                # 图片保存路径
                full_file_path = f"{local_file_path}/{image_file_name}"
                # 保存图片
                self.save_to_local(full_file_path, value)
        return item

    def save_to_local(self, full_file_path, web_image):
        with open(full_file_path, "wb") as handle:
            response = requests.get(
                url=web_image, headers={"Referer": "https://www.manhuagui.com/"}
            )
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
