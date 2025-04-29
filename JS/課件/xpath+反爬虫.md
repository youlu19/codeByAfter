

### 上次直播作业

- 下厨房的菜谱搜索(多个请求参数)

  - 通过抓包工具的分析发现，搜索菜谱的数据包有两个请求参数：

    - keyword：搜索的关键字
    - cat：1001固定形式

  - ```python
    import requests
    
    #请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    title = input('请输入菜名：')
    params = {
        'keyword':title,
        'cat':'1001'
    }
    #1.指定url
    url = 'https://www.xiachufang.com/search/'
    
    #2.发起请求
    response = requests.get(url=url,headers=headers,params=params)
    #处理乱码
    response.encoding = 'utf-8' #gbk
    
    #3.获取响应数据
    page_text = response.text
    
    #4.持久化存储
    fileName = title + '.html'
    with open(fileName,'w') as fp:
        fp.write(page_text)
    
    ```

- 肯德基

  - http://www.kfc.com.cn/kfccda/index.aspx

    - 将餐厅的位置信息进行数据爬取

    - ```python
      import requests
      head = { #存放需要伪装的头信息
          'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
      }
      #post请求的请求参数
      data = {
          "cname": "",
          "pid": "",
          "keyword": "天津",
          "pageIndex": "1",
          "pageSize": "10",
      }
      #在抓包工具中：Form Data存放的是post请求的请求参数，而Query String中存放的是get请求的请求参数
      url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
      #在post请求中，处理请求参数的是data这个参数不是params
      response = requests.post(url=url,headers=head,data=data)
      #将响应数据进行反序列化
      page_text = response.json()
      for dic in page_text['Table1']:
          name = dic['storeName']
          addr = dic['addressDetail']
          print(name,addr)
      ```

      


### 数据解析

#### 何为数据解析

- 概念：可以将爬取到的数据中指定的数据进行单独提取。
- 作用：实现聚焦爬虫。
- 数据解析通用原理：
  - 在一张页面中，想要解析的数据是存在于相关的html的标签中。
  - 可以先将指定的标签进行定位，然后可以将该标签中展示的数据进行提取。

- 聚焦爬虫编码流程:
  - 指定url
  - 发起请求
  - 获取页面源码数据
  - 数据解析
  - 持久化存储

- python中可以实现数据解析的技术：
  - 正则表达式（复杂度高）
  - bs4（python独有，学习成本较低）
  - xpath（通用性最强，最重要）
  - pyquery（css语句）



#### 数据解析的主流策略

- 具体解析的操作：

  - 在当前目录下新建一个test.html文件，然后将下述内容拷贝到该文件中

    - ```html
      <html lang="en">
      <head>
      	<meta charset="UTF-8" />
      	<title>测试bs4</title>
      </head>
      <body>
      	<div>
      		<p>百里守约</p>
      	</div>
      	<div class="song">
      		<p>李清照</p>
      		<p>王安石</p>
      		<p>苏轼</p>
      		<p>柳宗元</p>
      		<a href="http://www.song.com/" title="赵匡胤" target="_self">
      			<span>this is span</span>
      		宋朝是最强大的王朝，不是军队的强大，而是经济很强大，国民都很有钱</a>
      		<a href="" class="du">总为浮云能蔽日,长安不见使人愁</a>
      		<img src="http://www.baidu.com/meinv.jpg" alt="" />
      	</div>
      	<div class="tang">
      		<ul>
      			<li><a href="http://www.baidu.com" title="qing">清明时节雨纷纷,路上行人欲断魂,借问酒家何处有,牧童遥指杏花村</a></li>
      			<li><a href="http://www.163.com" title="qin">秦时明月汉时关,万里长征人未还,但使龙城飞将在,不教胡马度阴山</a></li>
      			<li><a href="http://www.126.com" alt="qi">岐王宅里寻常见,崔九堂前几度闻,正是江南好风景,落花时节又逢君</a></li>
      			<li><a href="http://www.sina.com" class="du">杜甫</a></li>
      			<li><a href="http://www.dudu.com" class="du">杜牧</a></li>
      			<li><b>杜小月</b></li>
      			<li><i>度蜜月</i></li>
      			<li><a href="http://www.haha.com" id="feng">凤凰台上凤凰游,凤去台空江自流,吴宫花草埋幽径,晋代衣冠成古丘</a></li>
      		</ul>
      	</div>
      </body>
      </html>
      ```


#### xpath（重点）

- 环境安装：

  - pip install lxml

- xpath解析的编码流程:

  - 创建一个etree类型的对象，把被解析的数据加载到该对象中
  - 调用etree对象中xpath函数结合不同形式的xpath表达式进行标签定位和数据的提取

- xpath表达式如何理解？

- ```python
  from lxml import etree
  #1.创建一个etree的工具对象，然后把即将被解析的页面源码数据加载到该对象中
  tree = etree.parse('test.html')
  #2.调用etree对象的xpath函数然后结合着不用形式的xpath表达式进行标签定位和数据提取
  #xpath函数返回的是列表，列表中存储的是满足定位要求的所有标签
  #/html/head/title定位到html下面的head下面的title标签
  title_tag = tree.xpath('/html/head/title')
  #//title在页面源码中定位到所有的title标签
  title_tag = tree.xpath('//title')
  #属性定位
      #定位到所有的div标签
  div_tags = tree.xpath('//div')
      #定位到class属性值为song的div标签 //tagName[@attrName='value']
  div_tag = tree.xpath('//div[@class="song"]')
  #索引定位://tag[index]
      #注意：索引是从1开始的
  div_tag = tree.xpath('//div[1]')
  #层级定位
      # /表示一个层级  //表示多个层级
  a_list = tree.xpath('//div[@class="tang"]/ul/li/a')
  a_list = tree.xpath('//div[@class="tang"]//a')
  
  #数据提取
      #1.提取标签中的文本内容:/text()取直系文本  //text()取所有文本
  a_content = tree.xpath('//a[@id="feng"]/text()')[0]
  div_content = tree.xpath('//div[@class="song"]//text()')
      #2.提取标签的属性值：//tag/@attrName
  img_src = tree.xpath('//img/@src')[0]
  print(img_src)
  ```


案例应用：碧血剑文本爬取

- url：https://bixuejian.5000yan.com/

- 需求：将每一个章节的标题和内容进行爬取然后存储到文件中

  ```python
  #首页：章节名称，章节详情页的连接
  #详情页：章节内容
  
  import requests
  
  from lxml import etree
  #存储小说文件的文件夹名称
  dir_name = 'xiaoshuoLib'
  
  headers = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
  }
  
  main_url = 'https://bixuejian.5000yan.com/'
  response = requests.get(url=main_url,headers=headers)
  response.encoding = 'utf-8'
  page_text = response.text
  
  #解析首页
  tree = etree.HTML(page_text)
  a_alist = tree.xpath('/html/body/div[2]/div/div[1]/div[3]/ul/li/a')
  
  for a in a_alist:
      #局部解析
      title = a.xpath('./text()')[0]
      detail_url = a.xpath('./@href')[0]
      detail_response = requests.get(url=detail_url,headers=headers)
      detail_response.encoding = 'utf-8'
      detail_page_text = detail_response.text
      tree = etree.HTML(detail_page_text)
      content_list = tree.xpath('/html/body/div[2]/div/div[1]/div[3]/div[4]//text()')
      content = ''.join(content_list)
      with open('./xiaoshuoLib/'+title+'.txt','w',encoding='utf-8') as fp:
          fp.write(title+'\n'+content)
          print(title,":章节内容爬取保存成功！")
  
  ```

简历模版下载：https://sc.chinaz.com/jianli/free.html

  - 下载当前页所有的建立模板

    - 简历名称+简历的下载链接

    - 根据简历的下载链接 下载简历文件

    - 根据下载地址下载的压缩包，压缩包是二进制的数据

      ```python
      
      
      import requests
      from time import sleep
      from lxml import etree
      dir_name = 'jianliLib'
      
      headers = {
          'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
      }
      for page in range(1,3):
          if page == 1:
              main_url = 'https://sc.chinaz.com/jianli/free.html'
          else:
              main_url = 'https://sc.chinaz.com/jianli/free_%d.html'%page
      
          response = requests.get(url=main_url,headers=headers)
          response.encoding = 'utf-8'
          page_text = response.text
          tree = etree.HTML(page_text)
          div_list = tree.xpath('//*[@id="container"]/div')
          for div in div_list:
              sleep(0.5)
              detail_url = div.xpath('./p/a/@href')[0]
              title =  div.xpath('./p/a/text()')[0]
      
              detail_page_text = requests.get(detail_url,headers=headers).text
              tree = etree.HTML(detail_page_text)
              #解析到了简历的下载链接
              down_load_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
              data = requests.get(down_load_url,headers=headers).content
              with open('jianliLib/'+title+'.rar','wb') as fp:
                  fp.write(data)
                  print(title,'保存下载成功！')
      
      ```

- 图片懒加载：

  - url：https://sc.chinaz.com/tupian/meinvtupian.html
    - 爬取上述链接中所有的图片数据
  - 主要是应用在展示图片的网页中的一种技术，该技术是指当网页刷新后，先加载局部的几张图片数据即可，随着用户滑动滚轮，当图片被显示在浏览器的可视化区域范围的话，在动态将其图片请求加载出来即可。（图片数据是动态加载出来）。
  - 如何实现图片懒加载/动态加载？
    - 使用img标签的伪属性（指的是自定义的一种属性）。在网页中，为了防止图片马上加载出来，则在img标签中可以使用一种伪属性来存储图片的链接，而不是使用真正的src属性值来存储图片链接。（图片链接一旦给了src属性，则图片会被立即加载出来）。只有当图片被滑动到浏览器可视化区域范围的时候，在通过js将img的伪属性修改为真正的src属性，则图片就会被加载出来。
  - 如何爬取图片懒加载的图片数据？
    - 只需要在解析图片的时候，定位伪属性的属性值即可
    
    ```python
    import requests
    from time import sleep
    from lxml import etree
    dir_name = 'imgLib'
    
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }
    for page in range(1,3):
        if page == 1:
            url = 'https://sc.chinaz.com/tupian/meinvtupian.html'
        else:
            url = 'https://sc.chinaz.com/tupian/meinvtupian_%d.html'%page
    
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        page_text = response.text
    
        tree = etree.HTML(page_text)
        #解析图片地址
        div_list = tree.xpath('/html/body/div[3]/div[2]/div')
    
        for div in div_list:
            img_src = "https:"+div.xpath('./img/@data-original')[0]
            title = div.xpath('./div/a/text()')[0]+'.jpg'
            #对图片链接请求
            img_data = requests.get(img_src,headers=headers).content
            with open('imgLibs/'+title,'wb') as fp:
                fp.write(img_data)
            print(title,'保存下载成功！')
    
    
    ```
    
    

