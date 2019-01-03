from api_demo.util import util
from api_demo.util.send_base import send

osign_list = ['userName', 'password','verifyCode']    # 定义签名参数列表，例如签名方法为 username+password+verifycode 做md5 。  具体需要替换为实际的签名参数列表。

def login_osign(user):   # 签名方法。  这里举例是进行 MD5 加密， 具体需要替换为实际的签名方法。
    user['osign'] = util.getOsign(user, osign_list)
    return user

def login(user,need_osign = True,isMock=False):     # 具体的接口url 拼接、参数生成和发送方法
    url = '/login'
    if need_osign:
        login_osign(user)
    return send(user, url,isMock=isMock)