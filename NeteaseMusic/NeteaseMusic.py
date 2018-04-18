# 用于爬取网易云音乐某位歌手专辑页的所有专辑封面

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


class AlbumCover():

    def __init__(self):
        self.init_url = "http://music.163.com/#/artist/album?id=783150&limit=36&offset=0"  # 请求网址
        self.folder_path = "E:\PycharmProjects\WebCrawler\\NeteaseMusic\\albumcover"  # 想要存放的文件目录

    # limit参数是限制一个页面加载专辑的个数
    # offset参数是前面过滤多少个专辑，初始一页12个专辑，offset = 0，则第二页是offset = 12，第三页offset = 24，以此类推

    def save_img(self, url, file_name):  # 保存图片
        print('开始请求图片地址...')
        img = self.request(url)
        print('开始保存图片...')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名叫', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已存在，不再创建')
            return False

    def get_files(self, path):  # 获取文件夹中的文件名称列表
        pic_names = os.listdir(path)
        return pic_names

    def get_pic(self):
        print("Start!")
        driver = webdriver.PhantomJS()
        driver.get(self.init_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        self.mkdir(self.folder_path)  # 创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹

        file_names = self.get_files(self.folder_path)  # 获取文件夹中的所有文件名，类型是list

        all_li = BeautifulSoup(html, 'lxml').find('ul', id='m-song-module').find_all('li')
        # print(type(all_li))

        for li in all_li:
            album_img = li.find('img')['src']  # li中找到img标签的src属性值，即封面图片URL
            album_name = li.find('p', class_='dec dec-1 f-thide2 f-pre')['title']  # li中找到p标签的title属性值，即专辑名称
            album_date = li.find('span', class_='s-fc3').get_text()  # li中找到span标签中的字符串，即发行日期

            # 样例http://p4.music.126.net/DME0lEX9oraFu3Y3gzBYYQ==/109951163203880810.jpg?param=120y120
            end_pos = album_img.index('?')
            album_img_url = album_img[:end_pos]  # Python切片，去除“?param=120y120”，取消120*120的图片大小限制

            photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
            print(album_img_url, photo_name)

            if photo_name in file_names:
                print('图片已经存在，不再重新下载')
            else:
                self.save_img(album_img_url, photo_name)


album_cover = AlbumCover()
album_cover.get_pic()
