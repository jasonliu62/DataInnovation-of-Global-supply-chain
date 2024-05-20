
import ast
import urllib

def gttk():
    url = 'https://pc.alayunchina.com/baseApi/user/login'
    LoginHead = {
        'authority': 'pc.alayunchina.com',
        'method': 'POST',
        'path': '/baseApi/user/login',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '47',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'pgv_pvid=2126061615; UM_distinctid=177a8f1a3ee1fe-068201d5cf0de2-45410429-144000-177a8f1a3f0165; __qc_wId=223; CNZZDATA1279198396=781072322-1613447189-%7C1613454300; token=null',
        'origin': 'https://pc.alayunchina.com',
        'referer': 'https://pc.alayunchina.com/login',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same - origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    account = {
            'z1': '19946274065',
            'm1': 'jiangjianwei',
            'z2': '18221189950',
            'm2': 'jydz1423',
            'z3': '15801998598',
            'm3': 'gaorui63782468',
            'z4': '17781617624',
            'm4': '556677520Kmq',
            'z5': '18621533161',
            'm5': 'zzy863arkZZY',
            'z6': '15232173323',
            'm6': 'mnqyfc86'
    }

    cookies = {
        'c1':'__qc_wId=800; pgv_pvid=2126061615; UM_distinctid=177a8f1a3ee1fe-068201d5cf0de2-45410429-144000-177a8f1a3f0165; CNZZDATA1279198396=781072322-1613447189-%7C1613447189; token=93c173d5-8b98-4d00-a9ab-f807dfbd30a5',
        'c2':'__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=f8689940-36fb-4073-9769-00ea68d2847c',
        'c3':'__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=39da6318-37c5-42c9-aa61-c038081bfd18',
        'c4':'__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=57f4b3e6-9e76-4bec-a03f-2998cf02d999',
        'c5':'__qc_wId=331; pgv_pvid=4739248052;UM_distinctid=1777c9d21e60-080030e18b2c9f-45410429-144000-1777c9d21e743; CNZZDATA1279198396=1291446618-1612703455-%7C1612703455; token=e63001f6-596c-4f0e-bc12-edbae6647dad',
        'c6':'__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612840585; token=0c4a3765-27cf-47c5-a84e-b68fbe6619e4'
    }
    tokens = {}
    LoginData = {
        'account_name': '19946274065',
        'user_password': 'jiangjianwei'
    }

    for i in range (1, 7):
        # 如果测试，此处请更改
        LoginData['account_name'] = account['z'+str(i)]
        LoginData['user_password'] = account['m' + str(i)]
        postData = urllib.parse.urlencode(LoginData).encode("utf-8")
        LoginHead['content-length'] = len(postData)
        # 请求体
        req = urllib.request.Request(url, headers=LoginHead, data=postData)
        response = urllib.request.urlopen(req)
        data2 = response.read()
        datastr = str(data2, 'utf-8')
        user_dict = ast.literal_eval(datastr)
        data3 = user_dict.get('data')
        token = data3.get('user_token')
        tokens['token'+str(i)] = token
    return tokens




