import requests
from requests import request


class BaseApi:
    #���
    def send_api(self, req):
        # ��request���ж��η�װ���õ��˽����ʽ
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