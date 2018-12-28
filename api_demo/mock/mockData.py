from urllib.parse import urlparse,parse_qs


def mockData(url):
    requestInfo = urlparse(url)
    if requestInfo.path == '/login':
        from api_demo.mock import mockLogin
        return mockLogin.login().login(parse_qs(requestInfo.query))

if __name__ == '__main__':
    url='http://test1.com/login?osign=a2f3d1771260b3a011697284fdb7e78c&password=password&userName=username&verifyCode=verifyCode'
    print(mockData(url))