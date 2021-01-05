import requests
import os
from lxml import html


if __name__ == "__main__":
    etree = html.etree

    url = 'https://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 这里解决中文乱码问题
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    # 数据解析
    tree = etree.HTML(page_text)
    # 这里存放简历url
    # all_jianli_url = []
    # 解析为a标签对象//
    a_list = tree.xpath('//div[@id="container"]/div/a')

    # 创建文件夹
    if not os.path.exists('./jianli'):
        os.mkdir('./jianli')
    print(a_list)
    for a in a_list:
        jianli_url = 'https:' + a.xpath('./@href')[0]
        # 获取简历模板名称
        jianli_name = a.xpath('./img/@alt')[0] + '.rar'
        print(jianli_name)
        # jianli_name = jianli_name.encode('iso-8859-1').decode('gbk')
        # all_jianli_url.append(jianli_url)
        # 发起请求
        page_text = requests.get(url=jianli_url, headers=headers).text
        tree = etree.HTML(page_text)
        # 获取简历url
        jianli_load_url = tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[4]/a/@href')[0]
        # 获取简历名称
        # jianli_path = 'jianli/' + jianli_load_url.split('/')[-1]
        jianli_path = 'jianli/' + jianli_name
        # 发起请求
        jianli_data = requests.get(url=jianli_load_url, headers=headers).content
        # 持久化存储
        with open(jianli_path, 'wb') as fp:
            fp.write(jianli_data)
            print(jianli_path, '下载成功')
    print('perfect')


