import json

str = "[\"\\uff08\\u7f8e\\uff09  Y. Daniel Liang\"]"

res = json.loads(str)
print(res)
