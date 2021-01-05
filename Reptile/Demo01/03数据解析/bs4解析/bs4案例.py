import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 1、批量获取不同企业的id值
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

    # 2、进行 UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text

    # 实例化一个BeautifulSoup对象
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，得到详情页中章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功！！！')
