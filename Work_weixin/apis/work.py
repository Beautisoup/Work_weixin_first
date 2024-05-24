# -*- coding: utf-8 -*-
'''
业务接口
'''
import requests
from Work_weixin.apis.wework import WeWork
# 部门需要继承 Wework，这样就可以直接获取 Wework 中获取到的 access_token

class Work(WeWork):
    def __init__(self):
        super().__init__()
        self.gettoken = self.get_token()

    def creat_worker(self, data):
        creatworker_url = f'{self.base_url}/cgi-bin/user/create?access_token={self.get_token()}'
        #r = requests.post(creatworker_url, json=data)
        req ={
            'method': 'POST',
            'url': creatworker_url,
            'json': data
        }
        r= self.send_api(req)
        return r

    def del_worker(self, param):
        del_url = f'{self.base_url}/cgi-bin/user/delete?access_token={self.get_token()}'
        #r = requests.get(del_url, params=param)
        req = {
            'method': 'GET',
            'url': del_url,
            'params': param
        }
        r = self.send_api(req)
        return r

    def search_worker(self, data):
        search_url = f'{self.base_url}/cgi-bin/user/list_id?access_token={self.get_token()}'
        #r = requests.post(search_url, json=data)
        req = {
            'method': 'post',
            'url': search_url,
            'json': data
        }
        r = self.send_api(req)
        return r

