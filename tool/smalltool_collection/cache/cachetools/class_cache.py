import time

from cachetools import TTLCache, cached


class DataOperationClass:
    # ttl即过期时间，单位是是秒
    @cached(cache=TTLCache(maxsize=32, ttl=25))
    def ttl_with_param_method(self, user_id, name, age):
        time.sleep(2)
        print(f"invoke true method, param is: {user_id},{name},{age}")
        return f"success ,user_id:{user_id}"


# 尝试在类上的缓存装饰器是否生效：理想情况下，给方法传递相同的参数，会命中缓存
def test_class_ttl_method():
    operation_class = DataOperationClass()
    print(operation_class.ttl_with_param_method(2, "zj", 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(2, "zj", 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(3, "zj", 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(2, "zj", 13))
    print("*" * 100)


if __name__ == "__main__":
    test_class_ttl_method()
