import requests
import re
import os

if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # 创建一个文件夹用来保存图片
    if not os.path.exists('./newQiutuLibs'):
        os.mkdir('./newQiutuLibs')

    # 通过分析，可以设置一个通过的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pageNum in range(1, 3):
        # 对应页面的url
        new_url = format(url%pageNum)
        # 使用通用爬虫对整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text
        # 使用聚焦爬虫对页面中所有的的糗图进行解析
        # 正则表达式
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

        # 正则作用到数据解析时re.S，即为单行匹配
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            # 拼接处一个完整的url
            src = 'https:' + src
            # 获取图片的二进制文件
            img_data = requests.get(url=src, headers=headers).content
            # 获取图片名称
            img_name = src.split('/')[-1]
            # 图片存储路径
            img_path = './newQiutuLibs/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！！')
