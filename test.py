# 测试百度车牌识别ocr
# 1. 获取token
# import requests 
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=。。。。&client_secret=。。。。。'
# response = requests.get(host)
# if response:
#     print(response.json()['access_token'])


# # 2. 调取通用识别的api
# import requests
# import base64
# '''
# OCR 通用识别
# '''
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
# # 二进制方式打开图片文件
# f = open('./dataset/images/─■A0C93F.jpg', 'rb')
# img = base64.b64encode(f.read())

# params = {"image":img}
# access_token = ''
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())


# 2. 车牌识别的api
import requests
import base64
'''
OCR 通用识别
'''
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
# 二进制方式打开图片文件
f = open('./dataset/images/456.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = 'access_token'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())