from datetime import datetime
from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default import phone_number
from keyboards.inline import option, courses
from states.register import RegisterState
from utils.file_manager import append, read
from utils.id_generator import generate_new_id

router = Router()

@router.message(F.text == '/start')
async def start_handler(message: Message, state: FSMContext):
    users = read('users')
    is_found = False
    for user in users:
        if str(user[1]) == str(message.from_user.id):
            is_found = True
            break

    if not is_found:
        text = "👋 Welcome to Najot Ta'lim! Please register to use our bot."
        await message.answer(text=text, reply_markup=option)
        await state.set_state(RegisterState.full_name)
    else:
        text = "Choose your favourite courses here ➡️"
        await message.answer(text=text, reply_markup=courses)


@router.callback_query(RegisterState.full_name)
async def option_handler(call: CallbackQuery, state: FSMContext):
    await state.update_data(option=call.data)
    if call.data == 'register':
        text = "Please enter your full name"
        await call.message.answer(text=text)
        await state.set_state(RegisterState.full_name)
    else:
        text = """NajotEduBot is designed to help prospective students register
for Najot Ta’lim training courses easily via Telegram. It guides users through name collection, course selection, schedule choice, and final confirmation — all within a user-friendly chat flow.
contact: @Mahmud_Rustamov"""
        await call.message.answer(text=text)
        return


@router.message(RegisterState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Please enter your phone number"
    await message.answer(text=text, reply_markup=phone_number)
    await state.set_state(RegisterState.phone_number)


@router.message(RegisterState.phone_number, F.content_type == ContentType.CONTACT)
async def phone_number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    text = "Now, Please enter your age"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.age)



@router.message(RegisterState.age)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    if data:
        new_id = generate_new_id(filename="users")
        user_id = message.from_user.id
        full_name = data['full_name']
        phone_num = data['phone_number']
        age = data['age']
        created_at = datetime.now()
        updated_at = None

        user = [new_id, user_id, full_name, phone_num, age, created_at, updated_at]
        append(filename="users", data=user)
        text = "Successfully registered! ✅\nChoose your favourite courses here ➡️"
        await message.answer(text=text, reply_markup=courses)
    else:
        text = "Something went wrong"
        await message.answer(text=text)



@router.callback_query()
async def course_handler(call: CallbackQuery, state: FSMContext):
    await state.update_data(courses=call.data)
    course_name = call.data.lower()
    if course_name not in ['python', 'go', 'flutter', 'full_stack', 'html', 'c++', 'java', 'data', 'swift']:
        text = "Course is not found!!!"
        await call.message.answer(text=text)
        return

    user_id = call.from_user.id
    data = read("courses")
    is_found = False
    for course in data:
        if str(course[1]) == str(user_id) and course[2] == course_name:
            is_found = True
            break

    if not is_found:
        new_id = generate_new_id(filename="courses")
        created_at = datetime.now()
        updated_at = None
        course = [new_id, user_id, course_name, created_at, updated_at, updated_at]
        append('courses', course)
        text = "You have successfully enrolled in this course! ✅"
        await call.message.answer(text=text)
    else:
        text = "You have already enrolled in this course! 🙅"
        await call.message.answer(text=text)






