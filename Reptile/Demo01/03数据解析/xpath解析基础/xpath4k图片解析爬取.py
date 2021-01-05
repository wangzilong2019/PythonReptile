import requests
import os
from lxml import html


if __name__ == "__main__":
    etree = html.etree

    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    # 解决爬取图片名称乱码问题 (此时手动设置响应数据编码格式解决不了乱码问题)
    # response.encoding = 'utf-8'
    page_text = response.text
    # 实例化对象
    tree = etree.HTML(page_text)
    # 获取li标签对象
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    # 创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 较为通用的处理中文乱码解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name, img_src)
        # 请求图片持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功')
    print('over!!!')