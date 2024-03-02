from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery


router = Router()
a = []

yes = InlineKeyboardButton(text="Мы вместе!", callback_data='yes')
yboard = [[yes]]
start = InlineKeyboardMarkup(
    inline_keyboard=yboard
)


@router.message(Command("start"))
async def cmd_start(message: Message):
    if len(a) // 10 % 10 == 1:
        if len(a) % 10 == 1:
            candle = "свечей"
    else:
        if len(a) % 10 == 0:
            candle = "свечей"
        elif len(a) % 10 == 1:
            candle = "свеча"
        elif len(a) % 10 == 2 or len(a) % 10 == 3 or len(a) % 10 == 4:
            candle = "свечи"
        elif len(a) % 10 == 5 or len(a) % 10 == 6 or len(a) % 10 == 7 or len(a) % 10 == 8 or len(a) % 10 == 9:
            candle = "свечей"

    caption = "<blockquote>Привет, это Навальный!</blockquote>\n" \
              "Алексей Навальный - герой России, символ мужества, правды. Человек с большой буквы. " \
              "Именно он научил не бояться говорить, действовать. " \
              "Его расследования расскрывали глаза миллионам людей на ложь и коррупцию, воровство со стороны путина и его друзей. " \
              "Алексей посвятил всю жизнь своей стране, мечте и людям, мы должны продолжить его дело, не терпеть и стать свободными. " \
              "Россия будущего недалеко! Спасибо, Алексей, за все!🕯️💔\n\n" \
              "Хотим сообщить, что мы не собираем никакую информацию о вас!\n\n" \
              "Здесь горит {} {}.".format(len(a), candle)
    await message.answer_video(video="****************************************************************************************************", caption=caption, reply_markup=start, parse_mode="HTML")


@router.callback_query(F.data == "yes")
async def cmd_navalny(callback: CallbackQuery):
    a.append("1")
    await callback.message.answer("❤️‍🩹")
    if len(a) // 10 % 10 == 1:
        candle = "свечей"
    else:
        if len(a) % 10 == 0:
            candle = "свечей"
        elif len(a) % 10 == 1:
            candle = "свеча"
        elif len(a) % 10 == 2 or len(a) % 10 == 3 or len(a) % 10 == 4:
            candle = "свечи"
        elif len(a) % 10 == 5 or len(a) % 10 == 6 or len(a) % 10 == 7 or len(a) % 10 == 8 or len(a) % 10 == 9:
            candle = "свечей"

    caption = "<blockquote>Привет, это Навальный!</blockquote>\n" \
              "Алексей Навальный - герой России, символ мужества, правды. Человек с большой буквы. " \
              "Именно он научил не бояться говорить, действовать. " \
              "Его расследования расскрывали глаза миллионам людей на ложь и коррупцию, воровство со стороны путина и его друзей. " \
              "Алексей посвятил всю жизнь своей стране, мечте и людям, мы должны продолжить его дело, не терпеть и стать свободными. " \
              "Россия будущего недалеко! Спасибо, Алексей, за все!🕯️💔\n\n" \
              "Хотим сообщить, что мы не собираем никакую информацию о вас!\n\n" \
              "Здесь горит {} {}.".format(len(a), candle)
    await callback.message.answer_video(video="******************************************************************************************", caption=caption, reply_markup=start, parse_mode="HTML")


@router.message(Command("navalny"))
async def cmd_navalny(message: Message):
    await message.answer("Алексей Навальный:\n@navalny\nhttps://www.instagram.com/navalny\nhttps://youtube.com/@NavalnyRu\nhttps://x.com/navalny\nhttps://navalny.com\nhttps://navalny.shop\n\nЮлия Навальная:\nhttps://x.com/yulia_navalnaya\nhttps://www.instagram.com/yulia_navalnaya\n\nДаша Навальная:\nhttps://www.instagram.com/dasha_navalnaya\n\nМария Певчих:\nhttps://www.instagram.com/maria_pevchikh\nhttps://x.com/pevchikh\n\nИван Жданов:\nhttps://www.instagram.com/ioannz\nhttps://x.com/ioannzh\n@ioannzh\n\nЛеонид Волков:\nhttps://x.com/leonidvolkov\nhttps://instagram.com/leonidvolkov\n\nКира Ярмыш:\nhttps://x.com/kira_yarmysh\nhttps://instagram.com/kira_yarmysh\n\nГеоргий Албуров:\nhttps://instagram.com/alburov\nhttps://x.com/alburov\n\nACF/ФБК:\nhttps://acf.international/\nhttps://fbk.info\nhttps://x.com/fbkinfo\nhttps://www.instagram.com/fbk.info/\n\nКоманда Навального:\n@teamnavalny\nhttps://x.com/teamnavalny\nhttps://www.instagram.com/teamnavalny\n\nПопулярная политика:\n@politica_media\nhttps://www.instagram.com/politica_media\nhttps://youtube.com/@Popularpolitics\n\nНавальный Live:\n@navalnylivechannel\nhttps://x.com/navalnylive\nhttps://www.instagram.com/navalny.live/\nhttps://www.facebook.com/navalnylive\n\nСирена:\n@news_sirena\nhttps://twitter.com/news_sirena\n\nВечная память Алексею и вечный стыд путину и его друзьями.\n<blockquote>Если это произошло, это означает, что мы необыкновенно сильны в этот момент, раз они решили меня убить. Нужно использовать эту силу: не сдаваться, помнить о том, что мы — огромная сила, которая находится под гнетом вот этих вот чуваков плохих лишь потому, что мы не можем осознать, насколько действительно мы сильны. Все, что нужно для торжества зла, — это бездействие добрых людей. Поэтому бездействовать не надо</blockquote>\nДело Алексея Навального будет жить, пока в России и мире есть миллионы неравнодушных людей. Поэтому сдаваться нельзя!\n\nГерои не умирают!\nПутин - убийца! Нет войне! Россия будет свободной!", parse_mode="HTML")


@router.message(Command("code"))
async def cmd_code(message: Message):
    await message.answer("Мы не срываем исходный код этого бота. Код можно просмотреть на сайте https://github.com/")


@router.message()
async def cmd_del(message: Message):
    await message.delete()
