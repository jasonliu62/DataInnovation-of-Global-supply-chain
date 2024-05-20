import account
import search
import ast
from urllib.parse import urlencode
from datetime import datetime, timedelta
import time
import json
import sql

url = 'https://pc.alayunchina.com/baseApi/dataSearch/getForeignCustomerOrderList'
headers = {
    'authority': 'pc.alayunchina.com',
    'method': 'POST',
    'path': '/baseApi/dataSearch/getForeignCustomerOrderList',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '173',
    #
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '__qc_wId=331; pgv_pvid=4739248052; UM_distinctid=1777c9d21e60-080030e18b2c9f-45410429-144000-1777c9d21e743; CNZZDATA1279198396=1291446618-1612703455-%7C1612703455; token=e63001f6-596c-4f0e-bc12-edbae6647dad',
    'origin': 'https://pc.alayunchina.com',
    'referer': 'https://pc.alayunchina.com/workbench/cloud/OverSeas',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': 'bc603de5-699f-4247-9965-d8d07917abed',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

data = {
    'originCountry': 'China (CN)',
    'destinationCountry': '',
    'companyName': '',
    'importerName': '',
    'queryBeginDate': '2021 -06 -01',
    'queryEndDate': '2021 -06 -10',
    'hsCode': '',
    'page_num': '',
    'page_size': '7',
    'goodsName': ''
    # goods Name...


}

zhanghao = {
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
    'c1': '__qc_wId=800; pgv_pvid=2126061615; UM_distinctid=177a8f1a3ee1fe-068201d5cf0de2-45410429-144000-177a8f1a3f0165; CNZZDATA1279198396=781072322-1613447189-%7C1613447189; token=93c173d5-8b98-4d00-a9ab-f807dfbd30a5',
    'c2': '__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=f8689940-36fb-4073-9769-00ea68d2847c',
    'c3': '__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=39da6318-37c5-42c9-aa61-c038081bfd18',
    'c4': '__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612490511; token=57f4b3e6-9e76-4bec-a03f-2998cf02d999',
    'c5': '__qc_wId=331; pgv_pvid=4739248052;UM_distinctid=1777c9d21e60-080030e18b2c9f-45410429-144000-1777c9d21e743; CNZZDATA1279198396=1291446618-1612703455-%7C1612703455; token=e63001f6-596c-4f0e-bc12-edbae6647dad',
    'c6': '__qc_wId=914; pgv_pvid=539137730; UM_distinctid=1770e4a114b3f6-0ceee797a344c4-31346d-e1000-1770e4a114c29c; CNZZDATA1279198396=1463852213-1610852471-https%253A%252F%252Fwww.baidu.com%252F%7C1612840585; token=0c4a3765-27cf-47c5-a84e-b68fbe6619e4'
}


def access(gdname):
    try:
        tokens = account.gttk()
        find = gdname
        last_search(find)
        # 此处是要搜索的货物
        for i in range(1, 7):
            # 此处如果要测试的话，请将1-6改成1-3，以免测试错误让每个号的搜索次数用完，同理account.py的1-6也要改
            search.conti[0] = 'Yes'
            headers['cookie'] = cookies['c' + str(i)]
            headers['token'] = tokens['token' + str(i)]
            print('现在是第' + str(i) + '个账号')
            try:
                f = open('D:/' + 'last_search' + '.json', 'r', encoding='utf-8')
                info_data = json.load(f)
                f.close()
                if find == info_data['last_search']:
                    if i == 1:
                        k = open('D:/' + 'last_page' + '.json', 'r', encoding='utf-8')
                        pg = json.load(k)
                        begin = int(pg['next_starting_page'])
                        k.close()
                        search.search(data, headers, begin, url, i)



                    else:
                        nbegin = search.nc_begin['next_begin']
                        begin = int(nbegin)
                        search.search(data, headers, begin, url, i)



            except Exception as j:
                if i == 1:
                    begin = 1
                    search.search(data, headers, begin, url, i)



                else:
                    nbegin = search.nc_begin['next_begin']
                    begin = int(nbegin)
                    search.search(data, headers, begin, url, i)

            print('准备将csv存入mysql')
            sql_op = open('D:/' + 'output_for_sql' + '.json', 'r', encoding='utf-8')
            op = json.load(sql_op)
            csvtosql = str(op['sql01'])
            print(csvtosql)
            sql.connection(csvtosql)


            if search.conti[0] == 'No':
                break


        print('已经更新last_search为' + find)
        if search.conti[0] == 'No':
            print('本次搜索已经完成')
        else:
            print(find + '的下一页从' + str(search.nc_begin['next_begin']) + '开始搜索')

    except Exception as e:
        asssss = 0


def last_search(find):
    with open('D:/' + 'last_search' + '.json', 'w', encoding='utf-8') as f:
        json.dump({'last_search': find.__str__()}, f)
        f.close()




if __name__ == '__main__':
    try:
        a = open('D:/' + 'last_search' + '.json', 'r', encoding='utf-8')
        info_data = json.load(a)
        ans = info_data['last_search']
        print('上次搜索的货物是：' + ans)
        a.close()
    except Exception as pt:
        print('暂无搜索记录')
    gdname = str(input('请输入要搜索的货物：'))
    data['goodsName'] = gdname
    while True:
        access(gdname)
        time.sleep(1 * 60 * 60 * 15)



