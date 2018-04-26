# 使用Chrome插件xpath helper找到元素的完整xpath（Chrome自带的只能找到相对xpath）
# 再使用selenium模拟点击操作

from selenium import webdriver  # 导入Selenium的webdriver
import time

driver = webdriver.Chrome()  # 指定使用的浏览器，初始化webdriver
driver.get("http://music.163.com/#/playlist?id=93675032")  # 请求网页地址（网易云音乐首页）
time.sleep(1)

xpath = "/html/body/div[@id='g-topbar']/div[@class='m-top']/div[@class='wrap f-cb']/h1[@class='logo']/a"  # 网易云音乐网页左上角的logo
element = driver.find_element_by_xpath(xpath)  # 通过xpath寻找
element.click()
