import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')


def help_command(update, context):
    update.message.reply_text('Ask google if you need help')
