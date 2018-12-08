#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from bottle import *
import pymysql.cursors

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db='0106952799_frettavefur',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@get('/')
def index():

    try:
        with connection.cursor() as cursor:
            sql = "SELECT `not_nafn`,`lykil` FROM `notandi`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

    return template('index', user=result)

run(Debug=True)
run(host='0.0.0.0', port=argv[1])
