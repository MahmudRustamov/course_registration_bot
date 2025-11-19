from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.file_manager import read

option = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👉 Register", callback_data="register"),
            InlineKeyboardButton(text="ℹ️ About", callback_data="about"),
        ]
    ]
)

courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python", callback_data="python"),
            InlineKeyboardButton(text="Java", callback_data="java"),
            InlineKeyboardButton(text="Go", callback_data="go"),
        ],
        [
            InlineKeyboardButton(text="Html", callback_data="html"),
            InlineKeyboardButton(text="Data Science", callback_data="data"),
            InlineKeyboardButton(text="C++", callback_data="c++"),
        ],
        [
            InlineKeyboardButton(text="Flutter", callback_data="flutter"),
            InlineKeyboardButton(text="Swift", callback_data="swift"),
            InlineKeyboardButton(text="Full stack", callback_data="full_stack"),
        ],
    ]
)
