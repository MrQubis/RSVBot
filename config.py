import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='main',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)