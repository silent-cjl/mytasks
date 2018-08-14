from new_day.tuozhan_all import post,get
import json
from urllib import request,parse
from http import cookiejar

url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018721547588'
form = {
    "email": "17600088221",
    "icode": "",
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": "1",
    "captcha_type": "web_login",
    "password": "37be309b4c4367fb4cf5c63b72981dadff7d8e14bad67e2ef818ba164b6c7d9f",
    "rkey": "cb15f985754fd884a44506ff5db1256e",
    "f": "https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_r-h4h4RsVJtWYvcrgiTSe0",
}

cookie_object = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie_object)
opener = request.build_opener(handler)

form_bytes = parse.urlencode(form).encode('utf-8')
response = opener.open(url,form_bytes)
# html_bytes = post(url,form)
res_dict = json.loads(response.read().decode('utf-8'))
home_url = res_dict['homeUrl']
response = opener.open(home_url)
html_bytes = response.read().decode('utf-8')
print(html_bytes)