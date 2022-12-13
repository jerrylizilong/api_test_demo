import api_demo
import sys
from api_demo import run_pytest

print(sys.argv)
api_demo.environmentFlag = str('1')   # 通过输入参数配置执行的环境
print('environmentFlag is:',api_demo.environmentFlag)
run_pytest.run_test()