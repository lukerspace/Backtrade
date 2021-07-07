import os
import sys
from flask import *

pre_path = os.path.abspath("../backtraded")
sys.path.append(pre_path)
app=Flask(__name__)
# import quote

from api.qqq_sign import appQqqSign
# from api.qqq_hist import appQqqHist

from api.ark_sign import appArkSign
from api.ark_hist import appArkHist

from api.spy_sign import appSpySign
# from api.spy_hist import appSpyHist

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["JSON_SORT_KEYS"] = False
app.secret_key="backtrader"

app.register_blueprint(appQqqSign, url_prefix='/api')
# app.register_blueprint(appQqqHist, url_prefix='/api')

app.register_blueprint(appArkSign, url_prefix='/api')
app.register_blueprint(appArkHist, url_prefix='/api')

app.register_blueprint(appSpySign, url_prefix='/api')
# app.register_blueprint(appSpyHist, url_prefix='/api')

@app.route("/")
def menu():
	return render_template("menu.html")

@app.route("/qqq")
def index():
	return render_template("qqq.html")

@app.route("/ark")
def ark():
	return render_template("ark.html")

@app.route("/spy")
def spy():
	return render_template("spy.html")

# app.run(port=3000)

app.run(host='0.0.0.0', port=3000)		



