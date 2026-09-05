from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users" # SQL'deki tablonun adını birebir yazıyoruz, böylece eşleşiyorlar.

    user_ID = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(300), nullable=False)

    events = relationship("Event", back_populates="owner")

class Event(Base):
    __tablename__= "event"

    event_id = Column(Integer, primary_key=True, index=True)
    user_ID = Column(Integer,ForeignKey("users.user_ID"))
    created_date= Column(DateTime,nullable=False)
    title = Column(String(50),nullable=False)
    description = Column(String(50),nullable=False)
    event_date = Column(DateTime,nullable=False)

    owner = relationship("User", back_populates="events")
    reminders = relationship("Reminder", back_populates="event_reference")

class Reminder(Base):
     __tablename__="reminder"

     reminder_id = Column(Integer,primary_key=True ,index=True)
     event_id  = Column(Integer, ForeignKey("event.event_id"))
     reminder_time =Column(DateTime,nullable=False)
     reminder_message=Column(String(100),nullable=False)
     
     event_reference = relationship("Event", back_populates="reminders")
     

    


