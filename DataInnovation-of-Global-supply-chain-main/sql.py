# coding=utf-8
import pymysql
import pandas as pd
import csv
import time
import os


def connection(fp):
    file_path = fp

    con = pymysql.connect(host='127.0.0.1', user='root', password='Jason5038!', database='test001', charset='utf8')
    cur = con.cursor()
    create_table_user(cur)
    custom_list = []
    if True:
        custom_csv(file_path, custom_list)

        with open("D:/custom_table.csv", 'r', encoding='utf-8') as jb:
            ab = csv.reader(jb)
            for row in ab:
                if row[1] == '海关编码':
                    continue
                else:
                    try:
                        qu = 'INSERT IGNORE INTO custom_gd(' \
                             '`id`,' \
                             '`海关编码`,' \
                             '`详细信息产品名称`)' \
                             'VALUES(%s, %s, %s)'
                        cur.execute(qu, row)
                    except Exception as es:
                        continue

        main_table(file_path)

        with open("D:/main_table.csv", 'r', encoding='utf-8') as ab:
            a = csv.reader(ab)
            for row in a:
                if row[0] == '海关编码/产品信息id':
                    continue

                else:
                    try:
                        qu = 'INSERT INTO main(' \
                             '`海关编码/产品信息id`,' \
                             '`日期`,' \
                             '`进口商`,' \
                             '`进口商所在国家`,' \
                             '`出口商`,' \
                             '`出口商所在国家`,' \
                             '`起运港`,' \
                             '`目的地`,' \
                             '`金额（USD）`,' \
                             '`重量（kg）`,' \
                             '`编号（no）`)'\
                             'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                        cur.execute(qu, row)
                    except Exception as e:
                        print(row)

                        print(e)

        join = 'SELECT*' \
               'FROM main' \
               'JOIN custom_gd ON main.`海关编码/产品信息id` = custom_gd.id'
        cur.execute(join)

    # 'INSERT INTO c2 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    con.commit()
    cur.close()


def create_table_user(cur):
    sql = "CREATE TABLE IF NOT EXISTS `test001`.`main` (" \
          "`海关编码/产品信息id` VARCHAR(200) NOT NULL," \
          "INDEX custom (`海关编码/产品信息id`)," \
          "`日期` VARCHAR(200) NOT NULL," \
          "INDEX date(`日期`)," \
          "`进口商` VARCHAR(200) NOT NULL," \
          "INDEX import (`进口商`)," \
          "`进口商所在国家` VARCHAR(200) NOT NULL," \
          "INDEX import_ct (`进口商所在国家`)," \
          "`出口商` VARCHAR(200) NOT NULL," \
          "INDEX export (`出口商`)," \
          "`出口商所在国家` VARCHAR(200) NOT NULL," \
          "INDEX export_ct (`出口商所在国家`)," \
          "`起运港` VARCHAR(200) NOT NULL," \
          "INDEX start (`起运港`)," \
          "`目的地` VARCHAR(200) NOT NULL," \
          "INDEX destiny (`目的地`)," \
          "`金额（USD）` VARCHAR(200) NOT NULL," \
          "`重量（kg）` VARCHAR(200) NOT NULL," \
          "`编号（no）` INT NOT NULL," \
          "PRIMARY KEY (`编号（no）`));"
    cur.execute(sql)
    cmb = "CREATE TABLE IF NOT EXISTS `test001`.`custom_gd` (" \
          "`id` INT NOT NULL," \
          "INDEX identity (`id`)," \
          "`海关编码` VARCHAR(200) NOT NULL," \
          "INDEX custom (`海关编码`)," \
          "`详细信息产品名称` VARCHAR(500) NOT NULL," \
          "INDEX good (`详细信息产品名称`)," \
          "PRIMARY KEY (`海关编码`));"
    cur.execute(cmb)


def custom_csv(file_path, custom_list):
    with open(file_path, 'r', encoding='utf-8') as f:
        a = csv.reader(f)
        ct = 0
        if os.path.isfile("D:/" + 'custom_table' + ".csv"):
            print('go')
        else:
            infohead = ['id', '海关编码', '详细信息产品名称']
            with open("D:/" + 'custom_table' + ".csv", 'w', newline='', encoding='utf-8') as f1:
                f_csv = csv.writer(f1)
                f_csv.writerow(infohead)
            time.sleep(0.1)
        with open("D:/custom_table.csv", 'r', encoding='utf-8')as r1:
            r = csv.reader(r1)
            for row_2 in r:
                if row_2[1] == '海关编码':
                    continue
                else:
                    ct = int(row_2[0])
                    custom_list.append(row_2[1])

        for row_1 in a:
            if row_1[0] == '海关编码':
                continue
            else:
                if row_1[0] not in custom_list:
                    custom_list.append(row_1[0])
                    ct += 1
                    lstrow1 = []
                    final1 = []
                    lstrow1.append(str(ct))
                    lstrow1.append(row_1[0])
                    lstrow1.append(row_1[1])
                    final1.append(lstrow1)
                    with open("D:/" + 'custom_table' + ".csv", 'a+', newline='', encoding='utf-8') as fd:
                        fd_csv = csv.writer(fd)
                        fd_csv.writerows(final1)
                else:
                    continue


def main_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        a = csv.reader(f)
        count = 0
        if os.path.isfile("D:/" + 'main_table' + ".csv"):
            print('go')
        else:
            infohead = ['海关编码/产品信息id',
                        '日期',
                        '进口商',
                        '进口商所在国家',
                        '出口商',
                        '出口商所在国家',
                        '起运港',
                        '目的地',
                        '金额（USD）',
                        '重量（kg）',
                        '编号（no）']
            with open("D:/" + 'main_table' + ".csv", 'w', newline='', encoding='utf-8') as f1:
                f_csv = csv.writer(f1)
                f_csv.writerow(infohead)
            time.sleep(0.1)
        with open("D:/main_table.csv", 'r', encoding='utf-8')as b:
            r = csv.reader(b)
            for row_2 in r:
                if row_2[0] == '海关编码/产品信息id':
                    continue
                else:
                    count = row_2[10]
        for row in a:
            if row[0] == '海关编码':
                continue
            else:
                with open("D:/custom_table.csv", 'r', encoding='utf-8')as r1:
                    r = csv.reader(r1)
                    for row_2 in r:
                        if row[0] == row_2[1]:
                            count += 1
                            lstrow1 = []
                            final = []
                            lstrow1.append(row_2[0])
                            lstrow1.append(row[2])
                            lstrow1.append(row[3])
                            lstrow1.append(row[4])
                            lstrow1.append(row[5])
                            lstrow1.append(row[6])
                            lstrow1.append(row[7])
                            lstrow1.append(row[8])
                            lstrow1.append(row[9])
                            lstrow1.append(row[10])
                            lstrow1.append(count)
                            final.append(lstrow1)
                            with open("D:/" + 'main_table' + ".csv", 'a+', newline='', encoding='utf-8') as fd:
                                fd_csv = csv.writer(fd)
                                fd_csv.writerows(final)
                        else:
                            continue



