import requests
import json


if __name__ == "__main__":
    # 1、指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    #2、进行 UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    data = {
        'cname':' ',
        'pid':' ',
        'keyword': '北京',
        'pageIndex':'1',
        'pageSize':'10'
    }

    # 3、发起请求
    response = requests.post(url=url, data=data, headers=headers)

    # 4、获取数据
    list_data = response.text

    fp = open('./肯德基地址.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!!!')
