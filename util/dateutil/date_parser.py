from dateutil import parser

parse_result = parser.parse("2018-3-1")

print(f"parse_result is {parse_result}")
print(f"parse_result type is {type(parse_result)}")

print(parser.parse("2018-03-2"))

print(parser.parse("2018/3/3"))
print(parser.parse("2018/03/04"))
print(parser.parse("03-05"))
print(parser.parse("03/06/18"))
print(parser.parse("03/07/18"))

print(parser.parse("32-3"))
print(parser.parse("1221"))
print(parser.parse("100-7"))
