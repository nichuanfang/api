# 剧集 处理类
from core import cache


@cache.cache_with_expiry(876000)
def get_index():
    return ''
