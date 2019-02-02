# -*- coding: utf-8*-

import unittest
from api_demo.api_manage.api_base import getOsign,api_send
import pytest
from api_demo import environmentFlag

isMock = True    # 如果不需要使用 mock ，直接使用接口，此处改为 False
osign_list = ['userName', 'password','verifyCode']    # 定义签名参数列表，例如签名方法为 username+password+verifycode 做md5 。  具体需要替换为实际的签名参数列表。
url = '/login'    # 具体的接口 url 相对路径， 测试时会拼凑为完整路径：  http://host/login

code_success = 200
msg_success = 'success!'

code_sign_error = 4010
msg_sign_error = 'invalid request!'

code_login_fail = 500
msg_login_fail = 'username or password is wrong ,please try again!'


class mytest(unittest.TestCase):
    @classmethod
    def setUp(self):
        import warnings
        warnings.simplefilter("ignore", ResourceWarning)
        print("start")

        # 通用参数初始化
        self.testuser = {}
        self.testuser['userName']='correctuser'
        self.testuser['password']='correctpassword'
        self.testuser['verifyCode']='123456'

    def tearDown(self):
        print("end")

    # 正常场景：login 是否成功。
    def test_login(self):
        result =api_send(self.testuser,osign_list,url,isMock=isMock)
        self.assertEqual(result['code'],code_success)
        self.assertEqual(result['msg'],msg_success)

    @pytest.mark.skipif(environmentFlag =='1', reason='skip')
    # 异常场景： userName错误。
    def test_login_wrong_userName(self):
        print(environmentFlag =='1')
        print('evironment is : ',environmentFlag)
        self.testuser['userName']='username'
        result = api_send(self.testuser,osign_list,url,isMock=isMock)
        self.assertEqual(result['code'],code_login_fail)
        self.assertEqual(result['msg'],msg_login_fail)

    @pytest.mark.skipif(isMock , reason='skip')
    # 异常场景： password错误。
    def test_login_wrong_password(self):
        self.testuser['password']='password'
        result = api_send(self.testuser,osign_list,url,isMock=isMock)
        self.assertEqual(result['code'],code_login_fail)
        self.assertEqual(result['msg'],msg_login_fail)


    # 异常场景： verifyCode错误。
    def test_login_wrong_verifyCode(self):
        self.testuser['verifyCode']='123455'
        result = api_send(self.testuser,osign_list,url,isMock=isMock)
        self.assertEqual(result['code'],code_sign_error)
        self.assertEqual(result['msg'],msg_sign_error)

    # 异常场景： 签名错误。
    def test_login_osign_error(self):
        from api_demo.api_manage import api_base
        self.assertEqual(api_base.test_osign_error(self.testuser,osign_list,url,code_sign_error,msg_sign_error,isMock=isMock), 0)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
