import libsql_client
import os

# 获取数据库url
try:
    TURSO_DB_URL = os.environ.get('TURSO_DB_URL')
except:
    raise Exception('请先设置环境变量TURSO_DB_URL')
# 获取数据库token
try:
    TURSO_DB_AUTH_TOKEN = os.environ.get('TURSO_DB_AUTH_TOKEN')
except:
    raise Exception('请先设置环境变量TURSO_DB_AUTH_TOKEN')


def acquire_client():
    """获取客户端(异步)

    Returns:
        _type_: 客户端
    """
    client = libsql_client.create_client(
        url=TURSO_DB_URL, auth_token=TURSO_DB_AUTH_TOKEN)  # type: ignore
    return client


def acquire_client_sync():
    """获取客户端(同步)

    Returns:
        _type_: 客户端

    """
    client = libsql_client.create_client_sync(
        url=TURSO_DB_URL, auth_token=TURSO_DB_AUTH_TOKEN)
    return client
