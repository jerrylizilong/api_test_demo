# api_test_demo

## 简介
整理如何用 unittest 编写接口测试用例，和使用 pytest+allure 生成报表。

## 如何运行
- 下载源码。
- 安装 requirements
- 运行 run.bat/ run.sh 文件开始执行。
- 报告生成： 打开 api_demo.allurereport.html  下的 index.html 文件查看 allure 报告。（需要安装 allure ）

![example1](cmd.png "example1")

![example2](allure.png "example2")

## 结构介绍

### 1. 接口功能编写
api_demo.api_manage.login 示例如何为登录接口进行签名、拼接参数和url，及发送。

#### 使用说明： 按照实际待测试的接口定义进行修改。

```
def login_osign(user):   # 签名方法，例如签名方法为 username+password+verifycode 做md5 。  具体需要替换为实际的签名方法。
    user['osign'] = util.md5(user['userName']+user['password']+user['verifyCode'] )
    return user

def login(user,need_osign = True,isMock=False):     # 具体的接口url 拼接、参数生成和发送方法
    url = '/login'
    if need_osign:
        login_osign(user)
    return send(user, url,isMock=isMock)
  ```

### 2. 模拟接口功能实现
api_demo.mock     示例如何为登录接口生成mock 数据。
#### 使用说明： 如果接口已开发完成，可以使用，可忽略这步。

```
def login(self,query):
    data = {}
    osign = query['osign'][0]
    userName = query['userName'][0]
    password = query['password'][0]
    verifyCode = query['verifyCode'][0]
    if osign != util.md5(userName +password+verifyCode) or verifyCode !='123456':      # 签名不匹配，或者验证码错误
        data['code']=4010
        data['msg']='invalid request!'
    elif userName !='correctuser' or password !='correctpassword' :                # 用户名或密码错误
        data['code']=500
        data['msg']='username or password is wrong ,please try again!'
    else:                                                                               # 正常登录
        data['code']=200
        data['msg']='success!'
        data['loginTime'] = self.loginTime
    return data
```

### 3. 测试用例
 api_demo.test  示例如何编写不同场景的测试用例。
 #### 使用说明： 如果不需要使用 mock ，将 isMock 改为 False 即可；根据实际场景编写对应测试用例

```
def setUp(self):
    import warnings
    warnings.simplefilter("ignore", ResourceWarning)
    print("start")

    # 通用参数初始化
    self.testuser = {}
    self.testuser['userName']='correctuser'
    self.testuser['password']='correctpassword'
    self.testuser['verifyCode']='123456'

# 正常场景：login 是否成功。
def test_login(self):
    result =login(self.testuser,isMock=True)
    self.assertEqual(result['code'],code_success)
    self.assertEqual(result['msg'],msg_success)


# 异常场景： userName错误。
def test_login_wrong_userName(self):
    self.testuser['userName']='username'
    result = login(self.testuser, isMock=True)
    self.assertEqual(result['code'],code_login_fail)
    self.assertEqual(result['msg'],msg_login_fail)

```

### 4. pytest 执行和 allure 报告生成
run_pytest_entry.py 、 run_pytest.py

### 5. 环境切换
api_demo.__init__.py  文件中可以定义多个不同的测试环境地址，并通过 environmentFlag 进行切换：
```
environmentFlag='1'

if environmentFlag=='1':
    host = 'http://test1.com'
elif environmentFlag=='2':
    host = 'http://test2.com'
elif environmentFlag=='3':
    host = 'http://test3.com'
```

### 6. 命令行执行：run.bat/run.sh

python run_pytest_entry.py 1

其中最后的参数 1 为 environmentFlag， 如果需要切换不同的测试环境，只需传入不同的标记位。

