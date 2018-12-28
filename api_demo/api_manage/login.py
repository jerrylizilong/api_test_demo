from api_demo.util import util
from api_demo.util.send_base import send


def login_osign(user):   # 签名方法，例如签名方法为 username+password+verifycode 做md5 。  具体需要替换为实际的签名方法。
    user['osign'] = util.md5(user['userName']+user['password']+user['verifyCode'] )
    return user

def login(user,need_osign = True,isMock=False):     # 具体的接口url 拼接、参数生成和发送方法
    url = '/login'
    if need_osign:
        login_osign(user)
    return send(user, url,isMock=isMock)