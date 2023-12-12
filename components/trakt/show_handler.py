# 剧集 处理类
from core import cache


@cache.cache_with_expiry(1)
def get_index():
    return ''
