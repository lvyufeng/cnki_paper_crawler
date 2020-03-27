# CNKI论文数据爬虫
爬取专业内容知识，供数据集构造使用

由于初版仅使用了requests+bs4的简单抓取方式，不适合大规模爬取。现改为scrapy实现。

CNKI由于版权限制，开放部分仅为摘要和作者信息，全文HTML需要高校购买服务。

本项目仅为研究使用，若有侵权，请联系。

---
## 爬取刊物

1. JSJY: 计算机应用
1. JSGG: 计算机工程与应用
1. WJFZ: 计算机技术与发展
1. JSJA: 计算机科学
1. KXTS: 计算机科学与探索
1. SJSJ: 计算机工程与设计
1. RJXB: 软件学报
1. JFYZ: 计算机研究与发展
1. JSJF: 计算机辅助设计与图形学学报
1. JSJX: 计算机学报
1. XXWX: 小型微型计算机系统
1. JSJK: 计算机工程与科学

---

爬虫部署于 [Herokuapp](http://cqu-crawler.herokuapp.com/), 使用[scrapydweb](https://github.com/my8100/scrapydweb)项目框架，特此感谢。
