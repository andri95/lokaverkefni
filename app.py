from sys import argv

import bottle
from bottle import *

import pymysql.cursors

#Gagnagrunnurinn
'''
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             charset='utf8mb4')
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE 0106952799_veflokav')

finally:
    connection.close()

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_veflokav',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        tafla1 = "CREATE TABLE notandi(starfsm_numer varchar(3), not_nafn varchar(15), lykil varchar(15), PRIMARY KEY (starfsm_numer))"
        cursor.execute(tafla1)
        tafla2 = "CREATE TABLE frett(starfsm_numer varchar(3), nr_frettar varchar(3), fyrirsogn varchar(255), innihald varchar(255), PRIMARY KEY (nr_frettar), FOREIGN KEY (starfsm_numer) REFERENCES notandi(starfsm_numer))"
        cursor.execute(tafla2)
finally:
    connection.close()

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='0106952799',
                             password='mypassword',
                             db = '0106952799_veflokav',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
starfsm_numer = '101'
not_nafn = 'admin'
lykil = 'admin'

nr_frettar1 = '111'
nr_frettar2 = '112'
nr_frettar3 = '113'
fyrirsogn1 = 'Hreppti 131 milljón og þar með stærsta vinning frá upphafi'
fyrirsogn2 = 'Þessi risi er að koma til Íslands'
fyrirsogn3 = 'Hefur fengið 25 milljónir vegna aksturs og flugs'
frett1 = 'Íslenskur spilari hafði heppnina með sér í kvöld þegar dregið var í EuroJackpot og hreppti rúma 131 milljón króna. Um er að ræða stærsta vinning sem Íslendingur hefur unnið í happdrættinu. Þetta kemur fram í tilkynningu frá Íslenskri getspá.'
frett2 = 'Hann er nærri 400 tonn að þyngd og er nú um borð í hollenska flutningaskipinu Happy Dover. Skipið kom að ströndum Íslands í dag frá Gdynia í Póllandi og lagðist að bryggju í Straumsvík á tíunda tímanum í kvöld. '
frett3 = 'Lilja Rafney Magnúsdóttir, sem setið hefur á þingi fyrir Vinstri græn frá árinu 2009, hefur fengið samtals um 25 milljónir króna greiddar í kostnað vegna aksturs og flugs innan lands á síðustu tíu árum. '

try:
    with connection.cursor() as cursor:
        inn_tafla1 = "INSERT INTO notandi(`starfsm_numer`, `not_nafn`, `lykil`) VALUES(%s, %s, %s)"
        cursor.execute(inn_tafla1, (starfsm_numer, not_nafn, lykil))
        inn_tafla2 = "INSERT INTO frett(`starfsm_numer`, `nr_frettar`, `fyrirsogn`, `innihald`) VALUES(%s, %s, %s, %s)"
        cursor.execute(inn_tafla2, (starfsm_numer, nr_frettar1, fyrirsogn1, frett1))
        cursor.execute(inn_tafla2, (starfsm_numer, nr_frettar2, fyrirsogn2, frett2))
        cursor.execute(inn_tafla2, (starfsm_numer, nr_frettar3, fyrirsogn3, frett3))
        connection.commit()
finally:
    connection.close()
'''

bottle.debug(True)

@get('/')
def index():

    try:
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     user='0106952799',
                                     password='mypassword',
                                     db='0106952799_veflokav',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "SELECT `fyrirsogn`,`innihald` FROM `frett`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()

    return template('index', frettir=result)

run(host='0.0.0.0', port=argv[1])