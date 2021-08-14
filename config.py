import os
from dotenv import *
import sys

abs_path=os.path.abspath(os.getcwd())
pre_path = os.path.abspath("../backtrade/py/")
model_path=os.path.abspath("../backtrade/apps/")

sys.path.append(pre_path)
sys.path.append(abs_path)
sys.path.append(model_path)

print("DIRECTORY SETUP DONE")

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

IEX_API=os.getenv("IEX_API")

