import logging
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

CREDENTIALS_PATH = 'credentials.json'
SPREADSHEET_ID = '1H7mfHjsdNx5q_E5vSou5UkWdGqBFZyaVULgnRsiG1ZY'
BOT_TOKEN = '6318211039:AAHPxLSEdjwCG1IkNvAMhs-cMumVQ_8pgsk'

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        # Получение данных из сообщения
        login = message.from_user.username
        text = message.text
        timestamp = datetime.now().strftime('%d.%m.%Y %H:%M')

        # Запись данных в Google Sheets
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).sheet1
        row = [login, text, timestamp]
        sheet.append_row(row)

    except Exception as e:
        # Логгирование ошибки
        logging.error(f'Error occurred: {e}')
        with open('error_log.txt', 'a') as file:
            file.write(f'{datetime.now()} - Error: {e}\n')

if __name__ == '__main__':
    # Запуск бота
    dp.start_polling()


