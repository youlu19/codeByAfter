## 爬虫初始

### 爬虫相关介绍

- 什么是爬虫?
  - 爬虫程序是需要充当B/S或者C/S架构中的客户端。
  - 爬虫程序需要模拟客户端进行请求发送，然后获取服务器端对应的相关数据。
  - 在B/S架构中爬虫程序模拟的就是浏览器。

- 提问：如果日后你的爬虫程序没有爬取到你想要的数据，why？
  - 爬虫程序模拟浏览器的力度不够。

- 爬虫在应用场景的分类?
  - 通用爬虫：可以将一个页面中所有的数据都爬取到。
  - 聚焦爬虫：建立在通用爬虫基础之上。可以将一张页面中局部、指定的数据进行抓取
  - 增量式爬虫：可以监测网站数据更新的情况。以便将最新更新出来的数据进行抓取

- 爬虫的矛与盾（重点）?
  - 反爬机制：作用在门户网站中，网站会指定出一些阻止爬虫程序进行数据爬取的机制。
  - 反反爬策略：作用在爬虫程序中，可以指定破解反爬机制的策略，这些策略就是反反爬策略。


### 爬虫合法性探究

- **爬虫作为一种计算机技术就决定了它的中立性，因此爬虫本身在法律上并不被禁止，但是利用爬虫技术获取数据这一行为是具有违法甚至是犯罪的风险的。**所谓具体问题具体分析，正如水果刀本身在法律上并不被禁止使用，但是用来捅人，就不被法律所容忍了。
- 或者我们可以这么理解：爬虫是用来批量获得网页上的公开信息的，也就是前端显示的数据信息。因此，既然本身就是公开信息，其实就像浏览器一样，浏览器解析并显示了页面内容，爬虫也是一样，只不过爬虫会批量下载而已，所以是合法的。不合法的情况就是配合爬虫，利用黑客技术攻击网站后台，窃取后台数据（比如用户数据等）。
- 举个例子：像谷歌这样的搜索引擎爬虫，每隔几天对全网的网页扫一遍，供大家查阅，各个被扫的网站大都很开心。这种就被定义为“善意爬虫”。但是像抢票软件这样的爬虫，对着 12306 每秒钟恨不得撸几万次，铁总并不觉得很开心，这种就被定义为“恶意爬虫”。
- **爬虫所带来风险主要体现在以下3个方面：**
  - 1、违反网站意愿，例如网站采取反爬措施后，强行突破其反爬措施；
  - 2、爬虫干扰了被访问网站的正常运营；
  - 3、爬虫抓取了受到法律保护的特定类型的数据或信息。
- **那么作为爬虫开发者，如何在使用爬虫时避免进局子的厄运呢？**
  - 1、在规避反爬虫措施的同时，需要优化自己的代码，避免干扰被访问网站的正常运行；
  - 2、在使用、传播抓取到的信息时，应审查所抓取的内容，如发现属于用户的个人信息、隐私或者他人的商业秘密的，应及时停止并删除。
- 总结：
  - 可以说在我们身边的网络上已经密密麻麻爬满了各种网络爬虫，它们善恶不同，各怀心思。而越是每个人切身利益所在的地方，就越是爬满了爬虫。**所以爬虫是趋利的，它们永远会向有利益的地方爬行。**技术本身是无罪的，问题往往出在人无限的欲望上。因此爬虫开发者的道德自持和企业经营者的良知才是避免触碰法律底线的根本所在。 

### requests基础操作  

- 基本介绍
  - reqeusts是用来进行网络请求的一个python模块，其作用可以使用程序模拟浏览器进行请求发送。

- 环境安装
  - pip install requests

- 编码流程
  - 指定url
  - 发起请求
  - 获取响应数据（想爬取的数据）
  - 持久化存储



### 案例应用

#### 东方财富首页数据爬取

- https://www.eastmoney.com/

- ```python
  import requests
  
  #1.指定url
  url = 'https://www.eastmoney.com/'
  
  #2.发起请求:根据指定的url进行请求发送。get函数会返回该请求的响应对象。
  response = requests.get(url)
  print("响应状态码:",response.status_code) #查看响应对象的响应状态码
  
  #3.获取响应数据
  page_text = response.text #返回字符串形式的响应数据
  
  #4.持久化存储
  with open('./caifu.html','w',encoding='utf-8') as fp:
      fp.write(page_text)
  
  print('数据爬取结束！')
  ```

​     发现：爬取的页面数据出现了中文乱码。

#### 中文乱码解决

- ```python
  import requests
  
  #1.指定url
  url = 'https://www.eastmoney.com/'
  
  #2.发起请求:根据指定的url进行请求发送。get函数会返回该请求的响应对象。
  response = requests.get(url)
  print("响应状态码:",response.status_code) #查看响应对象的响应状态码
  
  #设置响应数据的编码格式
  response.encoding = 'utf-8'  #gbk
  
  #3.获取响应数据
  page_text = response.text #返回字符串形式的响应数据
  
  
  #4.持久化存储
  with open('./caifu.html','w',encoding='utf-8') as fp:
      fp.write(page_text)
  
  print('数据爬取结束！')
  ```

#### 爬取51游戏中任何游戏对应的搜索结果页面数据

- url：https://www.51.com/

- ```python
  import requests
  
  game_title = input('enter a game key:')
  #字典需要存放请求携带的所有的请求参数
  params = {
      'q':game_title
  } #请求参数的数量和字典的键值对的数量保持一致
  
  #指定url
  url = 'https://game.51.com/search/action/game/'
  
  #发起请求:向指定的url携带了指定的请求参数进行的请求发送
  response = requests.get(url=url,params=params)
  
  #获取响应数据
  page_text = response.text
  
  #持久化存储
  with open('games.html','w',encoding='utf-8') as fp:
      fp.write(page_text)
  ```

#### 中国人事考试网（UA检测）

- url：http://www.cpta.com.cn/

  - 爬虫模拟浏览器主要是模拟请求参数和主要的请求头。
    - User-Agent:请求载体的身份标识。
      - 使用浏览器发请求，则请求载体就是浏览器
      - 使用爬虫程序发请求，则请求载体就是爬虫程序
  - 反爬机制：UA检测
    - 网站后台会检测请求的载体是不是浏览器，如果是则返回正常数据，不是则返回错误数据。
  - 反反爬机制：UA伪装
    - 将爬虫发起请求的User-Agent伪装成浏览器的身份。

- ```python
  import requests
  
  url = 'http://www.cpta.com.cn/'
  
  #User-Agent:请求载体（浏览器，爬虫程序）的身份表示
  header = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
  #伪装了浏览器的请求头
  response = requests.get(url=url,headers=header)
  
  page_text = response.text
  
  with open('kaoshi.html','w') as fp:
      fp.write(page_text)
  
  #程序模拟浏览器的力度不够
  ```

#### 中国人事考试网---站内搜索（post请求+请求参数）

- ```python
  import requests
  url = 'http://www.cpta.com.cn/category/search'
  param = {
      "keywords": "人力资源",
      "搜 索": "搜 索"
  }
  header = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
  #发起了post请求：通过data参数携带了请求参数
  response = requests.post(url=url,data=param,headers=header)
  
  page_text = response.text
  
  with open('renshi.html','w') as fp:
      fp.write(page_text)
  
  #通过抓包工具定位了指定的数据包：
      #提取：url，请求方式，请求参数，请求头信息
  ```

  

#### 智慧职教（动态加载数据爬取）**(重点)**

- 抓取智慧职教官网中的专业群板块下的所有数据

  - url : https://www.icve.com.cn/portal_new/course/course.html

- 测试：直接使用浏览器地址栏中的url，进行请求发送查看是否可以爬取到数据？

  - 不用写程序，基于抓包工具测试观察即可。

- 经过测试发现，我们爬取到的数据并没有包含想要的数据，why？

- 动态加载数据：

  - 在一个网页中看到的数据，并不一定是通过浏览器地址栏中的url发起请求请求到的。如果请求不到，一定是基于其他的请求请求到的数据。
  - 动态加载数据值的就是：
    - 不是直接通过浏览器地址栏的url请求到的数据，这些数据叫做动态加载数据。
  - 如何获取动态加载数据？
    - 确定动态加载的数据是基于哪一个数据包请求到的？
    - 数据包数据的全局搜索：
      - 点击抓包工具中任何一个数据包
      - control+f进行全局搜索（弹出全局搜索框）
        - 目的：定位动态加载数据是在哪一个数据包中
      - 定位到动态加载数据对应的数据包，模拟该数据包进行请求发送即可：
        - 从数据包中提取出：
          - url
          - 请求参数   

  注意：请求头中需要携带Referer。（体现模拟浏览器的力度）

- ```python
  #爬取第一页的数据
  import requests
  headers = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      #Referer啥意思？不讲，后面单独讲
      'Referer':'https://www.icve.com.cn/portal_new/course/course.html?keyvalue=%E6%97%85%E6%B8%B8'
  }
  
  url = 'https://www.icve.com.cn/portal/course/getNewCourseInfo'
  data = {
      "kczy":"",
      "order":"",
      "printstate":"",
      "keyvalue": "旅游"
  }
  response = requests.post(url=url,headers=headers,data=data)
  
  #获取响应数据
  #json()可以将响应数据进行反序列化
  page_text = response.json()
  
  for dic in page_text['list']:
      title = dic['Title']
      name = dic['TeacherDisplayname']
      print(title,name)
  ```
  
  ```python
  #多页数据的爬取
  import requests
  headers = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      #Referer啥意思？不讲，后面单独讲
      'Referer':'https://www.icve.com.cn/portal_new/course/course.html?keyvalue=%E6%97%85%E6%B8%B8'
  }
  
  for page in range(1,5):
      url = 'https://www.icve.com.cn/portal/course/getNewCourseInfo?page=%d'%page
      data = {
          "kczy":"",
          "order":"",
          "printstate":"",
          "keyvalue": "旅游"
      }
      response = requests.post(url=url,headers=headers,data=data)
  
      #获取响应数据
      #json()可以将响应数据进行反序列化
      page_text = response.json()
  
      for dic in page_text['list']:
          title = dic['Title']
          name = dic['TeacherDisplayname']
          print(title,name)
  ```

#### 图片数据爬取

- ```python
  #方式1：
  import requests
  url = 'https://img0.baidu.com/it/u=540025525,3089532369&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'
  response = requests.get(url=url)
  #content获取二进制形式的响应数据
  img_data = response.content
  with open('1.jpg','wb') as fp:
      fp.write(img_data)
  ```

- ```python
  #方式2
  from urllib.request import urlretrieve
  #图片地址
  img_url = 'https://img0.baidu.com/it/u=4271728134,3217174685&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=500'
  #参数1：图片地址
  #参数2：图片存储路径
  #urlretrieve可以根据图片地址将图片数据请求到直接存储到参数2表示的图片存储路径中
  urlretrieve(img_url,'1.jpg')
  ```
  
- 爬取图片的时候需要做UA伪装使用方式1，否则使用方式2

#### 作业 (不收，不检查，完全自愿)

小试牛刀：

- url：https://www.xiachufang.com/
- 实现爬取下厨房网站中任意菜谱搜索结果数据爬取

小试牛刀：

- url ：https://sogou.com/
- 爬取任意关键字对应的搜索页面

肯德基（POST请求、动态加载数据、UA检测）

- http://www.kfc.com.cn/kfccda/storelist/index.aspx

  - 将餐厅的位置信息进行数据爬取



