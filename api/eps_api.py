import os
import sys
from flask import *
from datetime import *
pre_path = os.path.abspath("../backtrade/sql")
sys.path.append(pre_path)
from ark_eps import ark_eps_select

ark_eps_select('TDOC')
ark_eps_select('TSLA')