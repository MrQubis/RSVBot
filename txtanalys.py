from main import *
import langru

lvl = ['Администратор','Учитель','Кл.Руководитель']

def justtext(message):
    page = SqlGetBy('page', 'id', message.chat.id)
    groupid = SqlGetBy('groupid', 'id', message.chat.id)
    Class = SqlGetByStr('Class', 'id', message.chat.id)
    try: #login
        if(len(message.contact.phone_number) > 5):
            SqlUpdate(message.chat.id, 'phone', message.contact.phone_number)
            ShowMark(message.chat.id, langru.login.success.format(message.contact.phone_number[8:]))
            SqlUpdate(message.chat.id, 'page', 0)
    except: pass

    try:
        if(page == 6): #text
            try:
                if(message.json['text'] is not None):
                    SqlUpdate(message.chat.id, 'page', 104)
                    SqlUpdate(message.chat.id, 'Class', message.json['text'])
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.row(langru.button.cancel)
                    bot.send_message(message.chat.id, langru.uved.sendmlass.format(message.json['text']), reply_markup=markup)
            except: pass

    except: pass

    try:
        if (page == 9):  # text
            try:
                if (message.json['text'] is not None):
                    SqlUpdate(message.chat.id, 'page', 105)
                    SqlUpdate(message.chat.id, 'Class', message.json['text'])
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    markup.row(langru.button.cancel)
                    bot.send_message(message.chat.id, langru.uved.sendmlass.format(message.json['text']),
                                     reply_markup=markup)
            except:
                pass

    except:
        pass


    try:
        if(110>= page >= 101 and message.text != 'Отмена'): #text
            try:
                if(message.json['text'] is not None):
                    SendMessage(message,'text',special=Class)
            except:
                try:
                    if(message.json['photo'][0]['file_id'] is not None):
                        try:
                            SendMessage(message, 'photo',
                                        message.json['caption'],Class)
                        except:
                            SendMessage(message, 'photo',special=Class)

                except:
                    if (message.json['video']['file_id'] is not None):
                        SendMessage(message, 'video', special=Class)

    except: pass

    #addadmin
    try:
        if (groupid == 2 and (5 >= page >= 3)):
            if(message.text != langru.button.cancel and message.text.find('79') != -1 and message.text != 'Отмена'):
                phone = GetNumber(message.text)
                check = SqlGetBy('id', 'phone', phone)

                if (phone == -1):
                    bot.send_message(message.chat.id, langru.adm.error)
                else:
                    ShowMark(message.chat.id,langru.adm.success.format(lvl[page-3],message.text))
                    SqlUpdate(check,'groupid',page-1)
    except: pass

    # addadmin
    try:
        if (page == 7):
            if (message.text != langru.button.cancel and message.text.find('79') != -1 and message.text != 'Отмена'):
                phone = GetNumber(message.text)
                check = SqlGetBy('id', 'phone', phone)

                if (phone == -1):
                    bot.send_message(message.chat.id, langru.adm.error)
                else:
                    if(groupid == 2):
                        SqlUpdate(message.chat.id, 'page', 8)
                        SqlUpdate(message.chat.id, 'sendad', check)
                        bot.send_message(message.chat.id, langru.adm.classes)
                    else:
                        SqlUpdate(message.chat.id, 'page', 0)
                        SqlUpdate(check, 'ClassInvite', Class)
                        ShowMark(message.chat.id, langru.adm.successes.format(Class, message.text))
                        bot.send_message(check,
                                         'Вас пригласили вступить в класс!\nКласс:{0}. Зайдите в меню, что подтвердить/отменить'.format(Class))

    except:
        pass
    try:
        if (page == 8 and message.text != 'Отмена'):
            SqlUpdate(message.chat.id, 'page', 0)
            check = SqlGetBy('sendad', 'id', message.chat.id)
            phone = SqlGetBy('phone', 'id', check)
            SqlUpdate(check, 'ClassInvite', message.text)
            ShowMark(message.chat.id,langru.adm.successes.format(message.text,phone))
            bot.send_message(check, 'Вас пригласили вступить в класс!\nКласс:{0}. Зайдите в меню, что подтвердить/отменить'.format(Class))
    except:
        pass

    try:
        if (page == 20):
            if (message.text != langru.button.cancel and message.text.find('79') != -1 and message.text != 'Отмена'):
                phone = GetNumber(message.text)
                check = SqlGetBy('id', 'phone', phone)

                if (phone == -1):
                    bot.send_message(message.chat.id, langru.adm.error)
                else:
                    if (groupid == 2):
                        SqlUpdate(message.chat.id, 'page', 21)
                        SqlUpdate(message.chat.id, 'sendad', check)
                        bot.send_message(message.chat.id, langru.adm.classes)
                    else:
                        SqlUpdate(message.chat.id, 'page', 0)
                        SqlUpdate(check, 'ClassInvite', Class)
                        SqlUpdate(check, 'GroupInvite', 5)
                        ShowMark(message.chat.id, langru.adm.successes.format(Class, message.text))
                        bot.send_message(check,
                                         'Вас пригласили вступить в класс!\nКласс:{0}, как родитель. Зайдите в меню, что подтвердить/отменить'.format(
                                             Class))

    except:
        pass

    try:
        if (page == 10):
            if (message.text != langru.button.cancel and message.text.find('79') != -1 and message.text != 'Отмена'):
                phone = GetNumber(message.text)
                check = SqlGetBy('id', 'phone', phone)

                if (phone == -1):
                    bot.send_message(message.chat.id, langru.adm.error)
                else:
                    SqlUpdate(message.chat.id, 'page', 0)
                    SqlUpdate(check, 'groupid', 1)
                    SqlUpdate(check, 'Class', 'None')
                    SqlUpdate(check, 'ClassInvite', 0)
                    SqlUpdate(check, 'GroupInvite', 0)
                    ShowMark(message.chat.id, langru.adm.successesdel.format(phone))

    except:
        pass

    try:
        if (page == 21 and message.text != 'Отмена'):
            SqlUpdate(message.chat.id, 'page', 0)
            check = SqlGetBy('sendad', 'id', message.chat.id)
            phone = SqlGetBy('phone', 'id', check)
            SqlUpdate(check, 'GroupInvite', 5)
            SqlUpdate(check, 'ClassInvite', message.text)
            ShowMark(message.chat.id, langru.adm.successes.format(message.text, phone))
            bot.send_message(check,
                             'Вас пригласили вступить в класс!\nКласс:{0}, как родитель. Зайдите в меню, что подтвердить/отменить'.format(
                                 Class))
    except:
        pass
