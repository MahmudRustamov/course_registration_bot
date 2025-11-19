from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text = "Share my phone number", request_contact=True)
    ]], resize_keyboard=True
)

confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yes"), KeyboardButton(text="No")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)