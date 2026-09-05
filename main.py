from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime


import models
import schemas
from database import engine, SessionLocal

# Python'a "Git veritabanına bak, tabloları kontrol et, eksik varsa oluştur" diyoruz.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# SEKRETER: Her işlemde veritabanına bir kapı (session) açar, işlem bitince kapıyı güvenle kapatır.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GERÇEK İŞLEM: Yeni Kullanıcı Kaydetme (POST)
# @app.post demek: Dışarıdan bana veri gelecek (telefondan form doldurulacak) demek.
@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # 1. ÇEVİRİ: Telefondan gelen şemayı (UserCreate), veritabanı modeline (User) dönüştür.
    yeni_kullanici = models.User(
        name=user.name,
        lastName=user.lastName,
        email=user.email,
        password=user.password
    )
    
    # 2. EKLE: Yeni kullanıcıyı veritabanı kuyruğuna al.
    db.add(yeni_kullanici)
    
    # 3. KAYDET: İşlemi onaylayıp kalıcı olarak veritabanına yaz. (Hatırlarsan autocommit=False yapmıştık)
    db.commit()
    
    # 4. YENİLE: MS SQL'in otomatik verdiği ID numarasını (user_ID) görmek için veriyi yenile.
    db.refresh(yeni_kullanici)
    
    # 5. CEVAP VER: Mobil uygulamaya başaranın haberini gönder.
    return {"mesaj": "Kullanici basariyla olusturuldu!", "kullanici_bilgileri": yeni_kullanici}


@app.post("/events/")
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    
   
    yeni_etkinlik = models.Event(
        user_ID=event.user_ID,
        title=event.title,
        description=event.description,
        event_date=event.event_date,
        created_date=datetime.now()  
    )
    
    db.add(yeni_etkinlik)
    db.commit()
    db.refresh(yeni_etkinlik)
    
    return {"mesaj": "Etkinlik basariyla eklendi!", "etkinlik_bilgileri": yeni_etkinlik}



@app.post("/reminders/")
def create_reminder(reminder: schemas.ReminderCreate, db: Session = Depends(get_db)):

    yeni_hatirlatici=models.Reminder(
        event_id=reminder.event_id,
        reminder_time=reminder.reminder_time,
        reminder_message=reminder.reminder_message
    )

    db.add(yeni_hatirlatici)
    db.commit()
    db.refresh(yeni_hatirlatici)

    return {"mesaj": "Hatirlatici basariyla kuruldu!", "hatirlatici_bilgileri": yeni_hatirlatici}



# VERİ OKUMA İŞLEMİ: Tüm Kullanıcıları Listele (GET)
# @app.get demek: "Bana form gönderme, sadece adrese gel ve benden listeyi al" demek.
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    
    # 1. DOSYA DOLABINI AÇ VE LİSTEYİ AL:
    # Veritabanındaki User tablosuna git ve içindeki her şeyi (.all()) getir.
    tum_kullanicilar = db.query(models.User).all()
    
    # 2. LİSTEYİ TELEFONA/TARAYICIYA GÖNDER:
    return tum_kullanicilar


@app.get("/event/")
def get_events(db: Session = Depends(get_db)):

    tum_etkinlikler =db.query(models.Event).all()
    return tum_etkinlikler


@app.get("/reminder/")
def get_reminders(db: Session = Depends(get_db)):

    tum_hatirlaticilar=db.query(models.Reminder).all()
    return tum_hatirlaticilar



# SİLME İŞLEMİ: Belirli bir ID'ye sahip kullanıcıyı sil (DELETE)
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    
    # 1. ÖNCE KULLANICIYI BUL:
    silinecek_kullanici = db.query(models.User).filter(models.User.user_ID == user_id).first()
    
    # 2. EĞER KULLANICI YOKSA HATA VER:
    if silinecek_kullanici is None:
        return {"hata": "Bu ID'ye sahip kullanıcı bulunamadı!"}
    
    # 3. VERİTABANINDAN SİL VE ONAYLA:
    db.delete(silinecek_kullanici)
    db.commit()
    
    return {"mesaj": f"ID'si {user_id} olan kullanıcı başarıyla silindi!"}


@app.delete("/event/{event_id}")
def delete_event(event_id: int, db:Session=Depends(get_db)):

    silinicek_etkinlik=db.query(models.Event).filter(models.Event.event_id==event_id).first()

    if silinicek_etkinlik is None:
        return{"hata": "bu ıdye ait etkinlik bulunamadı!"}

    db.delete(silinicek_etkinlik)
    db.commit()

    return{"mesaj": f"ıd'si{event_id} olan etkinlik başarıyla silindi"}


@app.delete("/reminder/{reminder_id}")
def delete_reminder(reminder_id: int ,db: Session=Depends(get_db)):

    silinecek_hatirlatici=db.query(models.Reminder).filter(models.Reminder.reminder_id==reminder_id).first()

    if silinecek_hatirlatici is None:
         return{"mesaj": "bu id ile olan hatirlatici bulunamadı!"}

    db.delete(silinecek_hatirlatici)
    db.commit()

    return{"mesaj": f"ıd'si {reminder_id} olan hatirlatici basariyla silindi!"}






  

