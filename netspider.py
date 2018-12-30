import requests
from lxml import etree


url = 'http://waphn.189.cn/selfservice/adsl/queryAdslByCard'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'code_v=20170913; security_session_verify=a15f2c49fa4ff8999fa24e43a9c9fc87; JSESSIONID=67B9B0F52F14BC70452FCCEA3C6EBD74; svid=E3420CDF00F9F071; Hm_lvt_486ad555e85be4df181febdb2cb4b8a0=1545891479; Hm_lvt_0a4d7303a7ba43c1413cb959e5488e71=1545891479; s_fid=10C94B4CC87F8FFF-1D24D431ADCD1FA1; loginStatus=non-logined; lvid=7fb5dd7b3791ea608844beab7b4df7e5; nvid=1; trkId=1613332B-4E97-4079-834C-8F575C201555; s_cc=true; trkHmClickCoords=15%2C24%2C707; Hm_lpvt_0a4d7303a7ba43c1413cb959e5488e71=1545891573; Hm_lpvt_486ad555e85be4df181febdb2cb4b8a0=1545891573; s_sq=eship-189-wap%3D%2526pid%253D%25252Fpage%25252Fadsl%25252FnewAdslTopup%25252Fsearch.jsp%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BmySubmit%252528%252529%25257D%2526oidt%253D2%2526ot%253DP%26eshipeship-189-all%3D%2526pid%253D%25252Fpage%25252Fadsl%25252FnewAdslTopup%25252Fsearch.jsp%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BmySubmit%252528%252529%25257D%2526oidt%253D2%2526ot%253DP',
    'Host': 'waphn.189.cn',
    'Origin': 'http://waphn.189.cn',
    'Referer': 'http://waphn.189.cn/page/adsl/newAdslTopup/search.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}   #请求头


doc = open('result.txt','w')
for data in open("input_ids.txt"):
#data = {'cardNo': '430381198609187137'}
    data = data.strip('\n')
    data1 = {'cardNo': data}
    response = requests.post(url, data=data1, headers=headers)
    html = etree.HTML(response.text)
    result = html.xpath('//table[@class="recharge-tab"]/tr/td/text()')
    print(data,',',result)
    print(data, '|', result, file=doc)
doc.close()