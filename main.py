#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


############################ States ###########################################
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
                            reply_markup=timetable_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "Change settings for reminders for my lessons and exams"
def settings_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=settings_msg(),
                            reply_markup=settings_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "See module-specific information from your lecturers"
def information_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=information_msg(),
                            reply_markup=information_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "Learn more about what I can do for you"
def help_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=help_msg(),
                            reply_markup=help_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


############################ Keyboards #########################################

# All functions here are appended with _keyboard for consistency
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton("Send me your NUSMods timetable",
                                    callback_data='m1')],
              [InlineKeyboardButton("Change settings for reminders for my lessons and exams",
                                    callback_data='m2')],
              [InlineKeyboardButton("See module-specific information from your lecturers",
                                    callback_data='m3')],
              [InlineKeyboardButton("Learn more about what I can do for you",
                                    callback_data='m4')]
              ]
  return InlineKeyboardMarkup(keyboard)


def timetable_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def settings_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def information_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def help_keyboard():
    keyboard = [[InlineKeyboardButton('Return', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################

# All functions here are appended with _msg for consistency
def main_menu_msg():
    return ("*Hi there\! I am the NUSMods Telebot\.*\nIf it is your first time "
            "using this bot, please select 'Learn more' below to learn "
            "what I can do for you\.")

def timetable_msg():
    return ("*Timetable page:*\n"
            "I can't do anything yet\! Go back\!")

def settings_msg():
    return ("*Settings page:*\n"
            "I can't do anything yet\! Go back\!")

def information_msg():
    return ("*Information page:*\n"
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


############################# Handlers #########################################
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(os.environ['TELE_TOKEN'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu_page, pattern='main'))
    dp.add_handler(CallbackQueryHandler(timetable_page, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(settings_page, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(information_page, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(help_page, pattern='m4'))

    dp.add_error_handler(error)

    logger.info("Starting NUSMods Telebot...")
    updater.start_polling()
    logger.info("Bot is running!")
    updater.idle()


if __name__ == '__main__':
    main()