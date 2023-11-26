import rapidjson

data = {'foo': 100, 'bar': 'baz'}
dumps_result=rapidjson.dumps(data)
print(dumps_result)
print(type(dumps_result))

loads_result=rapidjson.loads('{"bar":"baz","foo":100}')
print(loads_result)
print(type(loads_result))