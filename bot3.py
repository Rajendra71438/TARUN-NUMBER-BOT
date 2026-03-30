import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID"))

MSG_ID_1 = int(os.getenv("MSG_ID_1"))   # first msg
VIDEO_MSG_ID_1 = int(os.getenv("VIDEO_MSG_ID_1"))
APK_MSG_ID = int(os.getenv("APK_MSG_ID"))
VIDEO_MSG_ID_2 = int(os.getenv("VIDEO_MSG_ID_2"))
VOICE_MSG_ID = int(os.getenv("VOICE_MSG_ID"))
MSG_ID_2 = int(os.getenv("MSG_ID_2"))   # last msg


async def send_full_message(user_id, context):

    for msg_id in [
        MSG_ID_1,
        VIDEO_MSG_ID_1,
        APK_MSG_ID,
        VIDEO_MSG_ID_2,
        VOICE_MSG_ID,
        MSG_ID_2
    ]:
        await context.bot.copy_message(
            chat_id=user_id,
            from_chat_id=SOURCE_CHAT_ID,
            message_id=msg_id
        )
        await asyncio.sleep(2)


async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    await send_full_message(user.id, context)


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join))

print("🔥 BOT RUNNING CORRECTLY...")
app.run_polling()