from unittest import TestCase
from api_demo import registApi,loginApi
import time,random
class test_api(TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print('end')

    def test1(self):
        now_time = time.localtime(int(time.time()))
        random_value = str(random.randrange(1, 99))
        assert registApi.registApi(now_time,random_value).regist()['user_id']==loginApi.loginApi(now_time,random_value).login()['user_id']