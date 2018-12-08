<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Forsíða</title>
  </head>
  <body>
    <p>Notandi:  {{ user }} </p>
  </body>
</html>



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
