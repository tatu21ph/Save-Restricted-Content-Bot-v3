# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "39193718")
API_HASH = os.getenv("API_HASH", "b6ea56ae8203eb4f64592bef337c2e3a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8432397497:AAE37DZ-JbG8Jfaew0rCLr4e72F--UF1tkA")
MONGO_URI = os.getenv("MONGO_DB", "ongodb+srv://supertonskie:<F41br334d14344>@cluster0.oxe2kqv.mongodb.net/?appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5227082629").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", None)) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", None)) # optional with -100
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
