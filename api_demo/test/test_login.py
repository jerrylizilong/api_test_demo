# -*- coding: utf-8*-

import unittest
from api_demo.api_manage.login import login_osign,login,osign_list

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

    # 异常场景： 签名错误。
    def test_login_osign_error(self):
        osignFailCount = 0
        for para in osign_list:
            result = self.login_osign_error(para)
            if not result:
                osignFailCount += 1
        print('osign para lenth : %d' % len(osign_list))
        self.assertEqual(osignFailCount, 0)

    def login_osign_error(self, para):
        self.testuser = login_osign(self.testuser)
        self.testuser[para] = self.testuser[para] + '1'
        result = login(self.testuser, need_osign=False,isMock=isMock)
        if result['code'] == code_sign_error and result['msg'] == msg_sign_error:
            return True
        else:
            print('osign error : %s, %s' % (para, result))
            return False

if __name__ == '__main__':
    unittest.main(warnings='ignore')
