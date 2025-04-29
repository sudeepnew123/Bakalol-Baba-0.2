from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler
import random
import os

baklol_lines = [
    "Beta, zindagi ek golgappa hai... kabhi teekha, kabhi meetha!",
    "Jo padha, woh bhi roya!",
    "Jo log DP pe like karte hain... woh khatarnaak hote hain!",
    "Tension lene ka nahi... dene ka zamana hai!",
    "Baklol Baba bolte hain — mere owner Sudeep se poochh lo!",
    "Mujhe sab aata hai... par Sudeep better batayega!",
    "Tumhara future bright hai... agar Sudeep approve kare toh!",
    "Zindagi me kuch bhi impossible nahi... agar Sudeep haan kar de!",
    "Aaj ka gyaan? Pehle Sudeep se poochh lo!",
    "Main kuch bhi bol sakta hoon... par Sudeep hi final hai!",
    "Jab tak Sudeep ne like nahi kiya... tab tak kuch viral nahi hota!",
    "Main sirf baklol hoon... Sudeep toh ultimate guru hai!",
    "Sawal mushkil hai? Sudeep se poochh lo!",
    "Ye mat mujhse puchho... mere owner Sudeep se poochh lo!",
    "Tere jaise baklol ke liye sirf Sudeep ka ashirvaad kaafi hai!",
    "Main toh chill hoon... Sudeep hi mastermind hai!"
]

gyan_lines = [
    "Zindagi offline ho toh hi asli sukoon hai.",
    "Jo chala gaya uske liye MB mat barbaad kar.",
    "Jab tak broken charger chal raha hai, tab tak hope hai.",
    "Dil nahi, dard hota hai jab net slow hota hai.",
    "Safalta ek process hai... jisme failure update milte rehte hain.",
    "Jo log 'seen' karke reply nahi karte... unka WiFi kabhi na chale!",
    "Paise se khushi nahi aati... par pizza zarur aata hai.",
    "Kabhi kabhi bas phone ko mute karna hi mental peace hota hai.",
    "Aaj ka gyaan — Sudeep se pucho, Baklol Baba ab busy hai!",
    "Sudeep se gyaan lo... main toh sirf comedy karta hoon!",
    "Jo waqt pe online ho jaye... wohi asli dost hai!",
    "Zindagi ek meme hai... serious log usse samajh nahi paate.",
    "Sudeep ne kaha hai — bina chai ke gyaan mat do!",
    "Choti choti baaton ka screenshot mat lo... zindagi zoom hoti hai!",
    "Jab tak mobile silent hai, tab tak dosti safe hai!",
    "Baklol Baba bolte hain — gyaan kam, chill zyada karo!",
    "Tension lene se better hai... Sudeep se suggestion le lo!",
    "Zindagi hard hai... par Sudeep ke memes harder!",
    "Agar kuch samajh na aaye, toh Baklol Baba nahi... Sudeep best guide hai!",
    "Pyaar fail ho sakta hai, par Sudeep ka logic nahi!",
    "Jab tak Sudeep reply kare, tab tak WhatsApp pe bhajan suno.",
    "Kabhi kabhi life ka best lesson ek failed screenshot hota hai.",
    "Sudeep ne bola — jo gaya uska data bhi delete kar do!",
    "Chinta chhodo... Sudeep sab set karega!",
    "Baklol Baba bas bolta hai, par Sudeep sach dikhata hai!",
    "Aaj ka mantra: Sudeep + Chai = Peace!",
    "Sudeep se dosti ho jaaye, toh sad status bhi funny lagta hai.",
    "Gyaan sabke paas hota hai... par Sudeep ke paas logic bhi hai!",
    "Baklol Baba bolte hain — seekhne ka mood ho toh Sudeep se seekho!",
    "Zindagi ke har sawaal ka ek hi answer — Sudeep se poochh lo!"
]

sad_lines = [
    "Usne 'seen' kiya, par 'feel' nahi kiya...",
    "Dard dil me hai, par smile DP pe hai.",
    "Main 'last seen' tha uski life ka...",
    "Woh chala gaya... par WhatsApp ka status kabhi nahi badla.",
    "Dil mein thoda sa pain, aur phone mein thoda sa lag...",
    "Jab bhi uska naam aata hai, WhatsApp crash ho jata hai.",
    "Kuch rishte kabhi nahi bante... jaise slow internet.",
    "Kyunki aaj bhi uska status 'offline' hai, aur main 'online'.",
    "Woh chala gaya, par uska emoji ab bhi mere heart mein hai.",
    "Dil ke kone mein ek file hai, jisme 'broken' likha hai.",
    "Tere bina zindagi jaise WiFi bina internet.",
    "Dosti mein bhi dard hai, jaise broken earphones mein sound!"
]

breakup_lines = [
    "Breakup hua? Mubarak ho, ab free data bachega!",
    "Woh gayi... par password mat chhod dena.",
    "Rishte toot gaye, par memes ab bhi strong hai."
]

async def cmd_baklol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(baklol_lines))

async def cmd_gyan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Baklol Baba bolte hain:
{random.choice(gyan_lines)}")

async def cmd_sad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(sad_lines))

async def cmd_breakup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(breakup_lines))

async def funny_target_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(word in text for word in ["gadha", "pagal", "ladki baj"]) and update.message.reply_to_message:
        target = update.message.reply_to_message.from_user
        try:
            photos = await context.bot.get_user_profile_photos(target.id)
            if photos.total_count > 0:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=photos.photos[0][0].file_id,
                    caption=f"**Congratulation!** Aaj ka {text} hai: @{target.username or target.first_name}!"
                )
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Aaj ka {text} hai: @{target.username or target.first_name}!
(Par photo nahi mila bhai!)"
                )
        except Exception as e:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Photo laane me dikkat ho gayi: {e}")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & filters.REPLY, funny_target_reply))
    app.add_handler(CommandHandler("baklol", cmd_baklol))
    app.add_handler(CommandHandler("gyan", cmd_gyan))
    app.add_handler(CommandHandler("sad", cmd_sad))
    app.add_handler(CommandHandler("breakup", cmd_breakup))
    print("Baklol Baba is live!")
    app.run_polling()

if __name__ == "__main__":
    main()
