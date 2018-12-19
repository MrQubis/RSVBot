import config
from func import *

def SqlInfo(id,field,num):
    with config.connection.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE id = %s"
        cursor.execute(sql, (id))
        for row in cursor:

            if (row[field] == num):

                config.connection.commit()
                return True

    config.connection.commit()
    return False

def SqlUpdate(id,field,num):
    with config.connection.cursor() as cursor:
        sql = "UPDATE `users` SET `{0}` = %s WHERE id = %s".format(field)
        cursor.execute(sql, (num,id))

    config.connection.commit()

def SqlGetByStr(what, field, num):
    with config.connection.cursor() as cursor:
        sql = "SELECT `{0}` FROM `users` WHERE `{1}` = {2}".format(what, field, num)

        cursor.execute(sql, ())
        oneRow = cursor.fetchone()

        if oneRow != None:
            return oneRow[what]

    config.connection.commit()
    return 'None'

def GetNumber(number):
    with config.connection.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `Phone` != 'None'"
        cursor.execute(sql, ())
        for row in cursor:
            if (int(strspn(row['phone'],str(number))) >= 90):
                config.connection.commit()
                return row['phone']
    config.connection.commit()
    return -1


def SqlGetBy(what, field, num):
    with config.connection.cursor() as cursor:
        sql = "SELECT `{0}` FROM `users` WHERE `{1}` = {2}".format(what,field,num)

        cursor.execute(sql, ())
        oneRow = cursor.fetchone()


        if oneRow != None:
            return int(oneRow[what])

    config.connection.commit()
    return -1

