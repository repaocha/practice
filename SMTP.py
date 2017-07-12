#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='123456', database='test',unix_socket='/private/tmp/mysql.sock')

cursor = conn.cursor()
# ����user��:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# ����һ�м�¼��ע��MySQL��ռλ����%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# �ύ����:
conn.commit()
cursor.close()

# ���в�ѯ:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# �ر�Cursor��Connection:
cursor.close()
conn.close()