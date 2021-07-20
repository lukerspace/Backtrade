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
FINANCIAL_URL = 'https://data.alpaca.markets/v2/reference/financials/'
API_MAX_LENGTH = 100