import api_demo
import sys
from api_demo import run_pytest

environment = '2'
print(sys.argv)
try:
    environment = sys.argv[1]
except Exception as e:
    print(e)
api_demo.environmentFlag = environment  # 通过输入参数配置执行的环境
print('environmentFlag is:',api_demo.environmentFlag)
run_pytest.run_test()