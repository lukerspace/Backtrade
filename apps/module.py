from apps import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# COMPANY
class Company_Ark(db.Model):
    __tablename__="ark_company"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(3000))
    company=db.Column(db.String(3000))
    describe=db.Column(db.String(3000))
    industry=db.Column(db.String(3000))
    website=db.Column(db.String(3000))
    def __init__(self,ticker,company,describe,industry,website):
        self.ticker=ticker
        self.company=company
        self.describe=describe
        self.industry=industry
        self.website=website
    # def __repr__(self):
    #     return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
    #         "industry":"{}".format(self.industry),"website":"{}".format(self.website)})
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Company_Spy(db.Model):
    __tablename__="spy_company"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(3000))
    company=db.Column(db.String(3000))
    describe=db.Column(db.String(3000))
    industry=db.Column(db.String(3000))
    website=db.Column(db.String(3000))
    def __init__(self,ticker,company,describe,industry,website):
        self.ticker=ticker
        self.company=company
        self.describe=describe
        self.industry=industry
        self.website=website
    # def __repr__(self):
    #     return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
    #         "industry":"{}".format(self.industry),"website":"{}".format(self.website)})
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
class Company_Qqq(db.Model):
    __tablename__="qqq_company"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(3000))
    company=db.Column(db.String(3000))
    describe=db.Column(db.String(3000))
    industry=db.Column(db.String(3000))
    website=db.Column(db.String(3000))
    def __init__(self,ticker,company,describe,industry,website):
        self.ticker=ticker
        self.company=company
        self.describe=describe
        self.industry=industry
        self.website=website
    # def __repr__(self):
    #     return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
    #         "industry":"{}".format(self.industry),"website":"{}".format(self.website)})
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
# # EPS

class Eps_Ark(db.Model):
    __tablename__="ark_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Eps_Spy(db.Model):
    __tablename__="spy_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Eps_Qqq(db.Model):
    __tablename__="qqq_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

# # REV

class Rev_Ark(db.Model):
    __tablename__="ark_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Rev_Spy(db.Model):
    __tablename__="spy_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Rev_Qqq(db.Model):
    __tablename__="qqq_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}


# # DIV

class Div_Ark(db.Model):
    __tablename__="ark_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Div_Spy(db.Model):
    __tablename__="spy_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

class Div_Qqq(db.Model):
    __tablename__="qqq_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.JSON)
    time_second=db.Column(db.JSON)
    time_third=db.Column(db.JSON)

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}