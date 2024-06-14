import requests

def check_connection(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 如果响应的状态码不是 200，就抛出异常
        return True
    except requests.exceptions.RequestException as err:
        print(f"网络连接失败：{err}")
        return False

# 测试网络连接
url = "https://www.baidu.com"
if check_connection(url):
    print("网络连接正常")
else:
    print("网络连接失败")