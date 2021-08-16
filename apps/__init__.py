from posixpath import abspath
from typing import Pattern
from flask import *
from flask_sqlalchemy import SQLAlchemy
import config
from config import *


app=Flask(__name__)

db=SQLAlchemy(app)


# CONFIG
app.secret_key="backtrader"
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["JSON_SORT_KEYS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"]={"pool_pre_ping":True}
app.config['SQLALCHEMY_DATABASE_URI']="mysql://{}:{}@localhost:3306/companies".format(config.DBUSER,config.PASSWORD)

# SIGNAL API
from api.api_signal import appQqqSign,appArkSign,appSpySign
# EPS API
from api.api_eps import appArkEps
# Consolidate
from api.api_consolidate import appSpyConsolidate,appArkConsolidate,appQqqConsolidate


# REGISTER
app.register_blueprint(appQqqSign, url_prefix='/api')
app.register_blueprint(appArkSign, url_prefix='/api')
app.register_blueprint(appSpySign, url_prefix='/api')
# REGITSTER EPS
app.register_blueprint(appArkEps, url_prefix='/api')
# REGISTER CONSOLIDATE
app.register_blueprint(appSpyConsolidate , url_prefix='/api')
app.register_blueprint(appArkConsolidate , url_prefix='/api')
app.register_blueprint(appQqqConsolidate , url_prefix='/api')


from apps.route import *