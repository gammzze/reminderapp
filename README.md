Markdown
# 🔔 Cross-Platform Reminder App

<div align="center">

  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100%2B-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/PWA-Enabled-purple?style=for-the-badge&logo=pwa&logoColor=white" alt="PWA">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">

  <p>A professional-grade, modern full-stack web and desktop reminder application engineered with a robust FastAPI backend and a responsive Tailwind CSS frontend, featuring native desktop notifications and Progressive Web App (PWA) capabilities.</p>

</div>

---

## 🌟 Key Features

* **🔒 Secure Authentication:** Token-based security utilizing OAuth2 standards with dedicated user registration (`/register`) and login (`/login`) workflows.
* **⏰ Smart Time-Specific Scheduling:** Integrated local-time synchronization supporting precise minute-level task scheduling via modern HTML5 datetime pickers.
* **🔔 Native Desktop Notifications:** Automated background polling system leveraging the browser's `Notification API` to trigger real-time Windows native desktop alerts when tasks come due.
* **📱 PWA (Progressive Web App) Support:** Fully configured web app manifest (`manifest.json`) enabling seamless installation as an independent desktop application shortcut.
* **⚡ Automated Execution Script:** Custom Windows batch automation (`baslat.bat`) that initializes the virtual environment, boots the Uvicorn server, and launches the interface instantly.

---

## 🛠️ Tech Stack

### Backend
* **Python** & **FastAPI** (High-performance asynchronous web framework)
* **Uvicorn** (ASGI server with live-reload capabilities)
* **Pydantic** & **OAuth2 / Passlib** (Data validation and secure password hashing)

### Frontend & Client
* **HTML5** & **Tailwind CSS** (Modern, utility-first responsive UI design)
* **JavaScript (ES6+)** (Asynchronous Fetch API & browser Notification management)

### Deployment & Tooling
* **Git & GitHub** (Version control and collaboration)
* **PWA Manifest API** (Desktop cross-platform installability)
* **Windows Batch Scripting** (Environment orchestration)

---

## 📂 Project Architecture

```text
reminderapp/
│
├── main.py              # FastAPI application entry point & API endpoints
├── database.py          # Database configuration and session management
├── models.py            # SQLAlchemy database models (Users & Events)
├── hashing.py           # Password hashing utilities (Bcrypt)
├── index.html           # Frontend user interface (Tailwind & Client JS)
├── manifest.json        # PWA configuration for desktop installation
├── baslat.bat           # One-click automated launch script
└── venv/                # Python virtual environment
🚀 Quick Start & Installation
Prerequisites
Python 3.10 or higher installed on your machine.

Microsoft Edge or Google Chrome (for PWA and notification support).

Setup & Running the Application
Clone the repository:

Bash
git clone [https://github.com/your-username/reminderapp.git](https://github.com/your-username/reminderapp.git)
cd reminderapp
Launch via Automation Script:
Simply double-click the baslat.bat file in the root directory. This script will automatically verify dependencies, start the FastAPI backend server on port 8000, and open your application interface.

Manual Execution (Alternative):
If you prefer using the terminal:

Bash
# Activate virtual environment
source venv/Scripts/activate  # For Git Bash / Windows

# Run the FastAPI server
uvicorn main:app --reload
💡 Usage Guide
Register/Login: Open the application, switch to the Sign Up tab to create a new user profile, and log in securely.

Add a Reminder: Fill out the title, description, and target reminder date/time using the scheduling form.

Enable Notifications: Allow browser notification permissions when prompted to ensure desktop alerts function smoothly.

Install as App: Click the install icon in your browser's address bar to run the app as a dedicated desktop window.

📜 License
This project is open-source and available under the MIT License.
