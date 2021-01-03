import requests
import json

if __name__ == "__main__":
    # 1、指定URL，注意这里url不是从页面直接获取，而是从抓包里获取的
    post_url = 'https://fanyi.baidu.com/sug'

    #2、进行 UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    #3、 post请求参数处理（同get一样）
    word = input('enter a word:')

    data = {
        'kw':word
    }
    # 4、发起请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5、获取响应数据（这里注意响应数据是json格式，json()返回的是obj，如果确认响应数据时json类型的才可以用 ）
    dic_obj = response.json()

    # 6、持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    # 因为拿到json字符串中有中文，中文不能使用ACSII编码
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!!')


