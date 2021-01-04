from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"مرحبا بك في النسخه التجريبيه قم ب ارسال رابط اليوتيوب"
    await message.reply_text(helptxt)
