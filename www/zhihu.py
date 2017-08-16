import requests

baseUrl = 'https://zhuanlan.zhihu.com'
headers = {'referer': 'https://zhuanlan.zhihu.com',
           'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'}
url = 'https://zhuanlan.zhihu.com/api/recommendations/posts?limit=%s&offset=0&seed=50'

def getRecommend(num):
    ret = requests.get(url % num, headers=headers)
    return ret.json()


if __name__ == '__main__':
    print(getRecommend())
