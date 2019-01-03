import httplib2
import json
import re
def md5( preosign):
    import hashlib
    m = hashlib.md5()
    preosign = preosign.encode('utf-8')
    print(preosign)
    m.update(preosign)
    return m.hexdigest()

def dict_2_str(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s=%s" % (str(k), str(v))
        tmplist.append(tmp)
    return '&'.join(tmplist)


def sendRequest(url):
    http = httplib2.Http(timeout=30)
    headers = {'Content-type': 'application/json;charset=utf8'}
    tryTime = 3
    while tryTime:
        try :
            response, content = http.request(url, 'POST',headers=headers)
            content = content.decode('utf-8')
            break
        except Exception as e:
            response = "Error"
            content = e
            tryTime += -1
    return response, content

def sendbody( url,data):
    http = httplib2.Http(timeout=30)
    data = data.encode('utf-8')
    headers = {'Content-type': 'application/json;charset=utf8'}
    tryTime = 3
    while tryTime:
        try :
            response, content = http.request(url, 'POST',body=data,headers=headers)
            content = content.decode('utf-8')
            break
        except Exception as e:
            response = "Error"
            content = e
            tryTime += -1
    return response, content


def hBody(j, needRE='0'):
    body = json.dumps(j, default=lambda j: j.__dict__, sort_keys=True,skipkeys= True)
    if needRE == '1':
        body = re.sub(r'\\', '', body)
        body = json.loads(body)
    return body


def getOsign(user,osignList):
    paraPand = ''
    for para in osignList:
        paraPand += str(user[para])
    return md5(paraPand)