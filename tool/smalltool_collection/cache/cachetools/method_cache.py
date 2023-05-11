import time

from cachetools import TTLCache, cached


# ttl即过期时间，单位是是秒
@cached(cache=TTLCache(maxsize=32, ttl=5))
def ttl_with_param_method(user_id, name, age):
    time.sleep(2)
    print(f"invoke true method, param is: {user_id},{name},{age}")
    return f"success ,user_id:{user_id}"


# 尝试缓存装饰器是否生效：理想情况下，给方法传递相同的参数，会命中缓存
def test_ttl_method():
    print(ttl_with_param_method(2, "zj", 13))
    print("*" * 100)
    print(ttl_with_param_method(2, "zj", 13))
    print("*" * 100)
    print(ttl_with_param_method(3, "zj", 13))
    print("*" * 100)
    print(ttl_with_param_method(2, "zj", 13))
    print("*" * 100)


# 尝试缓存过期是否生效
def test_ttl_overdue():
    print(ttl_with_param_method(15, "lz", 13))
    print(ttl_with_param_method(15, "lz", 13))
    # 指定了5秒的缓存时间。睡眠6秒 会导致缓存过期
    time.sleep(6)
    print(ttl_with_param_method(15, "lz", 13))


if __name__ == "__main__":
    # test_ttl_method()
    print("-" * 100)
    test_ttl_overdue()
