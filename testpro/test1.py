# list_square = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         list_square.append(i * j)
# print(list_square)

# list_square1 = [[i * j for i in range(1, 4) for j in range(1, 4)]]
# 列表推导式
# print(list_square1)

# python 解释器的路径
# import   sys
# print(sys.path)


# 一个try可以对应多个except.final都会被执行
# try:
#     num1 = int(input("请输入一个数字: "))
#     num2 = int(input("请输入一个数字: "))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("被除数必须为正整数")
# finally:
#     print("-------这条语句都会被执行")

'''
json.dump   将dict类型->str,并写入到json文件中
json.dumps  将dict-> str  1
json.load   从json文件中读取数据
json.loads  将str转成dict
'''
# import json

# list_str = {"name": "张三", "age": 28, "job": "tester", "home": "苏北"}
# print(type(list_str))
# str_list = json.dumps(list_str).encode().decode("unicode_escape")
#
# print(type(str_list))
# print(str_list)

# with open('../testair/write.json', mode='w',encoding='utf-8') as f:
#     json.dump(list_str, f, ensure_ascii=False)

# import json
#
# file = '../testair/write.json'
# output = json.load(open(file, mode='r', encoding='utf-8',))
# print(output)

import json

# str1 = {"a": [1, 2]}
# print(type(str1))
#
# str2 = [{"a": 1}, {"b": 2}]
# print(type(str2))
#
#
# str3 = '{"a": [1, 2]}'
# print(type(str3))

# str4=json.loads(str3)
# print(type(str4))

# import shutil
# 将文件内容拷贝到另一个文件中
# shutil.copyfileobj(open('../testair/write.json','r'),open('before.json','w'))



