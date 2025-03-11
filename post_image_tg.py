import telegram



def post_image(filepath, chat_id, token, caption=None):
    bot = telegram.Bot(token=token)
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file, caption=caption)
