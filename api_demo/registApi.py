import random
import time
class registApi(object):
    def __init__(self,now_time = time.localtime(int(time.time())),random_value = str(random.randrange(1,99))):
        self.api_url=''
        str_time = time.strftime('%Y-%m-%d-%H%M%S-',now_time)
        random_value=str_time+random_value
        self.user_id='user_id_'+ random_value
        self.user_name = 'user_name_'+random_value
        self.regist_time =time.strftime('%Y-%m-%d-%H:%M:%S',now_time)

    def regist(self):
        data = {}
        data['user_id']=self.user_id
        data['user_name']=self.user_name
        data['regist_time']=self.regist_time
        return data


# print(api1().regist())