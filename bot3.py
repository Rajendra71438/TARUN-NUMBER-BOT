import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes
)

# ===== LOAD TOKEN =====
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===== CONFIG =====
ADMIN_ID = 8340435729
ADMIN_USERNAME = "trk_atil_01"
REGISTRATION_LINK = "https://www.lottery7r.com/#/register?invitationCode=4114418553449"

VIDEO_PATH = "video.mp4"
APK_PATH = "app.apk"
VOICE_PATH = "voice.ogg"

# ===== COMMON FUNCTION =====
async def send_full_message(user_id, name, context):

    keyboard = [
        [InlineKeyboardButton("📞 CONTACT ADMIN 💬", url=f"https://t.me/{ADMIN_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ===== 1. WELCOME =====
    welcome_text = f"""
💸✨ 𝑯𝒊 {name} 👋 ✨💸
━━━━━━━━━━━━━━━━━━━
✅ 𝑻𝒖𝒎𝒉𝒂𝒓𝒊 𝑱𝒐𝒊𝒏 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝒎𝒊𝒍 𝒈𝒂𝒚𝒊 𝒉𝒂𝒊  
⏳ 𝑱𝒂𝒍𝒅𝒊 𝒉𝒊 𝒂𝒑𝒑𝒓𝒐𝒗𝒆 𝒉𝒐 𝒋𝒂𝒚𝒆𝒈𝒊  
━━━━━━━━━━━━━━━━━━━
📦 𝑨𝑷𝑲 • 𝑽𝑰𝑫𝑬𝑶 • 𝑽𝑶𝑰𝑪𝑬 𝑮𝑼𝑰𝑫𝑬  
👇 𝑵𝒊𝒄𝒉𝒆 𝒅𝒊𝒚𝒂 𝒈𝒂𝒚𝒂 𝒉𝒂𝒊  

⚠️ 𝑺𝒂𝒓𝒆 𝒔𝒕𝒆𝒑𝒔 𝒅𝒉𝒚𝒂𝒏 𝒔𝒆 𝒇𝒐𝒍𝒍𝒐𝒘 𝒌𝒂𝒓𝒏𝒂!
━━━━━━━━━━━━━━━━━━━
"""
    await context.bot.send_message(chat_id=user_id, text=welcome_text)

    # ===== VIDEO =====
    await context.bot.send_video(
        chat_id=user_id,
        video=open(VIDEO_PATH, "rb"),
        caption="🎥 𝑽𝑰𝑫𝑬𝑶 𝑮𝑼𝑰𝑫𝑬\n\n⚡ 𝑰𝒔 𝒗𝒊𝒅𝒆𝒐 𝒌𝒐 𝒅𝒉𝒚𝒂𝒏 𝒔𝒆 𝒅𝒆𝒌𝒉𝒐!"
    )

    # ===== APK =====
    await context.bot.send_document(
        chat_id=user_id,
        document=open(APK_PATH, "rb"),
        caption="""📲 𝑨𝑷𝑲 𝑫𝑶𝑾𝑵𝑳𝑶𝑨𝑫

💯 𝐏𝐑𝐎𝐅𝐈𝐓 𝟏𝟎𝟎% 𝐆𝐄𝐑𝐀𝐍𝐓𝐘 👑

💘 𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐌𝐈𝐍𝐈𝐌𝐔𝐌 ₹200 💸

💘 𝐓𝐇𝐄𝐍 100% 𝐇𝐀𝐂𝐊 𝐀𝐂𝐓𝐈𝐕𝐄 🌟

━━━━━━━━━━━━━━━━━━━
✈️ 100% 𝑺𝒖𝒓𝒆 𝑺𝒉𝒐𝒕 ✅  
↪️ 0 𝑳𝒆𝒗𝒆𝒍 𝑴𝒂𝒊𝒏𝒕𝒂𝒊𝒏 𝑶𝒏𝒍𝒚 ✅
━━━━━━━━━━━━━━━━━━━
"""
    )

    # ===== VOICE =====
    await context.bot.send_voice(
        chat_id=user_id,
        voice=open(VOICE_PATH, "rb"),
        caption="🎧 𝑰𝑴𝑷𝑶𝑹𝑻𝑨𝑵𝑻 𝑽𝑶𝑰𝑪𝑬 𝑮𝑼𝑰𝑫𝑬\n\n⚠️ 𝑰𝒔𝒆 𝒅𝒉𝒚𝒂𝒏 𝒔𝒆 𝒔𝒖𝒏𝒏𝒂!"
    )

    # ===== REGISTRATION =====
    await context.bot.send_message(
        chat_id=user_id,
        text=f"""
📝💸 𝑹𝑬𝑮𝑰𝑺𝑻𝑹𝑨𝑻𝑰𝑶𝑵 𝑺𝑻𝑬𝑷 💸📝  

👉 𝑨𝒃𝒉𝒊 𝒓𝒆𝒈𝒊𝒔𝒕𝒆𝒓 𝒌𝒂𝒓𝒐 👇  
🔗 {REGISTRATION_LINK}
"""
    )

    # ===== FINAL =====
    await context.bot.send_message(
        chat_id=user_id,
        text="""
━━━━━━━━━━━━━━━━━━━  
⬇️ 𝑲𝒐𝒊 𝒑𝒓𝒐𝒃𝒍𝒆𝒎 𝒂𝒂𝒚𝒆? ⬇️  
💬 𝑨𝒅𝒎𝒊𝒏 𝒔𝒆 𝒕𝒖𝒓𝒂𝒏𝒕 𝒄𝒐𝒏𝒕𝒂𝒄𝒕 𝒌𝒂𝒓𝒐  
━━━━━━━━━━━━━━━━━━━
""",
        reply_markup=reply_markup
    )


# ===== JOIN REQUEST ONLY =====
async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    # send to user
    await send_full_message(user.id, user.first_name, context)

    # send to admin
    await send_full_message(ADMIN_ID, user.first_name, context)

    # ❌ DO NOT APPROVE REQUEST


# ===== RUN =====
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(handle_join))

print("🔥 PRO BOT RUNNING...")
app.run_polling()