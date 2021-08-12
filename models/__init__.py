from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask('__main__')



app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:0000@localhost/company'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False



db=SQLAlchemy(app)
Migrate(app,db)



