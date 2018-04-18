# 用于爬取Unsplash图片网站的图片，包含模拟网页下拉功能

from selenium import webdriver  # 导入Selenium
import requests
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块
import time


class Unsplash():

    def __init__(self):  # 类的初始化操作
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://unsplash.com'  # 要访问的网页地址
        self.folder_path = 'E:\PycharmProjects\WebCrawler\\Unsplash\pictures'  # 设置图片要存放的文件目录

    def get_pic(self):
        print('开始网页get请求')
        driver = webdriver.PhantomJS()  # 使用selenium通过PhantomJS来进行网络请求
        driver.get(self.web_url)
        self.scroll_down(driver=driver, times=3)  # 执行网页下拉到底部操作，执行3次

        print('开始获取所有img标签')
        all_img = BeautifulSoup(driver.page_source, 'lxml').find_all('img', class_='_2zEKz')  # 获取网页中的class为_2zEKz的所有img标签

        print('开始创建文件夹')
        is_new_folder = self.mkdir(self.folder_path)  # 创建文件夹，并判断是否是新创建
        print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹

        print("img标签的数量是：", len(all_img))  # 这里添加一个查询图片标签的数量，来检查我们下拉操作是否有误
        file_names = self.get_files(self.folder_path)  # 获取文件夹中的所有文件名，类型是list

        for a in all_img:  # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            img_str = a['src']  # a标签中完整的src字符串
            print('img标签的src内容是：', img_str)
            img_url = img_str

            # 截取url中网址后、参数前的字符串为图片名
            name_start_pos = img_url.index('.com/') + 5  # 通过找.com/的位置，来确定它之后的字符位置
            name_end_pos = img_url.index('?')
            img_name = img_url[name_start_pos: name_end_pos] + '.jpg'
            img_name = img_name.replace('/', '')  # 把图片名字中的斜杠都去掉

            if is_new_folder:
                self.save_img(img_url, img_name)  # 调用save_img方法来保存图片
            else:
                if img_name not in file_names:
                    self.save_img(img_url, img_name)  # 调用save_img方法来保存图片
                else:
                    print("该图片已经存在：", img_name, "，不再重新下载。")

    def save_img(self, url, file_name):  # 保存图片
        print('开始请求图片地址...')
        img = self.request(url)
        print('开始保存图片...')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):  # 返回网页的response
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False

    def scroll_down(self, driver, times):
        for i in range(times):
            print("开始执行第", str(i + 1), "次下拉操作...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行JavaScript实现网页下拉倒底部
            print("第", str(i + 1), "次下拉操作执行完毕！")
            print("第", str(i + 1), "次等待网页加载...")
            time.sleep(5)  # 等待5秒，页面加载出来再执行下拉操作

    def get_files(self, path):
        pic_names = os.listdir(path)
        return pic_names


picture = Unsplash()  # 创建类的实例
picture.get_pic()  # 执行类中的方法
