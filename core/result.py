import json

# 统一结果类


class Result:

    @staticmethod
    def success(data: str | dict | list | None = None, code: int = 200, msg: str = 'success') -> str:
        res = {}
        res['data'] = data
        res['code'] = code
        res['msg'] = msg
        return json.dumps(res)

    @staticmethod
    def fail(data: str | dict | list | None = None, code: int = 500, msg: str = 'failed') -> str:
        res = {}
        res['data'] = data
        res['code'] = code
        res['msg'] = msg
        return json.dumps(res)
