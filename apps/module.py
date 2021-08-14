from apps import db

class Company_Ark(db.Model):
    __tablename__="ark_company"
    __table_args__ = {'extend_existing': True}
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
    __table_args__ = {'extend_existing': True}
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
    __table_args__ = {'extend_existing': True}
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