# PixivSpider
这是一个使用selenium模拟浏览器爬取p站(pixiv)图片的小脚本,支持登录,支持搜索,支持单图和多图下载(随便写写练练手)

项目使用pycharm构建,在.py文件中配置了将图片保存到项目下的pictures目录里,整个项目结构只有两个文件,一个pictures,一个.py


使用之前,你可能需要为你的python解释器安装selenium,six,以及chromedriver
此外需要修改.py中的user与passwd![image](https://user-images.githubusercontent.com/54017952/218311127-0ce9136b-5523-4423-8d0d-4226ada31649.png)


```shell
pip install selenium
pip install six
```
这是chromedriver的地址:http://chromedriver.storage.googleapis.com/index.html
记得将chromedriver添加到环境变量的目录中
