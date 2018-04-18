# 测试Selenium模拟Chrome浏览器在网页上的浏览、输入、查询操作
# Selenium是一个自动化测试框架，它能模拟人工操作（如能在浏览器中点击按钮、在输入框中输入文本、自动填充表单、进行浏览器窗口的切换、对弹出窗口进行操作等）

# 不知为何无法在搜索框中自动输入并搜索 2018.4.17
# 今天打开项目不知为何上述问题解决了？？？ 2018.4.18
from selenium import webdriver  # 导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys

driver = webdriver.Chrome()  # 指定使用的浏览器，初始化webdriver
driver.get("http://www.python.org")  # 请求网页地址
assert "Python" in driver.title  # 看看Python关键字是否在网页title中，如果在则继续，如果不在，程序跳出。
elem = driver.find_element_by_name("q")  # 找到name为q的元素，这里是个搜索框
elem.clear()  # 清空搜索框中的内容
elem.send_keys("pycon")  # 在搜索框中输入pycon
elem.send_keys(Keys.RETURN)  # 相当于回车键，提交
assert "No results found." not in driver.page_source  # 如果当前页面文本中有“No results found.”则程序跳出
# driver.close()  # 关闭webdriver

# ChromeDriver启动Chrome浏览器后，地址栏只显示data;，说明chromeDriver版本不对，
# 需要下载对应版本的 webdriver，网址为：https://sites.google.com/a/chromium.org/chromedriver/downloads
