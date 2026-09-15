from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8671730803:AAH7UM6xpFvheilze2A9Ml9-FuKKpsuMF48"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"🛍️ **DIMOAN SHOP – HỆ THỐNG TỰ ĐỘNG**\n\n"
        f"👤 **Khách hàng:** {user.full_name}\n"
        f"🆔 **ID của bạn:** `{user.id}`\n"
        f"💳 **Số dư ví:** 0đ\n\n"
        f"👇 Vui lòng chọn tính năng bên dưới:"
    )
    keyboard = [
        [InlineKeyboardButton("👑 Sản phẩm", callback_data='shop'), InlineKeyboardButton("⚡ Dịch vụ", callback_data='service')],
        [InlineKeyboardButton("💵 Nạp tiền", callback_data='deposit'), InlineKeyboardButton("🕒 Lịch sử", callback_data='history')],
        [InlineKeyboardButton("👤 Tài khoản", callback_data='account'), InlineKeyboardButton("📞 Hỗ trợ", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'deposit':
        user_id = query.from_user.id
        bank_code = "MB"
        account_no = "0987654321"
        account_name = "NGUYEN VAN A"
        content = f"NAP {user_id}"
        
        qr_url = f"https://img.vietqr.io/image/{bank_code}-{account_no}-compact2.png?amount=50000&addInfo={content}&accountName={account_name}"
        
        msg = (
            f"💳 **NẠP TIỀN TỰ ĐỘNG QUA VIETQR**\n\n"
            f"• Ngân hàng: `{bank_code}`\n"
            f"• STK: `{account_no}`\n"
            f"• Chủ TK: `{account_name}`\n"
            f"• Nội dung CK: `{content}`\n\n"
            f"⚠️ **Lưu ý:** Ghi đúng nội dung `{content}` để nạp tự động!"
        )
        await query.message.reply_photo(photo=qr_url, caption=msg, parse_mode="Markdown")
    elif query.data == 'shop':
        await query.message.reply_text("📦 Danh mục sản phẩm đang được cập nhật!")
    elif query.data == 'account':
        await query.message.reply_text(f"👤 Tài khoản: {query.from_user.full_name}\n🆔 ID: `{query.from_user.id}`\n💰 Số dư: 0đ", parse_mode="Markdown")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()
