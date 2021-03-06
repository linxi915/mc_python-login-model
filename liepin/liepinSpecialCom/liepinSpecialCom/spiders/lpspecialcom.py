import scrapy
import re
from datetime import datetime
import pandas as pd
import time

from liepinSpd.items import LiepinspdItem


class LiepinSpdier(scrapy.Spider):
    name = 'liepin'
    start_urls = ['https://www.liepin.com/job/1917579081.shtml?d_sfrom=search_comp&d_ckId=d112af69ab58e7da8305520f55b31904&d_curPage=0&d_pageSize=15&d_headId=d112af69ab58e7da8305520f55b31904&d_posi=0',
                  'https://www.liepin.com/job/1917549017.shtml?d_sfrom=search_comp&d_ckId=1bef90aa98c2e8da734552c320527ac0&d_curPage=0&d_pageSize=15&d_headId=1bef90aa98c2e8da734552c320527ac0&d_posi=0',
                  'https://www.liepin.com/job/1917543155.shtml',
                  'https://www.liepin.com/job/1917491571.shtml?d_sfrom=search_comp&d_ckId=5874ecde43eb4bd20e75fecb2709bf85&d_curPage=0&d_pageSize=15&d_headId=5874ecde43eb4bd20e75fecb2709bf85&d_posi=0',
                  'https://www.liepin.com/job/1917505785.shtml?d_sfrom=search_comp&d_ckId=fe82f0f79cda01b1dd4c140ced26087c&d_curPage=0&d_pageSize=15&d_headId=fe82f0f79cda01b1dd4c140ced26087c&d_posi=0',
                  'https://www.liepin.com/job/1916439263.shtml?d_sfrom=search_comp&d_ckId=d3f4428da37a0cd17a6235cb4a027f1e&d_curPage=0&d_pageSize=15&d_headId=d3f4428da37a0cd17a6235cb4a027f1e&d_posi=0',
                  'https://www.liepin.com/job/1911157736.shtml?d_sfrom=search_comp&d_ckId=2cf44398e8273003087d5148e113ef8f&d_curPage=0&d_pageSize=15&d_headId=2cf44398e8273003087d5148e113ef8f&d_posi=0',
                  'https://www.liepin.com/job/1917470663.shtml?d_sfrom=search_comp&d_ckId=9087e4fc55d61d200606fb906999f728&d_curPage=0&d_pageSize=15&d_headId=9087e4fc55d61d200606fb906999f728&d_posi=0',
                  'https://www.liepin.com/job/1917533673.shtml?d_sfrom=search_comp&d_ckId=98408645fba7219d4d7f17f2714c96f0&d_curPage=0&d_pageSize=15&d_headId=98408645fba7219d4d7f17f2714c96f0&d_posi=0',
                  'https://www.liepin.com/job/1917306593.shtml?d_sfrom=search_comp&d_ckId=85f632646e2b1ad7c06f436e25fd674d&d_curPage=0&d_pageSize=15&d_headId=85f632646e2b1ad7c06f436e25fd674d&d_posi=0',
                  'https://www.liepin.com/job/199929552.shtml'
                    ]

    # ????????????????????????
    def parse(self, response):
        text = response.text
        # print(text)
        # ????????????????????????
        # try:
        company_name = response.xpath('//div[@class="about-position"]//a/text()')[0].extract()
        # print(company_name)
        # comp_sum_tag = response.xpath('//div[@class="comp-summary-tag"]/a/text()').extract()
        # ?????????
        # stage = comp_sum_tag[0]
        # print(stage)
        size = re.search(r'???????????????(.*?)???',text).group(1)
        # print(size)
        city = re.search(r'???????????????(.*?)<',text).group(1)
        # print(city)
        industry = re.search(r'??????.*?>(.*?)<',text).group(1)
        # print(industy)
        # ????????????,list
        # comp_clearfix = str(response.xpath('//ul[@class="comp-tag-list clearfix"]//span/text()').extract())
        # print(comp_clearfix)
        # ???????????????   *%?????????float
        # rate_num = response.xpath('//p[@class="rate-num"]//span/text()')[0].extract()
        # rate_num = int(rate_num) / 100
        # print(rate_num)

        # job_count = int(re.search(r'<small data-selector="total">. ???([0-9]+) ???', text).group(1))
        # print(job_count)
        # ????????????(??????)
        # registered_capital = float(re.search(r'<li>???????????????(.*?)???????????????</li>', text).group(1))
        # print(registered_capital)

        as_of_date = datetime.now()  # ????????????????????????????????????

        item = LiepinspdItem()
        # ??????????????????,?????????????????????????????????????????????,?????????????????????
        data = pd.read_csv('G:\workspace\y2019m01\/first_lagou\company300.csv', encoding='gbk')
        try:
            for i in range(len(data)):
                n = 0
                for j in data.loc[i, '????????????']:
                    if j in company_name:
                        n += 1
                if n >= len(data.loc[i, '????????????'])-1:
                    item['ticker'] = data.loc[i, '????????????']
                    print(n, item['ticker'], company_name)
        except BaseException as e:
            item['ticker'] ='None'
            print('ticker????????????')

        item['as_of_date'] = as_of_date
        item['company_name'] = company_name
        # item['stage'] = stage
        item['size'] = size
        item['city'] = city
        item['industry'] = industry
        # item['comp_clearfix'] = comp_clearfix
        # item['rate_num'] = rate_num
        # item['job_count'] = job_count
        # item['registered_capital'] = registered_capital
        # time.sleep(2)

        yield item
        # except BaseException as e:
        #     print('error and pass')