import requests
from requests import request


class BaseApi:
    #解包
    def send_api(self, req):
        # 对request进行二次封装，用到了解包方式
        '''
        req = {
            'method': '',
            'url': '',
            'params': {},
            'data': {},
            'json': {}
        }
        '''
        r = request(**req)
        return r