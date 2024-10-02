import sys, os, logging, asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.client.default import DefaultBotProperties

from consts import *
from db import *
from keyboards import *

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

Admins = [370394115]

dp = Dispatcher()
router = Router()
dp.include_router(router)

# BOT --------------------------------------------------------------------

class UserStates(StatesGroup):
    Start = State()
    Classes = State()
    Info = State()
    Rules = State()

class AdminStates(StatesGroup):
    Start = State()
    Msg = State()

async def send_text_to_users(ids, message_text):
    for chat_id in ids:
        if chat_id == None:
            continue
        try:
            await bot.send_message(chat_id=chat_id, text=message_text)
            print(f"Message sent to {chat_id}")
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")

async def send_video_to_users(ids, file_id):
    for chat_id in ids:
        if chat_id is None:
            continue
        try:
            await bot.send_video(chat_id=chat_id, video=file_id)
            print(f"Sent to {chat_id}")
        except Exception as e:
            print(f"Error sending to {chat_id}: {e}")

async def send_photo_to_users(ids, file_id):
    for chat_id in ids:
        if chat_id == None:
            continue
        try:
            await bot.send_photo(chat_id=chat_id, photo=file_id)
            print(f"Sent to {chat_id}")
        except Exception as e:
            print(f"Error sending to {chat_id}: {e}")


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    if message.chat.id in Admins:
        await message.answer(
            text=f"Hello admin, выбери что делать будем?",
            reply_markup=make_kb_admin())
        await state.set_state(AdminStates.Start)
    else:
        add_member(message.from_user.username, message.chat.id)
        await message.answer(
            text=welcome,
            reply_markup=make_kb()
        )
        await state.set_state(UserStates.Start)

@router.message(UserStates.Start, F.text.in_(buttons))
async def user_button(message: Message, state: FSMContext):
    if message.text == buttons[0]:
        await message.answer(
            text=class_desc, reply_markup=make_kb_classes()
        )
        await state.set_state(UserStates.Classes)
    elif message.text == buttons[1]:
        await message.answer(
            text=info_desc, reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(UserStates.Info)
    elif message.text == buttons[2]:
        clss = get_user_class(message.chat.id)
        if clss in classes:
            cid = classes.index(clss)
            image_from_pc = FSInputFile(class_icons[cid])
            result = await message.answer_photo(
                image_from_pc,
                caption=character_descs[cid]
            )
        else:
            await message.answer(
                text=no_class
            )
    elif message.text == buttons[3]:
        await message.answer(
            text="Штош, почитаем",
            reply_markup=make_kb_rules()
        )
        await state.set_state(UserStates.Rules)

@router.message(UserStates.Rules, F.text.in_(rules))
async def rules_button(message: Message, state: FSMContext):
    if message.text == rules[0]:
        for r in rules_txt[:-1]:
            await message.answer(
                text=r,
                reply_markup=make_kb_rules()
            )
    elif message.text == rules[1]:
        for r in rules_txt[:3]:
            await message.answer(
                text=r,
                reply_markup=make_kb_rules()
            )
    elif message.text == rules[2]:
        await message.answer(
            text=rules_txt[3],
            reply_markup=make_kb_rules()
        )
    elif message.text == rules[3]:
        await message.answer(
            text=rules_txt[4],
            reply_markup=make_kb_rules()
        )
    elif message.text == rules[4]:
        await message.answer(
            text=rules_txt[5],
            reply_markup=make_kb_rules()
        )
    elif message.text == rules[5]:
        await message.answer(
            text=rules_txt[-1],
            reply_markup=make_kb()
        )
        await state.set_state(UserStates.Start)

@router.message(UserStates.Classes)
async def class_button(message: Message, state: FSMContext):
    fill_class(message.chat.id, message.text)
    await message.answer(
        text="Сохранил",
        reply_markup=make_kb()
    )
    await state.set_state(UserStates.Start)

@router.message(UserStates.Info)
async def info_button(message: Message, state: FSMContext):
    fill_info(message.chat.id, message.text)
    await message.answer(
        text="Сохранил",
        reply_markup=make_kb()
    )
    await state.set_state(UserStates.Start)

@router.message(AdminStates.Start, F.text.in_(admin))
async def admin_start(message: Message, state: FSMContext):
    if message.text == admin[0]:
        await message.answer(
            text="Чего базаришь?", reply_markup=make_kb_admin_msg()
        )
        await state.set_state(AdminStates.Msg)
    elif message.text == admin[1]:
        mems = get_all_info()
        for m in mems:
            await message.answer(
                text=m, reply_markup=ReplyKeyboardRemove()
            )
        await message.answer(
            text="Вывел", reply_markup=make_kb_admin()
        )
        await state.set_state(AdminStates.Start)


@router.message(AdminStates.Msg, F.photo)
async def admin_msg_photo(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    await send_photo_to_users(get_all_chat_ids(), file_id)
    await message.answer(
        text="Базар оформлен", reply_markup=make_kb_admin()
    )
    await state.set_state(AdminStates.Start)

@router.message(AdminStates.Msg, F.video)
async def admin_msg_video(message: Message, state: FSMContext):
    file_id = message.video.file_id
    await send_video_to_users(get_all_chat_ids(), file_id)
    await message.answer(
        text="Базар оформлен", reply_markup=make_kb_admin()
    )
    await state.set_state(AdminStates.Start)


@router.message(AdminStates.Msg)
async def admin_msg_text(message: Message, state: FSMContext):
    if message.text == admin_msg[0]:
        await message.answer(
            text="Базара нет", reply_markup=make_kb_admin()
        )
        await state.set_state(AdminStates.Start)
    else:
        await send_text_to_users(get_all_chat_ids(), message.text)
        await message.answer(
            text="Базар оформлен", reply_markup=make_kb_admin()
        )
        await state.set_state(AdminStates.Start)

@router.message(UserStates.Start)
async def unknown_command_st(message: types.Message):
    await message.answer(text="Неверная команда.")

@router.message()
async def unknown_command(message: types.Message):
    await message.answer(text="Введите /start для выбора опций.")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())