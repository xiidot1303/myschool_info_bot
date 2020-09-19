from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import students, dt, message
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import os
# Create your views here.
def index(request):
    data = {"HI":"shaha"}
    #_______________________bot
    PORT = int(os.environ.get('PORT', 5000))
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    TOKEN = '1384376997:AAFmCkMDUVrfoDlcs7YYKebyG75Fn5zBI-Y'

   
    def start(update, context):

        item_add = InlineKeyboardButton('add', callback_data='add')
        item_list = InlineKeyboardButton('List of groups', callback_data='list')
        markup = InlineKeyboardMarkup([[item_add, item_list]])
        update.message.reply_text('HI\nYou can see list of students or add students in the list', reply_markup=markup)
        


      
    
    #---------INLINE 
    def callback(update, context):
        if update.callback_query.data == 'list':
            ss = students.objects.all()
            gs = []
            distinct = []
            if ss:
                for i in ss:
                    if not i.group in distinct:
                        gs.append(KeyboardButton(i.group))
                    distinct.append(i.group)
            markup = ReplyKeyboardMarkup([gs], resize_keyboard=True)
            update.callback_query.message.reply_text('List of groups', reply_markup=markup)
        if update.callback_query.data == 'add':
            update.callback_query.message.reply_text('send me student`s name:')
            m = message.objects.get(pk=1) 
            m.name = True
            m.save()



    #------------TEXT
    def text(update, context):
        if update.message.text != '/add':
            m = message.objects.get(pk=1) 
            isname = m.name
            issurname = m.surname
            isgroup = m.group
            if isname:
                m.surname = True
                m.name = False
                m.save()
                students.objects.create(name = str.lower(update.message.text), surname = '/', group = '/')
                update.message.reply_text('send me student surname:')
            elif issurname:
                m.group = True
                m.surname = False
                m.save()
                s = students.objects.get(surname = '/')
                s.surname = str.lower(update.message.text)
                s.save()
                update.message.reply_text('send me group:\nBe carefull, You must write correctly, else your student info will save in another  group')
            elif isgroup:

                m.group = False

                m.save()
                s = students.objects.get(group = '/')
                s.group = str.lower(update.message.text)
                s.save()
                update.message.reply_text('Student added a list successfully')
                item_add = InlineKeyboardButton('add', callback_data='add')
                item_list = InlineKeyboardButton('List of groups', callback_data='list')
                markup = InlineKeyboardMarkup([[item_add, item_list]])
                update.message.reply_text('You can see list of students or add students in the list', reply_markup=markup)
            else:
                ss = students.objects.all()
                gs = []
                for i in ss:
                    gs.append(i.group)
                if update.message.text in gs:
                    ss = students.objects.filter(group=update.message.text)
                    answer = 'The students of ' + update.message.text + ' group:\n\n'
                    for x in ss:
                        answer += x.name + '  ' + x.surname +'\n\n'
                    update.message.reply_text(answer)
                    item_add = InlineKeyboardButton('add', callback_data='add')
                    item_list = InlineKeyboardButton('List of groups', callback_data='list')
                    markup = InlineKeyboardMarkup([[item_add, item_list]])
                    update.message.reply_text('You can see list of students or add students in the list', reply_markup=markup)
    


    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(callback))
    dp.add_handler(MessageHandler(Filters.text, text))

    updater.start_polling()
    #___________________________end bot
    return JsonResponse(data)


