import requests  # 导入requests库

r = requests.get('https://unsplash.com')  # 向目标url地址发送get请求，返回一个response对象

# print(type(r))

'''
# get请求（它构造了如下网址：http://httpbin.org/get?key1=value1&key2=value2）
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

# POST请求（用来提交表单数据，即填写一堆输入框，然后提交）
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
'''

print(r.text)  # r.text是http response的网页HTML
