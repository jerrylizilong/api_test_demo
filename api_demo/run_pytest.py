import pytest
import os
currentPath = os.path.dirname(os.path.abspath(__file__))

def run_test():
    report_path = os.path.join(currentPath , 'reports')
    allure_report_path = os.path.join(currentPath , 'allurereport')
    test_folder = os.path.join(currentPath , 'test')
    # print(test_folder)
    pytest.main([test_folder,'--alluredir=%s' %(report_path),'-o log_cli=true -o log_cli_level=INFO'])

    # os.system('C:\\Python34\\allure-2.7.0\\bin\\allure serve %s' %report_path)
    os.system('C:\\Python34\\allure-2.7.0\\bin\\allure generate %s -o %s/html --clean' %(report_path,allure_report_path))    # 替换为本地的 allure 安装路径

