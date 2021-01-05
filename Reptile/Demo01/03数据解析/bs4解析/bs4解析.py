import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档中数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)  # soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.find('div'))  作用等同于soup.div
    # print(soup.find('div', class_='song'))  属性定位
    # print(soup.find_all('a'))  返回符合要求的所有标签（列表）
    # print(soup.select('.tang'))  参数放某种选择器（id、class、标签选择器），返回的是一个列表
    # print(soup.select('.tang > ul > li > a')[0])  层级选择器的使用 > 表示的使一个层级 （空格）表示的使多个层级
    #   作用等同于上述  空格标识多个层级

    # 获取标签之间的文本数据 soup.a.text/string/get_text()
    # test/get_text() 可以获取一个标签中所有文本内容
    # string 只可以获取该标签下直系文本内容
    # print(soup.select('.tang > ul a')[0].get_text())

    # 获取标签中的属性值
    print(soup.select('.tang > ul a')[0]['href'])