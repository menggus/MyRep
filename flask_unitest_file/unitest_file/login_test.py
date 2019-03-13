import unittest  # 单元测试模块
from flask_app import app
import json


class LoginTest(unittest.TestCase):

    def setUp(self):  # 固定方法，首先执行
        # 开启flask测试debug，便于查找错误
        app.config['TESTING'] = True
        # 使用flask中的测试客户端进行模拟
        self.client = app.test_client()

    def tearDown(self):  # 固定方法，最后执行
        pass

    def test_empty_username_password(self):  # 方法名 test_  为固定前缀
        """模拟客户端post请求登录"""
        # 测试账号密码不完整情况
        # 1.无账号、密码 data={}
        ret = self.client.post('/login', data={})  # 响应体res
        res_to_dict = json.loads(ret.data)  # 获取res的数据，并转化为字典
        # 断言
        self.assertIn("code", res_to_dict)
        self.assertEqual(res_to_dict.get('code'), 1)

        # 2.测试有账号、无密码
        ret = self.client.post('/login', data={'username': "tao"})
        res_to_dict = json.loads(ret.data)  # 获取res的数据，并转化为字典
        # 断言
        self.assertIn("code", res_to_dict)
        self.assertEqual(res_to_dict.get('code'), 1)

        # 2.测试无账号、有密码
        ret = self.client.post('/login', data={'password': "tao"})
        res_to_dict = json.loads(ret.data)  # 获取res的数据，并转化为字典
        # 断言
        self.assertIn("code", res_to_dict)
        self.assertEqual(res_to_dict.get('code'), 1)

    def test_correct_username_password(self):
        """测试账密的正确性"""
        # 1.正确账号。密码
        ret = self.client.post('/login', data={'username': 'admin', 'password': '123456'})
        res_to_dict = json.loads(ret.data)  # 获取res的数据，并转化为字典
        # 断言
        self.assertIn("code", res_to_dict)
        self.assertEqual(res_to_dict.get('code'), 0)

        # 2.非正确账号、密码
        ret = self.client.post('/login', data={'username': 'tao', 'password': '123456'})
        res_to_dict = json.loads(ret.data)  # 获取res的数据，并转化为字典
        # 断言
        self.assertIn("code", res_to_dict)
        self.assertEqual(res_to_dict.get('code'), 2)


if __name__ == '__main__':
    unittest.main()  # 执行当前文件下的测试
