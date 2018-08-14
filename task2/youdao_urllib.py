import time
import random
import json
from new_day.tuozhan_all import post

def md5_my(need_str):
    import hashlib

    # 创建md5对象
    md5_o = hashlib.md5()
    # 需要有bytes, 作为参数
    # 由str, 转换成 bytes encode-------str.encode('utf-8')
    # 由bytes转换成 str, decode---------bytes.decode('utf-8')
    sign_bytes = need_str.encode('utf-8')

    # 更新md5 object的值
    md5_o.update(sign_bytes)
    sign_str = md5_o.hexdigest()
    return sign_str

# url

def translate(kw):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        #'Content-Length': '223',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-493176930@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=38624120.26076847; SESSION_FROM_COOKIE=unknown; JSESSIONID=aaabYcV4ZOU-JbQUha2uw; ___rl__test__cookies=1534210912076',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }


    # form 的生成1. i 需要确定, 2, salt, 3, sign
    key= kw

    # salt : ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    salt = int(time.time()*1000 + random.randint(0,10))

    salt_str = str(salt)

    # sign : o = u.md5(S + n + r + D);
    # S = "fanyideskweb"
    # D = "ebSeFb%=XZ%T[KZ)c(sy!"
    # n = key
    # r = salt_str
    S = "fanyideskweb"
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    sign_str = S + key + salt_str + D
    # md5 加密的方法
    sign_md5_str = md5_my(sign_str)

    form = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt_str,
        'sign': sign_md5_str,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    html_bytes = post(url, form, headers=headers)

    # 将 json 类型的 str, 转化成, 字典
    res_dict = json.loads(html_bytes.decode('utf-8'))
    #print(html_bytes.decode('utf-8'))

    translate_res = res_dict['translateResult'][0][0]['tgt']

    return translate_res

if __name__ == '__main__':
    ret = translate('青青河边草')

    print('青青河边草的翻译是:' + ret)
