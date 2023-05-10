import time

from cachetools import cached, TTLCache


class DataOperationClass:

    # ttl即过期时间，单位是是秒
    @cached(cache=TTLCache(maxsize=32, ttl=25))
    def ttl_with_param_method(self, user_id, name, age):
        time.sleep(2)
        print(f"invoke true method, param is: {user_id},{name},{age}")
        return f'success ,user_id:{user_id}'


if __name__ == '__main__':
    operation_class = DataOperationClass()
    print(operation_class.ttl_with_param_method(2, 'zjy', 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(2, 'zjy', 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(3, 'zjy', 13))
    print("*" * 100)
    print(operation_class.ttl_with_param_method(2, 'zjy', 13))
    print("*" * 100)
