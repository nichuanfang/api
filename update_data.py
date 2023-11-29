# 更新data.json文件
import json
import requests

with open('data.json', mode='r+',encoding='utf-8') as my_file:
    text = my_file.read()
    data = json.loads(text)
    # 新增数据
    data.append({
        'name': '新数据',
        'age': 18
    })
    # 写入文件
    with open('data.json', mode='w+',encoding='utf-8') as my_file:
        my_file.write(json.dumps(data))

print('已更新数据!')