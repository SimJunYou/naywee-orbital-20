#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

import requests
import json

from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# ConversationHandler states
TIMETABLE = range(1)


# User's timetable data
module_data = []


########## STATES ##########

def start(update, context):
    update.message.reply_text(main_menu_msg(),
                              reply_markup=main_menu_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)


# All state functions are appended with _page for consistency
def main_menu_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=main_menu_msg(),
                            reply_markup=main_menu_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "Send me your NUSMods timetable"
def timetable_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=timetable_msg(),
                            parse_mode=ParseMode.MARKDOWN_V2)
    return TIMETABLE


# User input valid NUSMods timetable link
def timetable_input_page(update, context):
    url = update.message.text
    url = url.split('?')[1].split('&')
    for data in url:
        data = data.split('=')
        data[1] = data[1].split(',')
        module_data.append(data)
    for data in module_data:
        for x in range(len(data[1])):
            data[1][x] = data[1][x].split(':')
            lesson_type = data[1][x][0]
            if lesson_type == "LEC":
                data[1][x][0] = "Lecture"
            elif lesson_type == "TUT":
                data[1][x][0] = "Tutorial"
            elif lesson_type == "REC":
                data[1][x][0] = "Recitation"
            elif lesson_type == "LAB":
                data[1][x][0] = "Laboratory"
            elif lesson_type == "SEC":
                data[1][x][0] = "Sectional Teaching"
    update.message.reply_text(timetable_input_msg(),
                              reply_markup=return_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return ConversationHandler.END


# User input invalid link
def invalid_input_page(update, context):
    update.message.reply_text(invalid_input_msg(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return TIMETABLE


# User types /cancel
def cancel_page(update, context):
    update.message.reply_text(cancel_msg(),
                              reply_markup=return_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return ConversationHandler.END


# "Change settings"
def settings_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=settings_msg(),
                            reply_markup=settings_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "See announcements"
def announcement_page(update, context):
    query = update.callback_query
    text = "Your lesson details are listed here:\n"
    semester = 1
    for i in range(len(module_data)):
        text = text + "\n" + module_data[i][0] + "\n"
        page = requests.get('https://api.nusmods.com/v2/2019-2020/modules/' + module_data[i][0] + '.json')
        page_py = json.loads(page.text)
        for x in page_py["semesterData"][semester - 1]["timetable"]:
            for j in range(len(module_data[i][1])):
                if x["classNo"] == module_data[i][1][j][1] and x["lessonType"] == module_data[i][1][j][0]:
                    text = text + x["lessonType"] + " " + x["classNo"] + " " + x["venue"] + " "\
                           + x["day"] + " " + x["startTime"] + "\n"
    query.edit_message_text(text=text,
                            reply_markup=return_keyboard())


# "Learn more"
def help_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=help_msg(),
                            reply_markup=return_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# List all modules added by the user
def list_module_page(update, context):
    query = update.callback_query
    if len(module_data) == 0:
        text = "No modules added yet!"
        query.edit_message_text(text,
                                reply_markup=return_keyboard())
    else:
        text = "Here is the list of your modules:\n\n"
        for data in module_data:
            text = text + data[0] + "\n"
        query.edit_message_text(text,
                                reply_markup=return_keyboard())


########## KEYBOARDS ##########

# All functions here are appended with _keyboard for consistency
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Sync timetable",
                                      callback_data='m1')],
                [InlineKeyboardButton("Change settings",
                                      callback_data='m2')],
                [InlineKeyboardButton("See announcements",
                                      callback_data='m3')],
                [InlineKeyboardButton("Learn more about me",
                                      callback_data='m4')],
                [InlineKeyboardButton("List my module(s)",
                                      callback_data='m5')]]
    return InlineKeyboardMarkup(keyboard)


def settings_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def information_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


# Keyboard that returns user to main page
def return_keyboard():
    keyboard = [[InlineKeyboardButton('Return to main page', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


########## MESSAGES ##########

# All functions here are appended with _msg for consistency
def main_menu_msg():
    return ("*Hi there\! I am the NUSMods Telebot\.*\nIf it is your first time "
            "using this bot, please select 'Learn more' below to learn "
            "what I can do for you\.")


def timetable_msg():
    return ("*Timetable page:*\n"
            "Send me a link to your NUSMods timetable for me to sync\!")


def timetable_input_msg():
    return ("Your timetable is now synced\!")


def invalid_input_msg():
    return ("Invalid input\! Please send me a url link instead\. Enter \/cancel "
            "to go back to the main page\.")


def cancel_msg():
    return ("Action cancelled\.")


def settings_msg():
    return ("*Settings page:*\n"
            "I can't do anything yet\! Go back\!")


def help_msg():
    return ("*Hi\! I am NUSMods Telebot\.*\n\n"
            "By sending me the link to your NUSMods timetable, I can link myself up with "
            "NUSMods’ data to send you reminders on lesson timings and venues\. If there is "
            "a change in your timetable, simply send your timetable link to me again\!\n\n"
            "I will send you daily reminders by default, but you can disable and then "
            "subsequently restart certain reminders if you wish\. You can also create custom "
            "reminders and change the frequency of your reminders\.\n\n"
            "You can view announcements given by your faculty members through me as well\!")


########## HANDLERS ##########

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(os.environ['TELE_TOKEN'], use_context=True)

    dp = updater.dispatcher
    # jq = updater.job_queue

    timetable_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(timetable_page, pattern='m1')],
        states={TIMETABLE: [MessageHandler(Filters.regex(r'https:\/\/nusmods\.com(.*)'), timetable_input_page),
                            MessageHandler(Filters.all & ~Filters.command, invalid_input_page)]},
        fallbacks=[CommandHandler('cancel', cancel_page),
                   CommandHandler('start', cancel_page)]
    )

    dp.add_handler(timetable_conv)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu_page, pattern='main'))
    dp.add_handler(CallbackQueryHandler(timetable_page, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(settings_page, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(announcement_page, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(help_page, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(list_module_page, pattern='m5'))

    dp.add_error_handler(error)

    logger.info("Starting NUSMods Telebot...")
    updater.start_polling()
    logger.info("Bot is running!")
    updater.idle()


if __name__ == '__main__':
    main()