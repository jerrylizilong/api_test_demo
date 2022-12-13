import pytest
import os,time
currentPath = os.path.dirname(os.path.abspath(__file__))
date =time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

def run_test():
    report_path = os.path.join(currentPath , 'reports',str(date))
    allure_report_path = os.path.join(currentPath , 'allure-report',str(date))
    test_folder = os.path.join(currentPath , 'test')
    # print(test_folder)
    # pytest.main([test_folder,'--alluredir=%s' %(report_path),'-n 3','--reruns 1','--dist=load','-o log_cli=true -o log_cli_level=INFO'])
    os.system('python -m pytest %s -n 3 --reruns 2 --dist=load --alluredir=%s -o log_cli=true -o log_cli_level=INFO' %(test_folder,report_path))
    os.system('allure generate %s -o %s -c' %(report_path,allure_report_path))


if __name__=='__main__':
    run_test()
