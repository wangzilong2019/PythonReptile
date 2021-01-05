import requests
from lxml import html


if __name__ == "__main__":
    # etree = html.etree
    #
    # url = 'https://www.aqistudy.cn/historydata/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    # }
    # page_text = requests.get(url=url, headers=headers).text
    # tree = etree.HTML(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_name = []
    # # 解析到的热门城市城市名称
    # for li in host_li_list:
    #     host_city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(host_city_name)
    #
    # # 解析全部城市名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(city_name)
    #
    # print(all_city_name, len(all_city_name))


    etree = html.etree

    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)

    # div/ul/li/a  热门城市的a标签层级关系
    # div/ul/div[2]/li/a  全部城市的a标签层级关系

    # 存储热门城市和全部城市的列表
    all_city_name = []
    # 热门城市和全部城市的a标签对象
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_name.append(city_name)

    print(all_city_name, len(all_city_name))
