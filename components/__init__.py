# 读取components目录下的所有文件，将其注册到组件列表中
import os


blueprints = []

# 获取 components模块 trakt模块下的 blueprint 并加入到blueprints列表中
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith('.py') or file == '__pycache__':
        continue
    module = __import__(__name__ + '.' + file, fromlist=[file])
    if hasattr(module, 'blueprint'):
        blueprints.append(module.blueprint)
