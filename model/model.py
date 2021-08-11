from model import db

class Company(db.Model):
    __tablename__="company"

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
        