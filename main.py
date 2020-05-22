#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# ConversationHandler states
TIMETABLE, ADD_MODULE = range(2)

# List of user's modules
modules = []


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
                            reply_markup=return_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)
    return TIMETABLE


# User input valid NUSMods timetable link
def timetable_input_page(update, context):
    update.message.reply_text(timetable_input_msg(),
                              reply_markup=return_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return ConversationHandler.END


# User input invalid link
def invalid_input_page(update, context):
    update.message.reply_text(invalid_input_msg(),
                              reply_markup=return_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return TIMETABLE


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
                            reply_markup=return_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)


# "Manually add module(s)"
def module_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=add_module_msg_1(),
                            reply_markup=return_keyboard(),
                            parse_mode=ParseMode.MARKDOWN_V2)
    return ADD_MODULE


# Prompts the user to add more modules
def module_page_2(update, context):
    new_text = update.message.text + add_module_msg_2()
    update.message.reply_text(text=new_text,
                              reply_markup=return_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    modules.append(update.message.text)
    return ADD_MODULE


# List all modules added by the user
def list_module_page(update, context):
    query = update.callback_query
    if len(modules) == 0:
        query.edit_message_text("No modules added yet!",
                                reply_markup=return_keyboard())
    else:
        text = "Here is the list of your modules:\n\n"
        for x in modules:
            text = text + x + "\n"
        query.edit_message_text(text,
                                reply_markup=return_keyboard())


########## KEYBOARDS ##########

# All functions here are appended with _keyboard for consistency
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Send me your NUSMods timetable",
                                    callback_data='m1')],
                [InlineKeyboardButton("Change settings for reminders for my lessons and exams",
                                    callback_data='m2')],
                [InlineKeyboardButton("See module-specific information from your lecturers",
                                    callback_data='m3')],
                [InlineKeyboardButton("Learn more about what I can do for you",
                                    callback_data='m4')],
                [InlineKeyboardButton("Manually add module(s)",
                                    callback_data='m5')],
                [InlineKeyboardButton("List my module(s)",
                                    callback_data='m6')]
                ]
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
    return ("Invalid input\! Please send me a url link instead\.")


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


def add_module_msg_1():
    return ("Here you can manually input your module\(s\)\.")


def add_module_msg_2():
    return (" added\! You may continue adding more module\(s\)\.")


########## HANDLERS ##########

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1130956112:AAHJvZVA3eblWpWSfTT4JF2E8mO4Wn1Xtqo', use_context=True)

    dp = updater.dispatcher

    timetable_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(timetable_page, pattern='m1')],
        states={TIMETABLE: [MessageHandler(Filters.regex(r'https:\/\/nusmods\.com(.*)'), timetable_input_page),
                            MessageHandler(Filters.all, invalid_input_page)]},
        fallbacks=[]
    )

    add_module_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(module_page, pattern='m5')],
        states={ADD_MODULE: [MessageHandler(Filters.text, module_page_2)]},
        fallbacks=[]
    )

    dp.add_handler(timetable_conv)
    dp.add_handler(add_module_conv)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu_page, pattern='main'))
    dp.add_handler(CallbackQueryHandler(timetable_page, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(settings_page, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(information_page, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(help_page, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(module_page, pattern='m5'))
    dp.add_handler(CallbackQueryHandler(list_module_page, pattern='m6'))

    dp.add_error_handler(error)

    logger.info("Starting NUSMods Telebot...")
    updater.start_polling()
    logger.info("Bot is running!")
    updater.idle()


if __name__ == '__main__':
    main()