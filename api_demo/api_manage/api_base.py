from api_demo.util import util
from api_demo.util.send_base import send

def getOsign(user,osign_list):   # 签名方法。  这里举例是进行 MD5 加密， 具体需要替换为实际的签名方法。
    user['osign'] = util.getOsign(user, osign_list)
    return user

def api_send(user,osign_list,url,need_osign = True,isMock=False):     # 具体的接口url 拼接、参数生成和发送方法
    if need_osign:
        getOsign(user,osign_list)
    return send(user, url,isMock=isMock)

# 传入：签名参数列表 osign_list；   返回签名不匹配的参数数量，如果返回 0 ，表示测试通过
def test_osign_error(user,osign_list,url,code_sign_error,msg_sign_error,isMock=False):
        osignFailCount = 0
        for para in osign_list:
            result = osign_error(user,osign_list,url,code_sign_error,msg_sign_error,para,isMock=isMock)
            if not result:
                osignFailCount += 1
        print('osign para lenth : %d' % len(osign_list))
        return osignFailCount

# 单个参数的签名校验：在生成完签名后修改某个参数值，看接口能否正确校验
def osign_error(user,osign_list,url,code_sign_error,msg_sign_error, para,isMock=False):
    if para in ['']:    # 过滤的加密参数，部分参数不需要加密验证
        return True
    else:
        user = getOsign(user,osign_list)
        if isinstance(user[para],int):
            user[para]= user[para] + 1
        else :
            user[para]=str(user[para] + '1')
    result = api_send(user, osign_list, url,need_osign=False,isMock=isMock)
    if result['code'] == code_sign_error and result['msg'] == msg_sign_error:
        return True
    else:
        print('osign error : %s, %s' % (para, result))
        return False