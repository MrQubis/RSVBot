from main import *
import txtanalys
import langru

def textcmd(message):
    page = SqlGetBy('page', 'id', message.chat.id)
    groupid = SqlGetBy('groupid', 'id', message.chat.id)


    # main callback

    if(message.text == langru.menu.menu): #меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.menu.rass)
        if(SqlInfo(message.chat.id, 'phone', 'None')):
            markup.row(langru.menu.login)
        elif (SqlInfo(message.chat.id, 'ClassInvite', 'None') == False):
            markup.row(langru.menu.classadd)
        markup.row(langru.menu.about)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.txt.menu, reply_markup=markup)

    elif (message.text == langru.invite.yes):
        classinv = SqlGetByStr('ClassInvite', 'id', message.chat.id)
        SqlUpdate(message.chat.id, 'Class', classinv)
        if(SqlInfo(message.chat.id,'GroupInvite',5)):
            SqlUpdate(message.chat.id, 'groupid', 5)
            SqlUpdate(message.chat.id, 'GroupInvite', 0)
        SqlUpdate(message.chat.id, 'ClassInvite', 'None')
        ShowMark(message.chat.id, langru.invite.success.format(classinv))

    elif (message.text == langru.invite.no):
        classinv = SqlGetByStr('ClassInvite', 'id', message.chat.id)
        SqlUpdate(message.chat.id, 'ClassInvite', 'None')
        ShowMark(message.chat.id, langru.invite.error.format(classinv))

    elif (message.text == langru.menu.classadd):
        if (SqlInfo(message.chat.id, 'ClassInvite', 'None') == False):
            classinv = SqlGetByStr('ClassInvite', 'id', message.chat.id)
            SqlUpdate(message.chat.id, 'page', 11)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.invite.yes, langru.invite.no)
            bot.send_message(message.chat.id, langru.invite.text.format(classinv), reply_markup=markup)

    elif (message.text == langru.menu.rass):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.yes,langru.button.no)
        bot.send_message(message.chat.id, langru.txt.helpsend, reply_markup=markup)

    elif(message.text == langru.menu.login):
        if(SqlInfo(message.chat.id, 'phone', 'None')):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_phone = types.KeyboardButton(text="Отправить данные", request_contact=True)
            markup.row(button_phone)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.login.sendwhat, reply_markup=markup)
            SqlUpdate(message.chat.id, 'page', 1)

    elif (message.text == langru.button.help):
        ShowMark(message.chat.id, langru.txt.info)

    elif (message.text == langru.menu.about):
        ShowMark(message.chat.id, langru.txt.about.format(vers))

    elif (message.text == langru.button.invite): #приглашение от адм
        if (groupid != 1):
            SqlUpdate(message.chat.id, 'page', 2)
            ShowInvite(message.chat.id, langru.adm.infoinvite)

    elif (message.text == langru.adm.addadm):  # администратор
        if (page == 2 and groupid == 2):
            SqlUpdate(message.chat.id, 'page', 3)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.invited, reply_markup=markup)

    elif (message.text == langru.adm.addteach):  # учитель
        if (page == 2 and groupid == 2):
            SqlUpdate(message.chat.id, 'page', 4)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.invited, reply_markup=markup)

    elif (message.text == langru.adm.addteachclass):  # кл. руковод
        if (page == 2 and groupid == 2):
            SqlUpdate(message.chat.id, 'page', 5)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.invited, reply_markup=markup)

    elif (message.text == langru.adm.delete):  # удаление пользователя
        if (page == 2 and groupid == 2):
            SqlUpdate(message.chat.id, 'page', 10)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.deletetxt, reply_markup=markup)

    elif(message.text == langru.adm.addschool): #ученики
        Class = SqlGetByStr('Class', 'id', message.chat.id)
        if (page == 2 and (groupid == 2 or Class != 'None')):
            SqlUpdate(message.chat.id, 'page', 7)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.goclass, reply_markup=markup)

    elif (message.text == langru.adm.addsmam):  # ученики
        Class = SqlGetByStr('Class', 'id', message.chat.id)
        if (page == 2):
            SqlUpdate(message.chat.id, 'page', 20)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row(langru.button.cancel)
            bot.send_message(message.chat.id, langru.adm.goteach, reply_markup=markup)

    elif (message.text == langru.button.yes):
        SqlUpdate(message.chat.id, 'spam', 1)
        ShowMark(message.chat.id, langru.txt.agree)

    elif (message.text == langru.button.no):
        SqlUpdate(message.chat.id, 'spam', 0)
        ShowMark(message.chat.id, langru.txt.disagree)

    elif (message.text == langru.button.cancel): # отмена
        SqlUpdate(message.chat.id, 'page', 0)
        SqlUpdate(message.chat.id, 'sendnew', 0)
        SqlUpdate(message.chat.id, 'sendad', 0)
        if (SqlInfo(message.chat.id, 'groupid', 2)):

            ShowMark(message.chat.id, langru.txt.nonew)
        else:
            ShowMark(message.chat.id, langru.txt.nonew)

    elif(message.text == langru.uved.uvdeomall):
        SqlUpdate(message.chat.id, 'page', 101)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.uved.sendmesto, reply_markup=markup)

    elif (message.text == langru.uved.rasp):
        SqlUpdate(message.chat.id, 'page', 102)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.uved.sendmesto, reply_markup=markup)

    elif (message.text == langru.uved.uvdeomchild):
        SqlUpdate(message.chat.id, 'page', 103)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.uved.sendmesto, reply_markup=markup)

    elif (message.text == langru.uved.childto):
        if(groupid == 2):
            SqlUpdate(message.chat.id, 'page', 6)
        elif (groupid == 4):
            SqlUpdate(message.chat.id, 'page', 104)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        if (groupid == 2):
            bot.send_message(message.chat.id, langru.uved.sendmestoclass, reply_markup=markup)
        elif (groupid == 4):
            bot.send_message(message.chat.id, langru.uved.sendmestoclass_now, reply_markup=markup)

    elif (message.text == langru.uved.mamto):
        if(groupid == 2):
            SqlUpdate(message.chat.id, 'page', 9)
        elif (groupid == 4):
            SqlUpdate(message.chat.id, 'page', 105)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        if (groupid == 2):
            bot.send_message(message.chat.id, langru.uved.sendmestoclass, reply_markup=markup)
        elif (groupid == 4):
            bot.send_message(message.chat.id, langru.uved.sendmestoclass_now, reply_markup=markup)

    elif (message.text == langru.button.choosetech_send):
        SqlUpdate(message.chat.id, 'page', 106)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.uved.sendmesto, reply_markup=markup)


    elif(message.text == langru.button.sendnew):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if(groupid == 2):
            SqlUpdate(message.chat.id,'page',100)
            markup.row(langru.uved.uvdeomall,langru.button.choosetech_send)
            markup.row(langru.uved.rasp, langru.uved.uvdeomchild)
        markup.row(langru.uved.childto,langru.uved.mamto)
        markup.row(langru.button.cancel)
        bot.send_message(message.chat.id, langru.uved.gonew, reply_markup=markup)

    else:
        txtanalys.justtext(message)  ## Проверяем на обычный текст(если не заготовка)