"""Ініціалізація модулів Initialization of modules"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Зробити: Видалити непотрібні кнопки (коли все буде зроблено і все буде працювати, як терба).
"""Ініціалізація кнопок Button initialization"""
b1 = KeyboardButton('/add_product')
b2 = KeyboardButton('/cancel')
b3 = KeyboardButton('/view')

# Заміняє звичайну клав-ру на кнопки; Replaces the usual keyboard with buttons
url_info = InlineKeyboardButton(text='Дивитись інструкцію', url='https://docs.google.com/document/d/1BllFcW2WAJjunn8_1yRox-jM75lK1O6NWZjhyyK15bI/edit?usp=sharing')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
url = InlineKeyboardMarkup(row_width=1)
kb = InlineKeyboardMarkup().row(
    InlineKeyboardButton('<-', callback_data='prev'),
    InlineKeyboardButton('->', callback_data='next')
)

# Додавання кнопок, розположення; Adding buttons, location
url.add(url_info)
kb_client.row(b1, b2).add(b3)