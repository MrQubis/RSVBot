import logging
import telebot,langru, cmd
from time import sleep
from sqlquery import *
from telebot import types
import sys

from tokens import *


logging.basicConfig(filename="error.log", level=logging.INFO)

bot = telebot.TeleBot(testtoken)

vers = '1.0.2'

markupstandart = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupstandart.row(langru.menu.menu, langru.button.help)


markupstandartadm = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupstandartadm.row(langru.menu.menu, langru.button.help)
markupstandartadm.row(langru.button.sendnew,langru.button.invite)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    if(SqlInfo(message.chat.id, 'id', message.chat.id) == False):
        with config.connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`id`, `groupid`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (message.chat.id, 1))
        config.connection.commit()
    ShowMark(message.chat.id, langru.txt.hello)

@bot.message_handler(commands=['update'])
def handle_start_help(message):
    if (SqlInfo(message.chat.id, 'groupid', 2)):
        with config.connection.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE 1"
            cursor.execute(sql, ())
            for row in cursor:
                SqlUpdate(row['id'], 'page', 0)
                SqlUpdate(row['id'], 'sendnew', 0)
                try:
                    ShowMark(row['id'], langru.txt.update)

                except:
                    continue
        config.connection.commit()

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo','contact','video'])
def handle_start_help(message):
    cmd.textcmd(message)

def SendSpecMsg(id,message,type,caption):
    try:
        if (type == 'text'):
            bot.send_message(id, langru.txt.messend.format(message.text))
        elif (type == 'photo' and caption != 'None'):
            bot.send_message(id, langru.txt.messend_attach)
            bot.send_photo(id, message.json['photo'][0]['file_id'], caption=caption)
        elif (type == 'photo' and caption == 'None'):
            bot.send_message(id, langru.txt.messend_attach)
            bot.send_photo(id, message.json['photo'][0]['file_id'])
        elif (type == 'video'):
            bot.send_message(id, langru.txt.messend_attach)
            bot.send_video(id, message.json['video']['file_id'])
    except: pass

def SendMessage(message, type, caption = 'None', special = 'None'):
    page = SqlGetBy('page', 'id', message.chat.id)
    with config.connection.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE 1"
        cursor.execute(sql, ())
        for row in cursor:
            if(page == 101):
                if(row['groupid'] != 2):
                    SendSpecMsg(row['id'],message,type,caption)
            elif(page == 102):
                if (row['groupid'] != 2 and row['spam'] == 1):
                    SendSpecMsg(row['id'], message, type, caption)
            elif (page == 103):
                if (len(row['phone']) > 5):
                    SendSpecMsg(row['id'], message, type, caption)
            elif (page == 104):
                if (row['Class'].find(special) != -1 and row['groupid'] == 1):
                    SendSpecMsg(row['id'], message, type, caption)
            elif (page == 105):
                if (row['Class'].find(special) != -1 and row['groupid'] == 5):
                    SendSpecMsg(row['id'], message, type, caption)
            elif (page == 106):
                if (row['groupid'] == 3):
                    SendSpecMsg(row['id'], message, type, caption)

        SqlUpdate(message.chat.id, 'page', 0)
        config.connection.commit()
        ShowMark(message.chat.id, langru.txt.access)

def ShowMark(id,msg):
    if (SqlInfo(id, 'groupid', 2) or SqlInfo(id, 'groupid', 4)):
        bot.send_message(id, msg, reply_markup=markupstandartadm)
    else: bot.send_message(id, msg, reply_markup=markupstandart)

def ShowInvite(id,msg):
    if (SqlInfo(id, 'groupid', 2)):
        markupinvite = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markupinvite.row(langru.adm.addteach, langru.adm.addteachclass,langru.adm.addadm)
        markupinvite.row(langru.adm.addschool,langru.adm.addsmam)
        markupinvite.row(langru.adm.delete)
        markupinvite.row(langru.button.cancel)
        bot.send_message(id, msg, reply_markup=markupinvite)
    elif (SqlInfo(id, 'groupid', 4)):
        markupinvite = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markupinvite.row(langru.adm.addschool,langru.adm.addsmam)
        markupinvite.row(langru.button.cancel)
        bot.send_message(id, msg, reply_markup=markupinvite)

def startbot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    sys.setrecursionlimit(99999999)
    startbot()