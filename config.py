import pymysql, mysqlconnect
connection = pymysql.connect(host=mysqlconnect.host, ## Хост от бд из mysqlconnect
                             user=mysqlconnect.user, ## Логин от бд из mysqlconnect
                             password=mysqlconnect.password, ## Пароль от бд из mysqlconnect
                             db=mysqlconnect.db, ## Сама бд из mysqlconnect
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)