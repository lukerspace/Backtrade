from __main__ import db


class Company_Ark(db.Model):
    __tablename__="ark_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company

class Company_Spy(db.Model):
    __tablename__="spy_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company

class Company_Qqq(db.Model):
    __tablename__="qqq_company"
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(255))
    describe=db.Column(db.String(255))
    industry=db.Column(db.String(255))
    ceo=db.Column(db.String(255))
    def __init__(self,company,describe,industry,ceo):
        self.company=company
        self.describe=describe
        self.industry=industry
        self.ceo=ceo
    def __repr__(self):
        return "<Company %r>" %self.company
