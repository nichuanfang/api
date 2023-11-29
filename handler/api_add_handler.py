import sys
import json
# 获取新增的数据

added_data = sys.argv[1]
print(added_data)
# 将added_data转为dict
added_data = json.loads(added_data)
# 将added_data新增到data.json中
with open('data.json', mode='r', encoding='utf-8') as my_file:
    text = my_file.read()
    # json转dict
    data = json.loads(text)
    # 增加数据
    data.append(added_data)
    # dict转json
    text = json.dumps(data)
    # 写入文件
    with open('data.json', mode='w', encoding='utf-8') as my_file:
        my_file.write(text)