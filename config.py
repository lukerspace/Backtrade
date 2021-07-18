import os
from dotenv import *

load_dotenv()

API_KEY=os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")

HEADERS = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': SECRET_KEY
}
BARS_URL = os.getenv("BARS_URL")

API_MAX_LENGTH = 100

# {"action": "auth", "key": "PK6LZPXUPE95ME620OBI", "secret": "IFRq60PngeddhIgjMCY4nPSERaVcoQwVDnaoA68f"}