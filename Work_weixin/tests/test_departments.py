# -*- coding: utf-8 -*-
import unittest
import self

from Work_weixin.apis.department import Department


class TestDepartments:

    def setup_class(self):
        #实例化部门类
        self.department = Department()
        # 准备测试数据
        self.depart_id = 220
        self.creat_data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.depart_id,
        }
        #部门更新
        self.update_name = 'new_name---update!!!'
        self.update_data = {
            "id": 220,
            "name": self.update_name,
        }
        #部门删和查
        self.del_param ={
            "id": self.depart_id,
        }
        self.get_param = {
            "id": self.depart_id,
        }
        #员工新增信息
        self.createworker_data = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [2200],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
            "biz_mail": "zhangsan@qyycs2.wecom.work",
            "is_leader_in_dept": [1],
            "direct_leader": ["lisi"],
            "enable": 1,
            "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
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
            "to_invite": 'true',
            "external_position": "高级产品经理",
            "external_profile": {
                "external_corp_name": "企业简称",
                "wechat_channels": {
                    "nickname": "视频号名称"
                },
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
                            "title": "my miniprogram"
                        }
                    }
                ]
            }
        }

        self.delparama ={
            'userid' : 'zhangsan'
        }


    def test_departments(self):
        '''
            部门增删改查场景测试
        '''
        #增
        r1 = self.department.creat(self.creat_data)
        #print(r1.json())
        assert r1.json().get('id') == self.depart_id
        #改
        r2 = self.department.update(self.update_data)
        print('改改',r2.json())
        #查
        rc = self.department.get_id(self.get_param)
        print('chacha',rc.json())
        ids = [i['id']for i in rc.json()['department_id']]
        assert self.depart_id in ids
        #删
        r = self.department.delete(self.del_param)
        print('ssssssssssssssss',r.json())
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "deleted"
        rall = self.department.get_all()
        ids = [i['id'] for i in rall.json()['department_id']]
        assert self.depart_id not in ids

    def test_work(self):
        '''
        测试员工管理--增/查
        '''
        r1 = self.department.creat_worker(self.createworker_data)
        print(r1.json())
        print('---------------------------------------')
        r2 = self.department.del_worker(self.del_param)
        print(r2.json())
