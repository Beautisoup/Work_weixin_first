# -*- coding: utf-8 -*-
import requests

from Work_weixin.apis.base_api import BaseApi

'''
    封装业务的全局操作
    企业ID
    应用secret
    获取token
    '''

class WeWork(BaseApi):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.base_url = 'https://qyapi.weixin.qq.com'
        self.secreat = 'NBh_33dSqN4CMV4PLw2x2wsBuWNyUfOyUS_A-hJHy1I'
        self.scorpid = 'wwfc559d7de1d0d9c8'
        self.token = self.get_token()

    def get_token(self):

        url = f'{self.base_url}/cgi-bin/gettoken'
        param = {
            'corpid': self.scorpid,
            'corpsecret': self.secreat,
        }
        req = {
            'method': 'GET',
            'url': url,
            'params': param,
        }
        r = self.send_api(req)
        #r = requests.get(self.base_url + '/cgi-bin/gettoken', params=param)
        #print(r.text)
        token = r.json()['access_token']
        #print(token)
        return token