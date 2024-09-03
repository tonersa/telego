touch bot.py
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install python-telegram-bot
pip freeze > requirements.txt
