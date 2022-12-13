import random
import time
from api_demo.util import util

valid_user = [
    {'username':'david','password':'beckham'},
    {'username':'michael','password':'jordan'},
    {'username':'stephen','password':'curry'},
    {'username':'roger','password':'federer'},
    {'username':'correctuser','password':'correctpassword'},
]

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
        if osign != util.md5(userName +password+verifyCode) or verifyCode !='123456':      # 签名不匹配，或者验证码错误
            data['code']=4010
            data['msg']='invalid request!'
        else:
            if self.verify_user_password(userName,password) is False:
                data['code'] = 500
                data['msg'] = 'username or password is wrong ,please try again!'

            else:  # 正常登录
                data['code'] = 200
                data['msg'] = 'success!'
                data['loginTime'] = self.loginTime
        return data

    def verify_user_password(self,username,password):
        for user in valid_user:
            if user['username']==username:
                if user['password']==password:
                    return True
        return False



if __name__ == '__main__':
    # print(login().login({'osign': ['a2f3d1771260b3a011697284fdb7e78c'], 'password': ['password'], 'userName': ['username'], 'verifyCode': ['verifyCode']}))

    userlist =  list(map(lambda x: 'user_%s' % x, range(10)))
    print(userlist)