### window上部署
1. 拉取下来之后，在`pycharm`上创建干净的虚拟环境
2. 在项目目录下使用
```
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
使用清华源拉取依赖，如果部分依赖拉取失败切换一下其他源试一下
```
阿里云 : http://mirrors.aliyun.com/pypi/simple/
中国科技大学 : https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣 : http://pypi.douban.com/simple
中国科学院 : http://pypi.mirrors.opencas.cn/simple/
清华大学 : https://pypi.tuna.tsinghua.edu.cn/simple/
```