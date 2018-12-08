#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from bottle import *
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             charset='utf8mb4')
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE 0106952799_frettavefur')

finally:
    connection.close()

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_frettavefur',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
try:
    with connection.cursor() as cursor:
        tafla1 = "CREATE TABLE notandi(starfsm_numer varchar(3), not_nafn varchar(15), lykil varchar(15))"
        cursor.execute(tafla1)
        tafla2 = "CREATE TABLE frett(starfsm_numer varchar(3), nr_frettar varchar(3), fyrirsogn varchar(30), innihald varchar(60))"
        cursor.execute(tafla2)
finally:
    connection.close()

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_frettavefur',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
starfsm_numer = 101
not_nafn = 'admin'
lykil = 'admin'
try:
    with connection.cursor() as cursor:
        inn_tafla1 = "INSERT INTO notandi(`starfsm_numer`, `not_nafn`, `lykil`) VALUES(%s, %s, %s)"
        cursor.execute(inn_tafla1, (starfsm_numer, not_nafn, lykil))
        connection.commit()
finally:
    connection.close()

@route('/')
def index():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                                 user='0106952799',
                                 password='mypassword',
                                 db='0106952799_frettavefur',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
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

'''
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_frettavefur',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

try:
    with connection.cursor() as cursor:
        sql = "SELECT `not_nafn`,`lykil` FROM `notandi` WHERE `stafsm_numer`=%s"
        cursor.execute(sql, ('101'))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()


connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_frettavefur',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

try:
    with connection.cursor() as cursor:
        sql = "SELECT `not_nafn`,`lykil` FROM `notandi`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
'''