import os
from dotenv import load_dotenv
from groq import Groq
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CommandHandler

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize clients
client = Groq(api_key=GROQ_API_KEY)

# Translation Function
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    if not user_text:
        return
    
    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        
        prompt = f"""You are a strict bilingual translator between Amharic and English.

Instructions:
1. Detect the language of the input text
2. If input is Amharic → Translate to English
3. If input is English → Translate to Amharic
4. If input is neither Amharic nor English → Respond with: "Error: Only Amharic and English are supported."
5. Return ONLY the translation or the error message, no explanations
Input: {user_text}
Translation:"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile" ,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=500
        )

        translation = response.choices[0].message.content.strip()
        
        if not translation:
            translation = "Error: Could not generate translation."
            
        await update.message.reply_text(translation)
        
    except Exception as e:
        print(f"Translation error: {e}")
        await update.message.reply_text("Error: Translation service unavailable. Please try again later.")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "👋 Welcome to Amharic-English Translator Bot!\n\n"
        "Send me any text in Amharic or English, and I'll translate it for you.\n\n"
    )
    await update.message.reply_text(welcome_msg)

# Main execution
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
   
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))
    
    print(" Bot is starting...")
    
    # Start the bot
    app.run_polling()