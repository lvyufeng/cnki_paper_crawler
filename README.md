# CNKI论文数据爬虫
爬取专业内容知识，供数据集构造使用

由于初版仅使用了requests+bs4的简单抓取方式，不适合大规模爬取。现改为scrapy实现。

CNKI由于版权限制，开放部分仅为摘要和作者信息，全文HTML需要高校购买服务。

本项目仅为研究使用，若有侵权，请联系。

爬虫部署于 [Herokuapp](http://cqu-crawler.herokuapp.com/), 使用[scrapydweb](https://github.com/my8100/scrapydweb)项目框架，特此感谢。
