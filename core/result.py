import json
from libsql_client.result import Row
from typing import Union
# 统一结果类


class Page:

    def __init__(self, curr_page: int = 1, page_size: int = 10, data=None):
        """分页对象

        Args:
            data (_type_): 分页数据
            page (int, optional): 当前页
            page_size (int, optional): 每页多少条数据
            total_page (int, optional): 总页数
            total_count (int, optional): 总条数
        """
        self.curr_page = curr_page
        self.page_size = page_size
        self.data = data

    def set_total_count(self, total_count: int):
        """设置总页数与总数

        Args:
            total_count (int): 总条数
        """
        self.total_count = total_count
        self.total_page = total_count // self.page_size + \
            (1 if total_count % self.page_size > 0 else 0)

    def __json__(self):
        return {
            'curr_page': self.curr_page,
            'page_size': self.page_size,
            'total_page': self.total_page,
            'total_count': self.total_count,
            'data': self.data
        }


class Result:

    @staticmethod
    def success(data: Union[str, dict, list, Page, Row, None] = None, code: int = 200, msg: str = 'success') -> str:
        """成功响应

        Args:
            data (Union[str, dict, list, Page, None], optional): _description_. Defaults to None.
            code (int, optional): _description_. Defaults to 200.
            msg (str, optional): _description_. Defaults to 'success'.

        Returns:
            str: _description_
        """
        res = {}
        if isinstance(data, Row):
            res['data'] = data.asdict()
        elif isinstance(data, Page):
            res['data'] = data.__json__()
        else:
            res['data'] = data
        res['code'] = code
        res['msg'] = msg
        return json.dumps(res)

    @staticmethod
    def fail(msg: Union[str, Exception] = 'failed', code: int = 500, data: Union[str, dict, list, Page, None] = None) -> str:
        """失败响应

        Args:
            data (Union[str, dict, list, Page, None], optional): _description_. Defaults to None.
            code (int, optional): _description_. Defaults to 500.
            msg (str, optional): _description_. Defaults to 'failed'.

        Returns:
            str: _description_
        """
        res = {}
        res['data'] = data.__json__() if isinstance(data, Page) else data
        res['code'] = code
        res['msg'] = msg if isinstance(msg, str) else str(msg)
        return json.dumps(res)
