# -*- coding: utf-8*-

import unittest
from api_demo.api_manage.login import login_osign,login

code_success = 200
msg_success = 'success!'

code_sign_error = 4010
msg_sign_error = 'invalid request!'

code_login_fail = 500
msg_login_fail = 'username or password is wrong ,please try again!'

isMock = True    # 如果不需要使用 mock ，直接使用接口，此处改为 False

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
        result =login(self.testuser,isMock=isMock)
        self.assertEqual(result['code'],code_success)
        self.assertEqual(result['msg'],msg_success)


    # 异常场景： userName错误。
    def test_login_wrong_userName(self):
        self.testuser['userName']='username'
        result = login(self.testuser, isMock=isMock)
        self.assertEqual(result['code'],code_login_fail)
        self.assertEqual(result['msg'],msg_login_fail)


    # 异常场景： password错误。
    def test_login_wrong_password(self):
        self.testuser['password']='password'
        result = login(self.testuser, isMock=isMock)
        self.assertEqual(result['code'],code_login_fail)
        self.assertEqual(result['msg'],msg_login_fail)


    # 异常场景： verifyCode错误。
    def test_login_wrong_verifyCode(self):
        self.testuser['verifyCode']='123455'
        result = login(self.testuser, isMock=isMock)
        self.assertEqual(result['code'],code_sign_error)
        self.assertEqual(result['msg'],msg_sign_error)


    # 异常场景：osign 错误。 userName
    def test_login_osign_error_userName(self):
        self.testuser=login_osign(self.testuser)
        self.testuser['userName']=self.testuser['userName']+'1'
        result =login(self.testuser,need_osign=False,isMock=isMock)
        self.assertEqual(result['code'],code_sign_error)
        self.assertEqual(result['msg'],msg_sign_error)


    # 异常场景：osign 错误。 password
    def test_login_osign_error_password(self):
        self.testuser=login_osign(self.testuser)
        self.testuser['password']=self.testuser['password']+'1'
        result =login(self.testuser,need_osign=False,isMock=isMock)
        self.assertEqual(result['code'],code_sign_error)
        self.assertEqual(result['msg'],msg_sign_error)


    # 异常场景：osign 错误。 verifyCode
    def test_login_osign_error_verifyCode(self):
        self.testuser=login_osign(self.testuser)
        self.testuser['verifyCode']=self.testuser['verifyCode']+'1'
        result =login(self.testuser,need_osign=False,isMock=isMock)
        self.assertEqual(result['code'],code_sign_error)
        self.assertEqual(result['msg'],msg_sign_error)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
