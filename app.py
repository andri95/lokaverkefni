#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import *
import pymysql.cursors

bottle.debug(True)

@get('/')
def index():

    try:
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     user='0106952799',
                                     password='mypassword',
                                     db='0106952799_frettavefur',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "SELECT `not_nafn`,`lykil` FROM `notandi`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

    return template('index', user=result)

run(host='0.0.0.0', port=argv[1])
