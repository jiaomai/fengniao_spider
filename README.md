#### 功能：

对企业信息进行爬取

#### 使用方法：

使用python3调用

示例：

`python fengniao_spider.py -k 石油`

![image-20230607164612067](https://cdn.jsdelivr.net/gh/jiaomai/MD-gallery/img/image-20230607164612067.png)

-k       指定查询关键词（也可以是具体的公司名，人名），必填

-p      查询数量，默认是10

-f       指定导出的文件，不支持和批量查询同时用

-r      指定批量查询的文件

`python fengniao_spider.py -k 石油 -f result`

![image-20230607170119304](https://cdn.jsdelivr.net/gh/jiaomai/MD-gallery/img/image-20230607170119304.png)

`python fengniao_spider.py -r 1111.txt`

![image-20230607170220139](https://cdn.jsdelivr.net/gh/jiaomai/MD-gallery/img/image-20230607170220139.png)

![image-20230607170630608](https://cdn.jsdelivr.net/gh/jiaomai/MD-gallery/img/image-20230607170630608.png)

官网：

[风鸟企业查询 (riskbird.com)](https://m.riskbird.com/h5/pages/user/vip/share?inviteCode=D0193D9A4038238B)