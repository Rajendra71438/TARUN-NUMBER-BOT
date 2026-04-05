import os
import asyncio
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

# -------------------- SETUP --------------------
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID"))

MSG_ID_1 = int(os.getenv("MSG_ID_1"))
VIDEO_MSG_ID_1 = int(os.getenv("VIDEO_MSG_ID_1"))
APK_MSG_ID = int(os.getenv("APK_MSG_ID"))
VOICE_MSG_ID = int(os.getenv("VOICE_MSG_ID"))
MSG_ID_2 = int(os.getenv("MSG_ID_2"))

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# -------------------- SEND MESSAGE --------------------
async def send_full_message(user_id, context):
    message_sequence = [
        MSG_ID_1,
        VIDEO_MSG_ID_1,
        APK_MSG_ID,
        VOICE_MSG_ID,
        MSG_ID_2
    ]

    for msg_id in message_sequence:
        try:
            await context.bot.copy_message(
                chat_id=user_id,
                from_chat_id=SOURCE_CHAT_ID,
                message_id=msg_id
            )
            await asyncio.sleep(2)
        except Exception as e:
            logging.error(f"Error sending {msg_id}: {e}")

# -------------------- JOIN REQUEST HANDLER --------------------
async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    try:
        # ❌ DO NOT approve request
        # ✅ Just send messages
        await send_full_message(user.id, context)

    except Exception as e:
        logging.error(f"Join request error: {e}")

# -------------------- MAIN --------------------
def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN missing")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(handle_join_request))

    print("🔥 BOT RUNNING...")
    app.run_polling()

# -------------------- START --------------------
if __name__ == "__main__":
    main()
