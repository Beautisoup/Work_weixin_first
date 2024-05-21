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
        self.base_url = 'https://qyapi.weixin.qq.com'
        self.secreat = 'NBh_33dSqN4CMV4PLw2x2wsBuWNyUfOyUS_A-hJHy1I'
        self.scorpid = 'wwfc559d7de1d0d9c8'
        self.token = self.get_token()

        req = {

        }

    def get_token(self):
        param = {
            'corpid': self.scorpid,
            'corpsecret': self.secreat,
        }
        r = requests.get(self.base_url + '/cgi-bin/gettoken', params=param)
        #print(r.text)
        token = r.json()['access_token']
        #print(token)
        return token