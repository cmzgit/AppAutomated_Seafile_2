# coding = utf-8
# @Time : 2021/1/1 20:16
# @Author : 崔孟泽
# @File : runner.py
# @Software: PyCharm
from run.BSTestRunner import BSTestRunner
import unittest
import time

def runTestCase():
    # 读取所有测试用例
    testcase_dir = '../testcase' # 所有测试用例的存放目录
    discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test_*.py')# 探索性测试（指定要执行的用例py文件）
    # 设置测试报告的名称
    report_dir = '../reports'    # 测试报告的存放目录
    now = time.strftime('%Y-%m-%d_%H-%M-%S_')
    report_name = report_dir + '/' + now +'崔孟泽_test-report.html'
    # 执行测试用例并生成测试报告
    with open(report_name,'wb') as f:
        runner = BSTestRunner(stream=f,title='崔孟泽的自动化测试报告',description='SEAFILE APP 自动化功能测试-登录')
        runner.run(discover)

if __name__=='__main__':
    runTestCase()