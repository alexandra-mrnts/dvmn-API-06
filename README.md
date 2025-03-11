# Comics telegram publisher

A script that fetch random xkcd comics image and automatically post it to a Telegram channel.


### How to install

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Your telegram chat ID and access token should be added to the .env file.
```
TG_CHAT_ID = '@mychat'
TG_TOKEN = '7219856276:AAGKGrSZwgpZf74JGEIBlAjiAosaVjBf4Tw'
```

### How to use
Run the following command:
```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
