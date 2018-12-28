import json
from api_demo import host
from api_demo.util import util
from api_demo.mock import mockData

def send(user,url,isMock=False,host=host,needJson=True):
    body = json.dumps(user, default=lambda user: user.__dict__, sort_keys=True, skipkeys=True)
    body = eval(body)
    list = util.dict_2_str(body)
    url = host+url+ '?' + list
    print(url)
    if isMock:
        return mockData.mockData(url)
    else:
        response, content = util.sendRequest(url)
        print(content)
        if needJson:
            content = json.loads(content)
        return content

