import requests
from lxml import html


if __name__ == "__main__":
    etree = html.etree

    url = 'https://suzhou.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    # 存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('./58.txt', 'w', encoding='utf-8')

    for li in li_list:
        # 这里注意./代表当前路径
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title)
