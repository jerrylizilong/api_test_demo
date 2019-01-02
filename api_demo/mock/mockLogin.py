import random
import time
from api_demo.util import util
class login(object):
    def __init__(self,now_time = time.localtime(int(time.time())),random_value = str(random.randrange(1,99))):
        str_time = time.strftime('%Y-%m-%d-%H%M%S-',now_time)
        random_value=str_time+random_value
        self.userId='user_id_'+ random_value
        self.userName = 'user_name_'+random_value
        self.loginTime =time.strftime('%Y-%m-%d-%H:%M:%S',now_time)

    def login(self,query):
        data = {}
        osign = query['osign'][0]
        userName = query['userName'][0]
        password = query['password'][0]
        verifyCode = query['verifyCode'][0]
        if osign != util.md5(userName +password+verifyCode) or verifyCode !='123456':
            data['code']=4010
            data['msg']='invalid request!'
        elif userName !='correctuser' or password !='correctpassword' :
            data['code']=500
            data['msg']='username or password is wrong ,please try again!'
        else:
            data['code']=200
            data['msg']='success!'
            data['loginTime'] = self.loginTime
        return data

if __name__ == '__main__':
    print(login().login({'osign': ['a2f3d1771260b3a011697284fdb7e78c'], 'password': ['password'], 'userName': ['username'], 'verifyCode': ['verifyCode']}))