import requests

if __name__ == "__main__":
    # 指定图片url
    url = 'https://pic.qiushibaike.com/system/pictures/12393/123937849/medium/TR7054L6WSSUI4LN.jpg'
    # 获取二进制形式的图片数据（content返回的是二进制形式的响应数据）
    # text（字符串）json（对象）
    img_data = requests.get(url=url).content

    with open('./糗图.jpg', 'wb') as fp:
        fp.write(img_data)

    print('over!!!')