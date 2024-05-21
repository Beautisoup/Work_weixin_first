# -*- coding: utf-8 -*-
import unittest
import self
import pytest
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

