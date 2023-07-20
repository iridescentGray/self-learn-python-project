from functools import reduce
from typing import Dict

"""
simple_demo_to_show_what_is_map_reduce
"""


def map_frequency(text: str) -> Dict[str, int]:
    """
    计算每一行文本中，单词的频率
    """
    words = text.split(" ")
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def merge_dict(first: Dict[str, int],
               second: Dict[str, int]) -> Dict[str, int]:
    """
    对两行文本统计出的词频进行合并
    """
    keys = first.keys() | second.keys()
    return {key: first.get(key, 0) + second.get(key, 0) for key in keys}


lines = ["I know what I know", "I know that I know",
         "I don't know that much", "They don't know much"]

if __name__ == '__main__':
    mapped_results = [map_frequency(line) for line in lines]
    print(reduce(merge_dict, mapped_results))
