import json

dict = {"a":1, "b":2, "c":3}
# 存储至本地
with open("dict.json", "w") as f:
    data = json.dumps(dict, ensure_ascii=False, indent=5)
    f.write(data)

# 从本地读取
with open("dict.json", "r") as f:
    data = f.read()
    print(data)
    print(type(data))
    data1 = json.loads(data)
    print(data1)
    print(type(data1))
