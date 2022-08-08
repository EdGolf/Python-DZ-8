from telegram.ext import ApplicationBuilder, CommandHandler
from telegram_bot_commands import *
from process import data_processor
from work_file import read_file

app = ApplicationBuilder().token("1234567890").build()

app.add_handler(CommandHandler("f1", help_command))          
app.add_handler(CommandHandler("1", id_command))             
app.add_handler(CommandHandler("2", fio_command))            
app.add_handler(CommandHandler("3", birthday_command))       
app.add_handler(CommandHandler("4", progress_command))       
app.add_handler(CommandHandler("5", sex_command))            
app.add_handler(CommandHandler("6", all_data_command))       
app.add_handler(CommandHandler("0", exit_command))          

print('server start')

app.run_polling()
