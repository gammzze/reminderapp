from pydantic import BaseModel, EmailStr
from datetime import datetime

# Kullanıcı dışarıdan (telefondan) kayıt olurken bize hangi verileri göndermek ZORUNDA?
class UserCreate(BaseModel):
    name: str
    lastName: str
    email: EmailStr # Bu sihirli kelime, içinde '@' ve '.com' olmayan her şeyi anında reddeder!
    password: str



class EventCreate(BaseModel):
    user_ID: int
    created_date: datetime
    title:str
    description:str
    event_date: datetime

class ReminderCreate(BaseModel):
    event_id: int
    reminder_time:datetime
    reminder_message:str
    