# 🚀 Cross-Platform Reminder App - Backend API

Python, FastAPI ve MS SQL Server kullanılarak sıfırdan geliştirilmiş, ilişkisel veritabanı mimarisine sahip robust (dayanıklı) bir Full-Stack Backend API projesidir.

## 🛠️ Kullanılan Teknolojiler ve Araçlar

* **Dil:** Python 3.13
* **Framework:** FastAPI
* **Veritabanı:** MS SQL Server
* **ORM & Sürücü:** SQLAlchemy, PyODBC
* **Veri Doğrulama:** Pydantic
* **Sunucu:** Uvicorn (ASGI)

## 📂 Proje Mimarisi

Proje, sürdürülebilir ve modüler bir mimariyle tasarlanmıştır:
- `main.py`: FastAPI endpoint'lerinin (API uç noktalarının) ve yönlendirmelerin yönetildiği ana dosya.
- `database.py`: MS SQL Server bağlantı ayarlarının ve oturum yönetiminin yapıldığı modül.
- `models.py`: SQLAlchemy kullanarak ilişkisel veritabanı tablolarının (`users`, `event`, `reminder`) Python sınıfları olarak modellenmesi.
- `schemas.py`: Dışarıdan gelen verileri doğrulayan Pydantic güvenlik ve veri transfer şemaları.

## 🚀 Projenin Özellikleri ve API Uç Noktaları (Endpoints)

Şu ana kadar tamamlanan ve aktif olarak çalışan CRUD operasyonları:

### 1. Kullanıcı Yönetimi (`/users/`)
* **POST `/users/`**: Yeni kullanıcı kaydı oluşturur (E-posta doğrulama ve şifreleme altyapısıyla).
* **GET `/users/`**: Veritabanındaki tüm kullanıcıları listeler.
* **DELETE `/users/{user_id}`**: Belirtilen ID'ye sahip kullanıcıyı sistemden siler.

### 2. Etkinlik Yönetimi (`/events/`)
* **POST `/events/`**: Belirli bir kullanıcıya (`user_ID` üzerinden Foreign Key bağlantısıyla) ait yeni etkinlik oluşturur.
* **GET `/events/`**: Sistemdeki tüm etkinlikleri listeler.
* **DELETE `/events/{event_id}`**: Belirtilen etkinlik kaydını siler.

### 3. Hatırlatıcı Yönetimi (`/reminders/`)
* **POST `/reminders/`**: Belirli bir etkinliğe (`event_id` üzerinden Foreign Key bağlantısıyla) ait alarm/hatırlatıcı kurar.
* **GET `/reminders/`**: Tüm hatırlatıcıları listeler.
* **DELETE `/reminders/{reminder_id}`**: İlgili hatırlatıcıyı siler.

## ⚙️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için şu adımları izleyin:

1. **Repoyu klonlayın:**
   ```bash
   git clone [https://github.com/kullaniciadin/reminderapp.git](https://github.com/kullaniciadin/reminderapp.git)
   cd reminderapp