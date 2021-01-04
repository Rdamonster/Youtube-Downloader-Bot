from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("تابع جديدنا", url="https://t.me/disco3")],
        [InlineKeyboardButton(
            "ابلاغ عن خطا😊", url="https://t.me/riida")]
    ])
    welcomed = f"مرحبا <b>{message.from_user.first_name}</b>\n/help لعرض قائمة المساعده"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
