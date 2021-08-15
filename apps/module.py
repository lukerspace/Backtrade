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
        return "<Company %r>" %self.company

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
        return "<Company %r>" %self.company

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
        return "<Company %r>" %self.company