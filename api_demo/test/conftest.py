import pytest
@pytest.fixture(scope='module')
def init_test_user():

    # 通用参数初始化
    testuesr = {}
    testuesr['userName']='correctuser'
    testuesr['password']='correctpassword'
    testuesr['verifyCode']='123456'
    return testuesr

