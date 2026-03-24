import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

# ===== LOAD TOKEN =====
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===== CONFIG =====
REGISTRATION_LINK = "https://www.lottery7r.com/#/register?invitationCode=4114418553449"

VIDEO_PATH = "video.mp4"
APK_PATH = "app.apk"

# ===== MAIN FUNCTION =====
async def send_full_message(user_id, name, context):

    # ===== 1. CLEAN WELCOME =====
    welcome_text = f"""
👋 Hi {name}

Tumhari Join Request mil gayi hai ✅  
Jaldi approve ho jayegi ⏳  

📦 APK + Video Guide niche diya hai 👇
"""
    await context.bot.send_message(chat_id=user_id, text=welcome_text)

    # ===== 2. VIDEO WITH LINK =====
    await context.bot.send_video(
        chat_id=user_id,
        video=open(VIDEO_PATH, "rb"),
        caption=f"""
{REGISTRATION_LINK}
"""
    )

    # ===== 3. APK (LIKE YOUR IMAGE STYLE) =====
    await context.bot.send_document(
        chat_id=user_id,
        document=open(APK_PATH, "rb"),
        filename="NUMBER PANAL 2.0.apk",
        caption="""⏩ Brand New Store Released ✔️

👀 Set-Up Video Dekh Lo Sab Log ✅"""
    )


# ===== JOIN REQUEST HANDLER =====
async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    # ONLY SEND TO USER
    await send_full_message(user.id, user.first_name, context)

    # ❌ DO NOT APPROVE
    # ❌ DO NOT SEND TO ADMIN


# ===== RUN BOT =====
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(handle_join))

print("🔥 BOT RUNNING (JOIN REQUEST ONLY)...")
app.run_polling()