import os
import time
from typing import Generator


def list_all_obvious_file(target_dir: str) -> list:
    """
    列出所有的非隐藏文件全路径(非目录)
    Args:
        target_dir: 被迭代地址

    Returns:
        生成器
    """
    file_paths = []
    for name in os.listdir(target_dir):
        path = os.path.join(target_dir, name)
        if not name.startswith(".") and os.path.isfile(path):
            file_paths.append(path)
    return file_paths


def without_hide_dir_file_generator(target_dir: str) -> Generator:
    """
    生成器方法——用于迭代目标路径的所有文件，除了隐藏文件外的文件
    Args:
        target_dir: 被迭代地址

    Returns:
        生成器
    """
    for root, dirs, files in os.walk(target_dir):
        for file_name in files:
            file_full_url = os.path.join(root, file_name)
            if not file_name.startswith("."):
                yield file_full_url


def create_dir_if_not_exit(will_create_dir: str):
    """
        如果目标目录不存在，则创建目标目录
    Args:
        will_create_dir: 将被创建的目录

    Returns:
        None
    """
    if not os.path.exists(will_create_dir):
        os.makedirs(will_create_dir)


def write_text_to_file(line: str, file: str, mode="w"):
    """
        把字符串写入到文件中
    Args:
        line: 字符串
        file: 将被创建的文件
        mode: 写入模式 w覆盖写入   a追加

    Returns:
        None
    """
    with open(file, mode) as f:
        f.write(line)


def write_text_to_file_if_not_exist(line: str, file: str, block: bool = False):
    """
        把字符串写入到文件中，如果文件不存在
    Args:
        line: 字符串
        file: 将被创建的文件
        block: 如果文件已存在，则不会覆盖旧文件，阻塞直到旧文件被删除

    Returns:
        None
    """
    while os.path.exists(file) and block:
        time.sleep(1)
    with open(file, "w") as f:
        f.write(line)
