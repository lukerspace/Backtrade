from apps import db

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


class Eps_Ark(db.Model):
    __tablename__="ark_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(200))
    time_first=db.Column(db.DateTime)
    time_second=db.Column(db.DateTime)
    time_third=db.Column(db.DateTime)
    est_first=db.Column(db.String(200))
    est_second=db.Column(db.String(200))
    est_third=db.Column(db.String(200))
    act_first=db.Column(db.String(200))
    act_second=db.Column(db.String(200))
    act_third=db.Column(db.String(200))

    def __init__(self,ticker,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
        self.est_first=est_first
        self.est_second=est_second
        self.est_third=est_third
        self.act_first=act_first
        self.act_second=act_second
        self.act_third=act_third


class Eps_Spy(db.Model):
    __tablename__="spy_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(200))
    time_first=db.Column(db.DateTime)
    time_second=db.Column(db.DateTime)
    time_third=db.Column(db.DateTime)
    est_first=db.Column(db.String(200))
    est_second=db.Column(db.String(200))
    est_third=db.Column(db.String(200))
    act_first=db.Column(db.String(200))
    act_second=db.Column(db.String(200))
    act_third=db.Column(db.String(200))

    def __init__(self,ticker,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
        self.est_first=est_first
        self.est_second=est_second
        self.est_third=est_third
        self.act_first=act_first
        self.act_second=act_second
        self.act_third=act_third


class Eps_Qqq(db.Model):
    __tablename__="qqq_eps"
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    ticker=db.Column(db.String(200))
    time_first=db.Column(db.DateTime)
    time_second=db.Column(db.DateTime)
    time_third=db.Column(db.DateTime)
    est_first=db.Column(db.String(200))
    est_second=db.Column(db.String(200))
    est_third=db.Column(db.String(200))
    act_first=db.Column(db.String(200))
    act_second=db.Column(db.String(200))
    act_third=db.Column(db.String(200))

    def __init__(self,ticker,time_first,time_second,time_third,est_first,est_second,est_third,act_first,act_second,act_third):
        self.ticker=ticker
        self.time_first=time_first
        self.time_second=time_second
        self.time_third=time_third
        self.est_first=est_first
        self.est_second=est_second
        self.est_third=est_third
        self.act_first=act_first
        self.act_second=act_second
        self.act_third=act_third


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


