import requests
from lxml import html


if __name__ == "__main__":
    etree = html.etree
    # 实例化一个etree对象，且将
    tree = etree.parse('test.html')
    # 第一个 / 表示从根目录遍历（这里要注意），表示一个层级
    r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')  与上述作用相同//：表示多个层级，
    # r = tree.xpath('//div')  与上述相同 //：表示从任意位置开始定位
    # r = tree.xpath('//div[@class="song"]')  属性定位
    # r = tree.xpath('//div[@class="song"]/p[3]')  索引定位（这里索引从1开始）

    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]  取内容：/text()，注意这里返回的是列表，后面取得是内容
    # /text()：获取的是标签中直系文本内容；//text()：获取该标签下的所有内容
    # /@attrName：取属性  例如：img/@src
    print(r)




