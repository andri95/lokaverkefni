#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from bottle import *
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db='0106952799_vef',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@route('/')
def index():

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `notendanafn`,`lykilord` FROM `innskraning` WHERE `stafsmannanumer`=%1"
            cursor.execute(sql, ('111'))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

    return template('index', user=result)

# run(Debug=True)
run(host='0.0.0.0', port=argv[1])


