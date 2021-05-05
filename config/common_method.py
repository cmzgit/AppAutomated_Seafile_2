# coding = utf-8
# @Time : 2020/12/30 20:19
# @Author : 崔孟泽
# @File : common.py
# @Software: PyCharm
from appium import webdriver
import os
import yaml

def Caps():
    # .yaml 的目录
    yaml_dir = os.path.dirname(__file__)
    # .yaml 的绝对路径
    yaml_path = os.path.join(yaml_dir,'config.yaml')
    # 打开 yaml 文件路径的配置文件
    config_file = open(yaml_path,'r',encoding='utf-8')
    # 载入该配置文件内容
    config = yaml.load(config_file,Loader=yaml.FullLoader)
    # 将配置文件内容，写入 desired capabilities (被测对象的基本信息)
    caps = {}
    caps['platformName'] = config['platformName']
    caps['platformVersion'] = config['platformVersion']
    caps['deviceName'] = config['deviceName']
    caps['appPackage'] = config['appPackage']
    caps['appActivity'] = config['appActivity']
    caps['noReset'] = config['noReset']
    caps['app'] = config['app']
    # 处理中文问题
    caps['unicodeKeyboard'] = config['unicodeKeyboard']
    caps['resetKeyboard'] = config['resetKeyboard']
    # 解决安卓7.0 以上元素定位出Bug的配置项
    # caps['automationName'] = "uiautomator2"
    # 启动app
    driver = webdriver.Remote('http://'+str(config['ip'])+':'+str(config['port'])+'/wd/hub',caps)
    return driver