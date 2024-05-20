import time
import random
import ast
import datetime
import os
import urllib
from urllib import request
import csv
from datetime import datetime
import json

nc_begin = {'next_begin': ''}
conti = ['Yes']

def search(data, headers, begin, url, i):
    today = datetime.now().strftime('%Y-%m-%d')
    numb = str(i)

    list = []
    n = 10
    pageSize = 7
    # 阿拉云页面，一页存7个
    maxpage = 400
    # 暂时没测试过，用不到
    findpage = 3
    # 我给每个账号每天留了5次去检查核对的机会
    error = 0

    for i in range(begin, begin + findpage):
        nc_begin['next_begin'] = str(i + 1)
        next1 = nc_begin['next_begin']
        last_page(next1)
        # begin for next account
        data['page_num'] = str(i)
        postData = urllib.parse.urlencode(data).encode("utf-8")  # **
        # 要对发送的数据包编码成二进制字节
        headers['content-length'] = len(postData)
        # 请求体
        req = urllib.request.Request(url, headers=headers, data=postData)

        count = 0
        loop = 0
        ttimes = 8
        while (not loop and count < ttimes):
            try:
                response = urllib.request.urlopen(req)
                # 打开url
                loop = 1
            except Exception as e:
                count = count + 1
                print("reconnecting for" + str(count) + "times")
                time.sleep(0.1 + random.uniform(0.05, 0.1))

        if (count == ttimes):
            error += 1
            print('重连失败')
            res = int(nc_begin['next_begin']) - 1
            nc_begin['next_begin'] = str(res)
            last_page(str(res))
            if error > 5:
                break
            continue
        time.sleep(0.3 + random.uniform(0.05, 0.1))

        print(response)
        data2 = response.read()
        datastr = str(data2, 'utf-8')

        user_dict = ast.literal_eval(datastr)
        # 将字符串转化为原有类型
        data3 = user_dict.get('data')
        # print(type(data3))
        if list == []:

            list = data3.get('records')


        else:
            list = list + data3.get('records')
        print(i)
        # if i % n == 0 or i == (begin + findpage - 1):
        cal = 0
        # 计算是否把所有东西找到
        if i != 0:
            # ????
            if os.path.isfile("D:/" + today + 'account' + numb + ".csv"):
                # 此处每换一个账号 重新存储一次 （举例：2021-7-13account1）
                print('go')

            else:
                infohead = ['海关编码',
                            '详细信息产品名称',
                            '日期',
                            '进口商',
                            '进口商所在国家',
                            '出口商',
                            '出口商所在国家',
                            '起运港',
                            '目的地',
                            '金额（USD）',
                            '重量（kg）']

                with open("D:/" + today + 'account' + numb + ".csv", 'w', newline='', encoding='utf-8')as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(infohead)

                time.sleep(0.1)

            nn = int(len(list) / pageSize)

            for j in range(0, nn * pageSize):

                lst_row = []
                final = []

                if list[j].get('海关编码') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('海关编码'))
                    cal += 1
                if list[j].get('详细产品名称') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('详细产品名称'))
                if list[j].get('日期') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('日期'))
                if list[j].get('进口商') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('进口商'))
                if list[j].get('进口商所在国家') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('进口商所在国家'))
                if list[j].get('出口商') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('出口商'))
                if list[j].get('出口商所在国家') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('出口商所在国家'))
                if list[j].get('起运港') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('起运港'))
                if list[j].get('目的港') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('目的港'))
                if list[j].get('金额') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('金额'))
                if list[j].get('重量') is None:
                    lst_row.append('')
                else:
                    lst_row.append(list[j].get('重量'))

                print(lst_row)
                final.append(lst_row)
                with open("D:/" + today + 'account' + numb + ".csv", 'a+', newline='', encoding='utf-8') as fd:
                    fd_csv = csv.writer(fd)
                    fd_csv.writerows(final)

        if cal == 0:
            print('打印完成')
            conti[0] = 'No'
            break
        list = []


        outp = "D:/" + today + 'account' + numb + ".csv"
        with open('D:/' + 'output_for_sql' + '.json', 'w', encoding='utf-8') as sq:
            json.dump({'sql01': outp.__str__()}, sq)
            sq.close()
            # 新加入

        time.sleep(0.1 + random.uniform(0.05, 0.1))


def last_page(next1):
    with open('D:/' + 'last_page' + '.json', 'w', encoding='utf-8') as j:
        json.dump({'next_starting_page': next1.__str__()}, j)
        j.close()


