from aiogram import types

buttons = ["Выбрать класс", "Добавить информацию", "Карточка персонажа", "Правила"]
rules = ["Все", "Общие", "Характеристики", "Бой", "Нетраннинг", "Выпустите меня отсюда!"]
classes = ["Рокербой", "Соло", "Нетраннер", "Техник"]
class_icons = ["char_icons/rocker.png", "char_icons/solo.png", "char_icons/net.png", "char_icons/tech.png"]
admin = ["Плотный @all", "Информируй меня полностью"]
admin_msg = ["Базара не будет"]

def make_kb():
    kb = [
        [
            types.KeyboardButton(text=b) for b in buttons[:2]
        ],
        [
            types.KeyboardButton(text=b) for b in buttons[2:]
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Жду на КМФ"
    )

    return keyboard

def make_kb_rules():
    kb = [
        [
            types.KeyboardButton(text=b) for b in rules[:2]
        ],
        [
            types.KeyboardButton(text=b) for b in rules[2:4]
        ],
        [
            types.KeyboardButton(text=rules[4])
        ],
        [
            types.KeyboardButton(text=rules[5])
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Жду на КМФ"
    )

    return keyboard    

def make_kb_classes():
    kb = [
        [
            types.KeyboardButton(text=b) for b in classes[:2]
        ],
        [
            types.KeyboardButton(text=b) for b in classes[2:]
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Жду на КМФ"
    )

    return keyboard


def make_kb_admin():
    kb = [
        [
            types.KeyboardButton(text=b) for b in admin
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Здесь был IT"
    )

    return keyboard

def make_kb_admin_msg():
    kb = [
        [
            types.KeyboardButton(text=b) for b in admin_msg
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Здесь был IT"
    )

    return keyboard