import os
from dotenv import *
import sys

abs_path=os.path.abspath(os.getcwd())
pre_path = os.path.abspath("../backtrade/py/")
model_path=os.path.abspath("../backtrade/apps/")
vix_path=os.path.abspath("../backtrade/vix/")

sys.path.append(pre_path)
sys.path.append(abs_path)
sys.path.append(model_path)
sys.path.append(vix_path)
load_dotenv()

# ALPACA API 
API_MAX_LENGTH = 100
FINANCIAL_URL = 'https://data.alpaca.markets/v2/reference/financials/'
API_KEY=os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
BARS_URL = os.getenv("BASE")
HEADERS = {'APCA-API-KEY-ID': API_KEY,'APCA-API-SECRET-KEY': SECRET_KEY}

# IEX_API
IEX_API=os.getenv("IEX_API")
PASSWORD="0000"
DBUSER="root"

print("CONFIG DIRECTORY SETUP IS DONE")