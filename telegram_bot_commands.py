from telegram import Update
from telegram.ext import ContextTypes
from process import data_processor
from work_file import read_file

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/1 - ID\n/2 - ФИО\n/3 - День рождения\n/4 - Успеваемость\n/5 - Пол\n/6 - Все данные\n/0 - Выход')

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 1)))

async def fio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 2)))

async def birthday_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 3)))

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 4)))

async def sex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 5)))

async def all_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 6)))

async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(data_processor(read_file('processing_model.csv'), 0)))