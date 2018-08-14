from urllib import request,parse
from urllib.error import HTTPError,URLError
import json
from http import cookiejar

class session():
    def __init__(self):
        cookie_object = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie_object)
        self.opener = request.build_opener(handler)
    def get(self,url,headers=None,):
        return get(url,headers,opener=self.opener)

    def post(self,url,form=None,headers=None,):
        return post(url, headers, opener=self.opener)


def get(url,headers=None,opener=None):
    '''
    :param url: get 请求的路径
    :param headers: 请求头
    :return: 二进制源代码
    '''
    html_byte = urlrequests(url,headers=headers,opener=opener)
    return html_byte

def post(url,form=None,headers=None,opener=None):
    '''
    :param url: post 请求的路径
    :param form: 请求的参数
    :param headers: post 请求头
    :return: json 列表
    '''
    html_byte = urlrequests(url,form=form,headers=headers,opener=opener)

    return html_byte

def urlrequests(url,form=None,headers=None,opener=None):
    if headers == None:
        user_Agent = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        headers = {
            'User_Agent': user_Agent
        }
    html_byte = b''

    try:
        if form == None:
            req = request.Request(url, headers=headers)
        else:
            form_dict = form
            form_byte = parse.urlencode(form_dict)
            req = request.Request(url,data=form_byte.encode('utf-8'),headers=headers)
        if opener:
            response = opener.open(req)
        else:
            response = request.urlopen(req)
        html_byte = response.read()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    return html_byte

if __name__ == '__main__':
    # url = 'http://www.baidu.com'
    # res = get(url)
    # print(res.decode())

    url = 'http://fanyi.baidu.com/sug'
    res = post(url,form={'kw':'漂亮'})
    print(json.loads(res.decode('utf-8')))
