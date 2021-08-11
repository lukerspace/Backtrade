from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask('__main__')



app.config['SQLALCHEMY_DATABASE_URI']=f'mysql://root:0000@localhost/{DBNAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)
Migrate(app,db)
