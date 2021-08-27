from apps import db

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
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
            "industry":"{}".format(self.industry),"website":"{}".format(self.website)})
    # def as_dict(self):
    #     return{c.name: getattr(self, c.name) for c in self.__table__.columns}

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
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
            "industry":"{}".format(self.industry),"website":"{}".format(self.website)})

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
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"company":"{}".format(self.company),"describe":"{}".format(self.describe),\
            "industry":"{}".format(self.industry),"website":"{}".format(self.website)})

# EPS

class Eps_Ark(db.Model):
    __tablename__="ark_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

class Eps_Spy(db.Model):
    __tablename__="spy_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

class Eps_Qqq(db.Model):
    __tablename__="qqq_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))
  
    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

# REV

class Rev_Ark(db.Model):
    __tablename__="ark_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})
        
class Rev_Spy(db.Model):
    __tablename__="spy_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third 
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    
    db.Model.to_dict=to_dict
    
class Rev_Qqq(db.Model):
    __tablename__="qqq_rev"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

# DIV

class Div_Ark(db.Model):
    __tablename__="ark_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

class Div_Spy(db.Model):
    __tablename__="spy_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})

class Div_Qqq(db.Model):
    __tablename__="qqq_div"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(2000))
    time_first=db.Column(db.String(2000))
    time_second=db.Column(db.String(2000))
    time_third=db.Column(db.String(2000))

    def __init__(self,ticker,time_first,time_second,time_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
    def __repr__(self):
        return  str({"ticker":"{}".format(self.ticker),"first":"{}".format(self.time_first),"second":"{}".format(self.time_second),"third":"{}".format(self.time_third)})