import requests

# UA伪装

# User-Agent：请求载体的身份标识
# UA伪装：门户网站的服务器会检测对应请求的载体身份标识，如果检测到某一载体身份标识为浏览器
# 说明请求为一个正常的请求，如果检测到请求的载体身份标识不是基于一款浏览器，则表示为不正常请求，服务器端可能会拒绝请求

# 即要建立UA伪装：让爬虫对应的请求载体身份标识伪装为一筐浏览器
# UA检测：反爬策略
# UA伪装：反反爬机制
if __name__ == "__main__":

    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    #1、指定url
    url = 'https://www.baidu.com/s'
    #2、处理url所携带的参数，封装到字典中
    kw = input('enter a word:')
    param = {
        'wd':kw
    }

    #2、对指定的url发起请求，对应的url是携带参数的，且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
