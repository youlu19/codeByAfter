# day04 django进阶-知识点

今日概要：

- 模板
- 中间件
- ORM操作（pymysql + SQL语句）
- session和cookie
- 缓存（很多种方式）



## 内容回顾

- 请求周期

  - 路由系统

    - 最基本路由关系
    - 动态路由（含正则）
    - 路由分发不同的app中 + include + 本质 + name + namespace

  - 视图

    - 类和函数（FBV和CBV）

    - 参数 request

      - 请求数据
      - 自定义数据

    - 响应

      ```
      HttpResponse/JsonResponse/render/redirect
      return HttpResponse("...")
      
      响应头
      obj = HttpResponse("...")
      obj['xxxxx'] = "值"
      return obj
      ```

- 其他知识

  - 虚拟环境

  - 纯净版项目，内置app功能去掉。

  - 多app，嵌套到apps目录。

  - pycharm创建django项目 + 虚拟环境

    - 最新的django项目
    - 低版本（环境+项目+django文件模板）

  - settings配置

    ```
    django默认settings [先加载] 500
    项目目录settings    [后加载] 20
    ```

  - 静态资源

    - 静态文件，项目必备【项目根目录，每个app目录下static - app注册顺序】
    - 媒体文件，用户上传





## 1.模板



### 1.1 寻找html模板

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

优先去项目根目录  > 每个已注册的app的templates目录找。



如何选择：

- 简单的项目，模板都放在根目录。
- 复杂的项目，模板放在各自的app中，公共部分放在templates目录。



扩展：修改内置app的模板也是同样的套路。





### 1.2 模板处理的本质

渲染完成后，生成了字符串，再返回给浏览器。

![image-20220703100004360](assets/image-20220703100004360.png)

![image-20220703100634467](assets/image-20220703100634467.png)



### 1.3 常用语法

![image-20220703104019949](assets/image-20220703104019949.png)





### 1.4 内置函数

在django模板语法中提供了内置函数让我们来。

![image-20220703104857782](assets/image-20220703104857782.png)



### 1.5 自定义模板功能

![image-20220703110604253](assets/image-20220703110604253.png)



三种方式：

-  filter

  ```
  - 数据处理，参数：1~2个
  - 数据处理，if条件
  ```

-  simple_tag

  ```
  参数无限制 & 返回文本
  ```

-  inclusion_tag

  ```
  参数无限制 & HTML片段
  ```



需求来了：根据用户权限不同显示不同的菜单。

![image-20220703112043922](assets/image-20220703112043922.png)



### 1.6 继承和母版

![image-20220703114930894](assets/image-20220703114930894.png)

![image-20220703114941168](assets/image-20220703114941168.png)



### 1.7 模板的导入

![image-20220703115519438](assets/image-20220703115519438.png)





















## 2.django中间件

![image-20220703140649928](assets/image-20220703140649928.png)

- 类
- 定义方法
- 注册

### 2.1 原始方式

![image-20220703141259948](assets/image-20220703141259948.png)

![image-20220703141313488](assets/image-20220703141313488.png)



### 2.2 MiddlewareMixin（建议）

![image-20220703142923194](assets/image-20220703142923194.png)

![image-20220703142936794](assets/image-20220703142936794.png)

注意：django1版本。



源码：

- 面向对象

  ```python
  class MyMd(object):
      def __init__(self....):
          pass
      
      def __call__(self,....):
          pass
          
  django内部默认执行call方法，传入参数。
  ```

- 反射

  ```python
  class MyMd(object):
      def __init__(self....):
          pass
      
      def __call__(self,....):
          if hasattr(self,'process_request'):
              response = self.process_request(request)
  		...
       
  django内部默认执行call方法，传入参数。
  ```

  ```python
  class MiddlewareMixin:
      def __init__(self, get_response=None):
          self.get_response = get_response
          
      def __call__(self, request):
          response = None
          if hasattr(self, 'process_request'):
              response = self.process_request(request)
          response = response or self.get_response(request)
          if hasattr(self, 'process_response'):
              response = self.process_response(request, response)
          return response
      
      
  class MyMd(MiddlewareMixin):
      
      def process_request(self,request):
          ...
      
      def process_response(self,request, response):
          ...
      
  django内部默认执行call方法，传入参数。
  ```





![image-20220703145219921](assets/image-20220703145219921.png)

![image-20220703145158733](assets/image-20220703145158733.png)



![image-20220703145210733](assets/image-20220703145210733.png)



**疑问**：prcess_request的执行时，是否已执行了路由匹配？

request.resolver_match



**注意**：process_view是在django中源码中写死了。

![image-20220703151639813](assets/image-20220703151639813.png)

### 2.3 其他

![image-20220703153559256](assets/image-20220703153559256.png)

![image-20220703153616241](assets/image-20220703153616241.png)







### 小结

- 定义中间类
- 类方法
  - process_request
  - process_view
  - process_reponse
  - process_exception，视图函数出现异常，自定义异常页面。
  - process_template_response，视图函数返回`TemplateResponse`对象  or  对象中含有.render方法。

![image-20220703155414569](assets/image-20220703155414569.png)





## 3.ORM操作

orm，关系对象映射，本质翻译的。

![image-20220703155844071](assets/image-20220703155844071.png)



### 3.1 表结构

实现：创建表、修改表、删除表。

在app中的models.py中按照规则编写类    ===> 表结构。

- 编写类

  ```python
  from django.db import models
  
  
  class UserInfo(models.Model):
      name = models.CharField(max_length=16)
      age = models.IntegerField()
  ```

- 注册app

  ```python
  INSTALLED_APPS = [
      # 'django.contrib.admin',
      # 'django.contrib.auth',
      # 'django.contrib.contenttypes',
      # 'django.contrib.sessions',
      # 'django.contrib.messages',
      'django.contrib.staticfiles',
      'apps.app01.apps.App01Config',
      'apps.app02.apps.App02Config',
  ]
  ```

- 命令，django根据models中类生成一个 `对数据库操作的配置文件` => `migrations`

  ```
  python manage.py makemigrations
  ```

  ![image-20220703160914596](assets/image-20220703160914596.png)

- 命令，读取已经注册么给app中的migrations目录将配置文件  -> 转换成：生成表，修改表 SQL -> 连接数据库去运行。

  ```python
  python manage.py migrate
  ```

  - 那个数据库？
  - 数据库账户和密码?

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
  ```

  ![image-20220703162050698](assets/image-20220703162050698.png)



**常见问题**：请不要再手动去修改数据的表结构 + 时刻保证 ORM和数据表是对应。



#### 3.1.1 常见字段和参数

- 字段

  ```
  CharField
  
  SmallIntegerField
  IntegerField
  BigIntegerField
  
  DateField
  DateTimeField
  
  BooleanField  -> 其实数据库不支持真假，根据SmallIntegerField创造出来出来。 0  1
  
  DecimalField  -> 精确的小数
  ```

- 参数

  ```python
  name = models.CharField(verbose_name="姓名", max_length=16)
  name = models.CharField(verbose_name="姓名", max_length=16, default="哈哈哈")
  
  # 经常查询，速度快（MySQL，https://www.bilibili.com/video/BV15R4y1b7y9）
  name = models.CharField(verbose_name="姓名", max_length=16, default="哈哈哈", null=True, blank=True, db_index=True)
  email = models.CharField(verbose_name="姓名", max_length=16, default="哈哈哈", null=True, blank=True, unique=True)
  
  # 在数据库存储时只能是：sh、bj （上海、北京一般用于页面显示中文）
  code = models.CharField(verbose_name="姓名", max_length=16, choices=(("sh", "上海"), ("bj", "北京")),default="sh")
  ```

  ```python
  # 不用 max_length=16
  count = models.IntegerField(verbose_name="数量", default=1, null=True, blank=True, unique=True)
  code = models.IntegerField(verbose_name="性别",choices=((1, "男"), (2, "女")),default=1)
  ```

  ```python
  register_date = models.DateField(verbose_name="注册时间", auto_now=True)
  ```

  ```python
  amount = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2)
  ```



示例：

```python
from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16, db_index=True)
    age = models.PositiveIntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=128, unique=True)
    amount = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    register_date = models.DateField(verbose_name="注册时间", auto_now=True)


class Goods(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    # detail = models.CharField(verbose_name="详细信息", max_length=255)
    detail = models.TextField(verbose_name="详细信息")
    price = models.PositiveIntegerField(verbose_name="价格")
    count = models.PositiveBigIntegerField(verbose_name="库存", default=0)
```



#### 3.1.2 表关系

![image-20220703173556969](assets/image-20220703173556969.png)

![image-20220703174433414](assets/image-20220703174433414.png)





![image-20220703175051329](assets/image-20220703175051329.png)

![image-20220703175312854](assets/image-20220703175312854.png)



![image-20220703175556444](assets/image-20220703175556444.png)

注意：ManyToManyField生成的表字段只能id/bid/gid



#### 小结

设计自己项目的业务时，理清楚表与表之间的关系。

强调：设计项目表结构：表名和字段都不要拼音。





### 3.2 数据

实现：增删改查。







## 任务

- 知识点
- 自己的项目设计表结构，自己设计。
  - 项目功能描述
  - 表结构
    - 设计图（提交）
    - ORM类（主要）



提交形式：zip包 -> markdown编写。

---

```
下节预告：
	orm数据操作、cookie和session、缓存、刷票平台（表结构设计）、用户管理、用户+权限菜单
```







































