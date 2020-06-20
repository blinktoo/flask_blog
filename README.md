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
```
pip freeze > requirements.txt
```
3. 数据库迁移
```
创建迁移存储库:
flask db init
生成迁移脚本:
flask db migrate -m "add users table"
将迁移脚本应用到数据库中:
flask db upgrade
说明： flask db downgrade 命令可以回滚上次的迁移
```
## RESTful API设计
HTTP方法 | 资源URL | 说明
---|---|---
`GET` | `/api/users` | 返回所有用户的集合
`POST` | `/api/users` | 注册一个新用户
`GET` | `/api/users/<id>` | 返回一个用户
`PUT` | `/api/users/<id>` | 修改一个用户
`DELETE` | `/api/users/<id>` | 删除一个用户
## API认证
使用`Flask-HTTPAuth`
