import scrapy


class itemSpider(scrapy.Spider):
    name = 'listSpider'

    start_urls = [
        'https://jobs.51job.com/gaojiyingjian/p1/',
        'https://jobs.51job.com/yingjian/p1/',
        'https://jobs.51job.com/gaojiruanjian/p1/',
        'https://jobs.51job.com/ruanjian/p1/',
        'https://jobs.51job.com/ruanjiansheji/p1/',
        'https://jobs.51job.com/suanfagongchengshi/p1/',
        'https://jobs.51job.com/fangzhenyingyong/p1/',
        'https://jobs.51job.com/erp-shishi/p1/',
        'https://jobs.51job.com/erp-jishukaifa/p1/',
        'https://jobs.51job.com/xuqiugongchengshi/p1/',
        'https://jobs.51job.com/xitongjicheng/p1/',
        'https://jobs.51job.com/xitongfenxi/p1/',
        'https://jobs.51job.com/xitong/p1/',
        'https://jobs.51job.com/xitongjiagou/p1/',
        'https://jobs.51job.com/shujukuguanli/p1/',
        'https://jobs.51job.com/jisuanjifuzhusheji/p1/',
        'https://jobs.51job.com/hulianwangruanjian/p1/',
        'https://jobs.51job.com/yuyinshipintuxingkaifa/p1/',
        'https://jobs.51job.com/duomeitiyouxikaifa/p1/',
        'https://jobs.51job.com/shoujiyingyongkaifa/p1/',
        'https://jobs.51job.com/wangzhanyunyingzongjian/p1/',
        'https://jobs.51job.com/wangzhanyunyingjingli/p1/',
        'https://jobs.51job.com/wangzhanyunying/p1/',
        'https://jobs.51job.com/chanpinzongjian/p1/',
        'https://jobs.51job.com/chanpinjingli/p1/',
        'https://jobs.51job.com/chanpinzhuanyuan/p1/',
        'https://jobs.51job.com/seo/p1/',
        'https://jobs.51job.com/wangluotuiguangzongjian/p1/',
        'https://jobs.51job.com/wangluotuiguangjingli/p1/',
        'https://jobs.51job.com/wangluotuiguangzhuanyuan/p1/',
        'https://jobs.51job.com/xinmeitiyunying/p1/',
        'https://jobs.51job.com/dianzishangwuzongjian/p1/',
        'https://jobs.51job.com/dianzishangwujingli/p1/',
        'https://jobs.51job.com/dianzishangwuzhuanyuan/p1/',
        'https://jobs.51job.com/wangluogongcheng/p1/',
        'https://jobs.51job.com/ui-sheji/p1/',
        'https://jobs.51job.com/yonghutiyansheji/p1/',
        'https://jobs.51job.com/dashujukaifa/p1/',
        'https://jobs.51job.com/qianduankaifa/p1/',
        'https://jobs.51job.com/wangzhanjiagousheji/p1/',
        'https://jobs.51job.com/wangzhanweihu/p1/',
        'https://jobs.51job.com/xitongwangluoguanli/p1/',
        'https://jobs.51job.com/wangzhancehua/p1/',
        'https://jobs.51job.com/wangyesheji/p1/',
        'https://jobs.51job.com/jiaobenkaifa/p1/',
        'https://jobs.51job.com/youxicehua/p1/',
        'https://jobs.51job.com/youxijiemian/p1/',
        'https://jobs.51job.com/flashsheji/p1/',
        'https://jobs.51job.com/yinxiaoshejishi/p1/',
        'https://jobs.51job.com/wangluoxinxianquan/p1/',
        'https://jobs.51job.com/cto-shouxijishuzhixing/p1/',
        'https://jobs.51job.com/jishuzongjian/p1/',
        'https://jobs.51job.com/xinxijishujingli/p1/',
        'https://jobs.51job.com/xinxijishuzhuanyuan/p1/',
        'https://jobs.51job.com/itxiangmuzongjian/p1/',
        'https://jobs.51job.com/itxiangmujingli/p1/',
        'https://jobs.51job.com/xiangmuzhuguan/p1/',
        'https://jobs.51job.com/xiangmuzhixing/p1/',
        'https://jobs.51job.com/weihujingli/p1/',
        'https://jobs.51job.com/weihugongchengshi/p1/',
        'https://jobs.51job.com/wangluoguanli/p1/',
        'https://jobs.51job.com/wangluoweixiu/p1/',
        'https://jobs.51job.com/jilianggongchengshi/p1/',
        'https://jobs.51job.com/biaozhunhuagongchengshi/p1/',
        'https://jobs.51job.com/pinzhijingli/p1/',
        'https://jobs.51job.com/xitongceshi/p1/',
        'https://jobs.51job.com/ruanjianceshi/p1/',
        'https://jobs.51job.com/yingjianceshi/p1/',
        'https://jobs.51job.com/ceshiyuan/p1/',
        'https://jobs.51job.com/wendanggongchengshi/p1/',
        'https://jobs.51job.com/peizhiguanli/p1/',
        'https://jobs.51job.com/jishuwenyuan/p1/',
        'https://jobs.51job.com/shoujiweixiu/p1/',
        'https://jobs.51job.com/diannaoweixiu/p1/',
        'https://jobs.51job.com/shoujiruanjiankaifa/p1/'
    ]

    def parse(self, response):
        qcwy_data = response.css("div.detlist").css('div.e ')
        name = response.css(".mk::text").extract()[2]
        for v in qcwy_data:  # 循环获取

            text = v.css('.text::text').extract_first()  # 提取
            text = text[11:-8]

            if "/" in name:
                fileName = name.replace("/", "or")
            else:
                fileName = name + '.txt'  # 定义文件名

            with open(fileName, "a+") as f:  # “a+”以追加的形式保存文件
                f.write(name)
                f.write('\t')
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.close()

        next_page = response.css('li.bk a::attr(href)').extract()
        if len(next_page) == 1:
            next_page = response.css('li.bk a::attr(href)').extract_first()
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        elif len(next_page) == 2:
            next_page = next_page[1]
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
