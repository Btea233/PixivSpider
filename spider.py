from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from six.moves import urllib
import time


purl = "https://www.pixiv.net/"
# 模拟登录
browser = webdriver.Chrome()
browser.get(purl)
login1 = browser.find_element_by_class_name("signup-form__submit--login")
login1.click()

user = '2406634977@qq.com'
passwd = 'lxlwsadlxl'

user_class = browser.find_element_by_class_name("degQSE")
passwd_class = browser.find_element_by_class_name("hfoSmp")
login2 = browser.find_element_by_class_name("jvCTkj")

user_class.send_keys(user)
passwd_class.send_keys(passwd)
login2.click()

# 模拟搜索
time.sleep(10)
search = browser.find_element_by_tag_name("input")
# browser.find_element_by_partial_link_text("搜索作品")
key = "归终"
key = input('请输入爬取关键字:')
search.send_keys(key)
search.send_keys(Keys.ENTER)

# 模拟下载
time.sleep(10)

photo_class_li = browser.find_element_by_class_name("krFoBL").find_elements_by_tag_name("a")
hrefs=[]
res_href=[]
num=1
print("正在获取链接......")
#获取所有a标签中的链接
for href in photo_class_li:
    hrefs.append(href.get_attribute("href"))
#过滤其中重复的与作者的链接
for href in hrefs:
    if num>60:
        break
    res_href.append(hrefs[num])
    num+=4
print(photo_class_li)
print("搜索到li,开始逐个进入")
for href in res_href:
    time.sleep(3)
    # print("当前进入到:",end="")
    print("当前爬取的图片地址是:"+href)
    browser.get(href)
    # picture.click()
    time.sleep(4)
    #多图页面的标志是存在"查看全部"这个标签,点击它就可以展开了
    try:
        browser.find_element_by_class_name("wEKy")
        browser.find_element_by_class_name("wEKy").click()
        print("采取多图")
        print("加载多图中...请稍等")
        time.sleep(10)
        pictures = browser.find_element_by_class_name("beQeCv").find_elements_by_tag_name("a")
        for p in pictures:
            pnum=1
            p.click()
            ture_temp = browser.find_element_by_class_name("cKLKGN").find_element_by_tag_name("img")
            url_temp=ture_temp.get_attribute("src")
            # 添加请求头
            opener = urllib.request.build_opener()
            opener.addheaders = [('Referer', "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=60541651")]
            urllib.request.install_opener(opener)
            # 请求下载
            urllib.request.urlretrieve(url_temp, f'./pictures/{pnum}+{url_temp.split("/")[-1]}')
            pnum=pnum+1
            ture_temp.click()
    except:
        print("采取单图")
        #单图
        true_picture_class = browser.find_element_by_class_name("beQeCv").find_element_by_tag_name("a")
        true_picture_class.click()
        true_picture = browser.find_element_by_class_name("cKLKGN").find_element_by_tag_name("img")
        #查询src地址
        url = true_picture.get_attribute("src")
        #添加请求头
        opener = urllib.request.build_opener()
        opener.addheaders = [('Referer', "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=60541651")]
        urllib.request.install_opener(opener)
        #请求下载
        urllib.request.urlretrieve(url, f'./pictures/{url.split("/")[-1]}')
        browser.back()











