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

TIMETABLE, TEST = range(2)

modules = []


########## STATES ##########

def start(update, context):
    update.message.reply_text(main_menu_msg(),
                              reply_markup=main_menu_keyboard(),
                              parse_mode=ParseMode.MARKDOWN_V2)


def timetable_input(update, context):
    update.message.reply_text(timetable_input_msg(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return ConversationHandler.END


def invalid_input(update, context):
    update.message.reply_text(invalid_input_msg(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return TIMETABLE


def cancel(update, context):
    update.message.reply_text(cancel_msg(),
                              parse_mode=ParseMode.MARKDOWN_V2)
    return ConversationHandler.END


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


def test_page(update, context):
    query = update.callback_query
    query.edit_message_text(text=add_module_msg_1(),
                            parse_mode=ParseMode.MARKDOWN_V2)
    return TEST

def test_page_2(update, context):
    new_text = update.message.text + add_module_msg_2()
    update.message.reply_text(text=new_text,
                              parse_mode=ParseMode.MARKDOWN_V2)
    modules.append(update.message.text)
    return TEST

def list_test_page(update, context):
    query = update.callback_query
    if len(modules) == 0:
        query.edit_message_text("No modules added yet! Type /start to return.")
    else:
        text = "Here is the list of your modules:\n\n"
        for x in modules:
            text = text + x + "\n"
        text = text + "\nType /start to return."
        query.edit_message_text(text)


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
                                    callback_data='test')],
                [InlineKeyboardButton("List my module(s)",
                                    callback_data='list_test')]
                ]
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


########## MESSAGES ##########

# All functions here are appended with _msg for consistency
def main_menu_msg():
    return ("*Hi there\! I am the NUSMods Telebot\.*\nIf it is your first time "
            "using this bot, please select 'Learn more' below to learn "
            "what I can do for you\.")

def timetable_msg():
    return ("*Timetable page:*\n"
            "Send me a link to your NUSMods timetable for me to sync\!\n"
            "If you wish to go back, type /cancel\.")

def timetable_input_msg():
    return ("Your timetable is now synced\! Type \/start to go back to the main page\.")

def invalid_input_msg():
    return ("Invalid input\! Please send me a url link instead\.")

def cancel_msg():
    return ("Cancelled\! Type \/start to go back to the main page\.")

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
    return ("Manually input your module\(s\)\. Type \/cancel when you are done\.")

def add_module_msg_2():
    return (" added\! Continue adding modules, or if you are done, type \/cancel\.")


########## HANDLERS ##########

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token="1130956112:AAHJvZVA3eblWpWSfTT4JF2E8mO4Wn1Xtqo", use_context=True)

    dp = updater.dispatcher

    timetable_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(timetable_page, pattern='m1')],
        states={TIMETABLE: [MessageHandler(Filters.regex(r'https:\/\/nusmods\.com(.*)'), timetable_input),
                            CommandHandler('cancel', cancel),
                            MessageHandler(Filters.all, invalid_input)]},
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    add_module_manually_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(test_page, pattern='test')],
        states={TEST: [CommandHandler('cancel', cancel),
                       MessageHandler(Filters.text, test_page_2)]},
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(timetable_conv)
    dp.add_handler(add_module_manually_conv)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu_page, pattern='main'))
    dp.add_handler(CallbackQueryHandler(timetable_page, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(settings_page, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(information_page, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(help_page, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(test_page, pattern='test'))
    dp.add_handler(CallbackQueryHandler(list_test_page, pattern='list_test'))

    dp.add_error_handler(error)

    logger.info("Starting NUSMods Telebot...")
    updater.start_polling()
    logger.info("Bot is running!")
    updater.idle()


if __name__ == '__main__':
    main()