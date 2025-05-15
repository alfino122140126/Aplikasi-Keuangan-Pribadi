# ============================================================
# README – Aplikasi Keuangan Pribadi
# ============================================================

# Judul Aplikasi
# Aplikasi Keuangan Pribadi

# Deskripsi
# Aplikasi ini digunakan untuk mencatat pemasukan, pengeluaran, utang, dan pengingat pengeluaran rutin.
# Backend menggunakan Python Pyramid + PostgreSQL
# Frontend menggunakan React.js + Tailwind CSS + Redux Toolkit

# ------------------------------------------------------------
# Struktur Proyek
# ------------------------------------------------------------

# Aplikasi-Keuangan-Pribadi/
# ├── backend/         # Backend API Pyramid
# │   ├── models/
# │   ├── views/
# │   ├── routes/
# │   └── development.ini
# ├── frontend/        # ReactJS + Tailwind CSS + Redux
# │   ├── src/
# │   │   ├── components/
# │   │   ├── pages/
# │   │   ├── store/
# │   │   └── services/
# │   └── tailwind.config.js
# ├── docs/            # Dokumentasi
# └── README.md

# ------------------------------------------------------------
# Fitur Utama
# ------------------------------------------------------------

# 🔐 Autentikasi pengguna (login/registrasi)
# ➕ CRUD transaksi keuangan
# 🏷️ Manajemen kategori transaksi
# 🤝 Pencatatan utang (utang kita ke orang, dan orang ke kita)
# ⏰ Pengingat pengeluaran rutin (WiFi bulanan, kontrakan tahunan)
# 📊 Dashboard saldo & grafik keuangan
# 🔄 Integrasi API React ↔ Pyramid
# 📱 Responsif (mobile & desktop)

# ------------------------------------------------------------
# Dependensi
# ------------------------------------------------------------

# Backend:
# - Python 3.13.x
# - Pyramid 2.x
# - SQLAlchemy
# - PostgreSQL 17
# - Alembic
# - Passlib
# - JWT (opsional)

# Frontend:
# - React 18+
# - React Router DOM
# - Redux Toolkit
# - Axios
# - Tailwind CSS
# - Vite (recommended)

# ------------------------------------------------------------
# Cara Menjalankan Backend (Pyramid)
# ------------------------------------------------------------

cd backend/
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
initialize_app_db development.ini
pserve development.ini

# ------------------------------------------------------------
# Cara Menjalankan Frontend (React + Tailwind)
# ------------------------------------------------------------

cd frontend/
npm install
npm run dev

# ------------------------------------------------------------
# Deployment (Opsional)
# ------------------------------------------------------------

# Frontend:
# - Vercel (auto-deploy React)

# Backend:
# - Railway / Render / Heroku
# - Pastikan PostgreSQL aktif dan URL-nya disimpan di .env


# MIT License
# Koling Dev – Tugas Besar Pemrograman Web 2024/2025
