# -*- coding: utf-8 -*-
'''
业务接口
'''
import requests
# -*- coding: utf-8 -*-
from Work_weixin.apis.wework import WeWork
# 部门需要继承 Wework，这样就可以直接获取 Wework 中获取到的 access_token

class Department(WeWork):
    def __init__(self):
        super().__init__()
        self.gettoken = self.get_token()

    def creat(self,data):
        '''
        创建部门
        :return:
        '''
        creat_url= f'{self.base_url}/cgi-bin/department/create?access_token={self.gettoken}'
        r = requests.post(creat_url,json = data)
        return r

    def update(self,data):
        '''更新部门'''
        update_url = f'{self.base_url}/cgi-bin/department/update?access_token={self.gettoken}'
        r = requests.post(update_url,json = data)
        return  r


    def delete(self, param):
        '''删除部门'''
        del_url = f'{self.base_url}/cgi-bin/department/delete?access_token={self.gettoken}'
        r = requests.get(del_url, params=param)
        return r

    def get_id(self,param):
        '''获取子部门ID列表'''
        get_url = f'{self.base_url}/cgi-bin/department/simplelist?access_token={self.gettoken}'
        r = requests.get(get_url, params = param)
        return r

    def get_all(self):
        get_url = f'{self.base_url}/cgi-bin/department/simplelist?access_token={self.gettoken}'
        r = requests.get(get_url)
        return r