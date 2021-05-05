# coding = utf-8
# @Time : 2021/1/1 20:27
# @Author : 崔孟泽
# @File : read_data.py
# @Software: PyCharm
def readCsv(csv_path):
    with open(csv_path,'r',encoding='utf-8') as f1:
        lines = f1.readlines()
        # print(lines)
    return lines
# 自测程序
if __name__=='__main__':
    readCsv('./data.csv')