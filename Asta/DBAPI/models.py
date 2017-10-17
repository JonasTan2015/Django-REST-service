from django.db import models

# Create your models here.
# This is Djanro ORM model
class CreditCard(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    deposit = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {"ID": self.ID, "name": self.name, "deposit": self.deposit, "date": self.date}


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DATE, VARCHAR, DateTime
from sqlalchemy.sql import func
import uuid
from DBAPI import engine

Base = declarative_base()
# This is Sqlalchemy ORM model
class AlchemyCreditCard(Base):
    __tablename__ = 'AlchemyCreditCard'
    ID = Column(VARCHAR(length=80), primary_key=True, default=uuid.uuid4())
    name = Column(VARCHAR(length=30))
    deposit = Column(Integer, default=0)
    date = Column(DateTime(timezone=True), default=func.now())


Base.metadata.create_all(engine)