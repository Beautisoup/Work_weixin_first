# -*- coding: utf-8 -*-
import unittest
import self
import pytest
import allure
from Work_weixin.apis.department import Department
@allure.feature('通讯录管理')
class TestUser(unittest.TestCase):
    def setUp(self):
        self.department = Department()
        # 准备测试数据
        # 新增员工信息
        self.createworker_data = {
            "userid": "test2",
            "name": "张三",
            "alias": "jackt",
            "mobile": "+86 13800000000",
            "department": [2200],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "1339549930@qq.com",
            # "biz_mail": "1339549930@qq.com",
            "is_leader_in_dept": [1],
            "direct_leader": ["test1"],
            "enable": 1,
            # "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "main_department": 1,
            "extattr": {
                "attrs": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    }
                ]
            },
            "to_invite": True,
            "external_position": "高级产品经理",
            "external_profile": {
                "external_corp_name": "",
                # "wechat_channels": {
                #     "nickname": "视频号名称"
                # },
                "external_attr": [
                    {
                        "type": 0,
                        "name": "文本名称",
                        "text": {
                            "value": "文本"
                        }
                    },
                    {
                        "type": 1,
                        "name": "网页名称",
                        "web": {
                            "url": "http://www.test.com",
                            "title": "标题"
                        }
                    },
                    {
                        "type": 2,
                        "name": "测试app",
                        "miniprogram": {
                            "appid": "wx8bd8012614784fake",
                            "pagepath": "/index",
                            "title": "myworker"
                        }
                    }
                ]
            }
        }
        self.search_user_id = 'test2'
        self.search_user_id2 = 'test1'
        # 查询ID为test2的用户信息
        self.delparama = {
            'userid': self.search_user_id
        }

        self.searchdata = {
            "limit": 10000
        }
    @allure.story('成员管理')
    @allure.title('测试员工管理--增/查/删')
    def test_work(self):
        '''
        测试员工管理--增/查/删
        '''
        with allure.step('增加用户'):
            r1 = self.department.creat_worker(self.createworker_data)
            print(r1.json())
        with allure.step('断言增加成功'):
            assert r1.json()['errcode'] == 0
            assert r1.json()['errmsg'] == 'created'
        print('---------------------------------------')
        # 查询ID为test2的用户信息
        with allure.step('查询ID为test2的用户信息'):
            r3 = self.department.search_worker(self.searchdata)
            print(r3.json())
            ids = [i['userid'] for i in r3.json()['dept_user']]
        # {'errcode': 0, 'errmsg': 'ok', 'dept_user': [{'userid': 'test1', 'department': 2200}, {'userid': 'LiYuanRui', 'department': 1}, {'userid': 'momo12345', 'department': 1}]}
        # ['test1', 'LiYuanRui', 'momo12345']
        # print(ids)
        with allure.step('断言test2在用户列表中'):
            assert self.search_user_id in ids
        print('---------------------------------------')
        with allure.step('删除用户test2'):
            r2 = self.department.del_worker(self.delparama)
        print(r2.json())
        with allure.step('断言删除成功'):
            assert r2.json()['errcode'] == 0
            assert r2.json()['errmsg'] == 'deleted'

        # 单调查询接口
    def test_search_worker(self):
        # 查询ID为test2的用户信息
        r3 = self.department.search_worker(self.searchdata)
        print(r3.json())
        ids = [i['userid'] for i in r3.json()['dept_user']]
        # {'errcode': 0, 'errmsg': 'ok', 'dept_user': [{'userid': 'test1', 'department': 2200}, {'userid': 'LiYuanRui', 'department': 1}, {'userid': 'momo12345', 'department': 1}]}
        # ['test1', 'LiYuanRui', 'momo12345']
        # print(ids)
        assert self.search_user_id2 in ids
#报告
'''
pytest -vs test_user.py --alluredir=./report --clean-alluredir
allure serve ./reportallure serve ./report
'''