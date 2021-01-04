import requests
import json


if __name__ == "__main__":
    # 1、批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    # 2、进行 UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 5、存储企业id
    id_list = []
    # 存储所有企业详情数据
    all_data_lst = []

    # 2、参数的封装
    for page in range(1, 16):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': ' ',
            'conditionType': '1',
            'applyname': ' ',
            'applysn': ' '
        }
        # 3、发起请求
        response = requests.post(url=url, data=data, headers=headers)
        # 4、获取响应数据
        json_ids = response.json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    # 6、获取企业详情数据
    for id in id_list:
        data = {
            'id':id
        }
        # 获取企业详情数据
        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        all_data_lst.append(detail_json)

    # 7、持久化存储
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_lst, fp=fp, ensure_ascii=False)
    print('over!!!')
