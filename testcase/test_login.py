# coding = utf-8
# @Time : 2021/1/1 20:12
# @Author : 崔孟泽
# @File : test_login.py
# @Software: PyCharm
# from data.read_data import getCsv
import unittest
from data.read_data import readCsv
from business.seafile_login import seafileLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        print('----测试seafile登录开始----')
    def tearDown(self):
        print('----测试seafile登录结束----')
    def test_login(self):
        # csv 的相对路径
        csv_path = r'../data/data.csv'
        # 读取 csv
        csv = readCsv(csv_path)
        # 分割 csv
        for i in range(len(csv)):
            print('\n'+'---这是第'+str(i+1)+'次登录测试---')
            # 读取 csv 内 url,username,password,expect
            c = csv[i].split(',')
            url = c[0]
            username = c[1]
            password = c[2]
            expect = c[3].strip()
            try:
                # 若csv内登录预期结果为true
                if expect =='true':
                    # 断言登录实际结果为true
                    self.assertTrue(seafileLogin(url,username,password))
                    print(c)
                else:
                    # 断言登录实际结果为false
                    self.assertFalse(seafileLogin(url,username,password))
                    print(c)
            except:
                print('不符合预期结果',expect,'本次测试不通过')
            else:
                print('符合预期结果',expect,'本次测试通过')
if __name__=='__main__':
    unittest.main()