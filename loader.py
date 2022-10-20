from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from database import DB

db = DB.Database('namedb.db')
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
