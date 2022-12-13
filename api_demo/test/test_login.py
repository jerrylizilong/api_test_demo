# -*- coding: utf-8*-

from api_demo.api_manage.api_base import getOsign,api_send
import pytest,allure
from api_demo import environmentFlag

isMock = True    # 如果不需要使用 mock ，直接使用接口，此处改为 False
osign_list = ['userName', 'password','verifyCode']    # 定义签名参数列表，例如签名方法为 username+password+verifycode 做md5 。  具体需要替换为实际的签名参数列表。
url = '/login'    # 具体的接口 url 相对路径， 测试时会拼凑为完整路径：  http://host/login
valid_user = [
    {'username':'david','password':'beckham'},
    {'username':'michael','password':'jordan'},
    {'username':'stephen','password':'curry'},
    {'username':'stephen','password':'curry1'},
    {'username':'stephen','password':'curry2'},
    {'username':'roger','password':'federer'}
]

code_success = 200
msg_success = 'success!'

code_sign_error = 4010
msg_sign_error = 'invalid request!'

code_login_fail = 500
msg_login_fail = 'username or password is wrong ,please try again!'







@allure.story('test login with single data')
def test_login_single(init_test_user):
    testuesr = init_test_user
    result =api_send(testuesr,osign_list,url,isMock=isMock)
    assert result['code']==code_success
    assert result['msg']==msg_success
@allure.title('test login with user')
@pytest.mark.parametrize("user", valid_user)
def test_login_para(init_test_user,user):
    testuesr = init_test_user
    testuesr['userName'] = user['username']
    testuesr['password'] = user['password']
    allure.dynamic.title('test login with user: %s %s' %(user['username'],user['password']))
    result =api_send(testuesr,osign_list,url,isMock=isMock)
    assert result['code']==code_success
    assert result['msg']==msg_success

@pytest.mark.skipif(environmentFlag =='1', reason='skip')
@pytest.mark.parametrize("username", list(map(lambda x: 'user_%s' % x, range(10))))
# 异常场景： userName错误。
def test_login_wrong_userName(init_test_user,username):
    testuesr = init_test_user
    print(environmentFlag =='1')
    print('evironment is : ',environmentFlag)

    allure.dynamic.title('test login with invalid user: %s' %(username))
    testuesr['userName']= username
    result = api_send(testuesr,osign_list,url,isMock=isMock)
    assert result['code'] == code_login_fail
    assert result['msg'] == msg_login_fail

@pytest.mark.skipif(isMock is False , reason='skip')
# 异常场景： password错误。
def test_login_wrong_password(init_test_user):
    testuesr = init_test_user
    testuesr['password']='password'
    result = api_send(testuesr,osign_list,url,isMock=isMock)
    assert result['code'] == code_login_fail
    assert result['msg'] == msg_login_fail


# 异常场景： verifyCode错误。
def test_login_wrong_verifyCode(init_test_user):
    testuesr = init_test_user
    testuesr['verifyCode']='123455'
    result = api_send(testuesr,osign_list,url,isMock=isMock)
    assert result['code'] == code_sign_error
    assert result['msg'] == msg_sign_error

# 异常场景： 签名错误。
def test_login_osign_error(init_test_user):
    testuesr = init_test_user
    from api_demo.api_manage import api_base
    assert api_base.test_osign_error(testuesr,osign_list,url,code_sign_error,msg_sign_error,isMock=isMock)== 0

