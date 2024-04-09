import orjson

data = {"foo": 100, "bar": "baz"}
dumps_result = orjson.dumps(data)
print(dumps_result)
print(type(dumps_result))

loads_result = orjson.loads('{"bar":"baz","foo":100}')
print(loads_result)
print(type(loads_result))
