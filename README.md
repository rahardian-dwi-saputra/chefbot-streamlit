# 🍳 ChefBot: AI Recipe Generator from Available Ingredients

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Conda](https://img.shields.io/badge/Conda-Supported-green.svg)](https://docs.conda.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.63%2B-FF4B4B.svg)](https://streamlit.io/)
[![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-3.6--Flash-4285F4.svg)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**ChefBot** adalah aplikasi chatbot interaktif berbasis AI yang membantu Anda mengkreasi resep masakan lezat berdasarkan bahan-bahan yang tersedia di dapur Anda. Ditenagai oleh **Google Gemini 3.6 Flash API** dan dibangun menggunakan **Streamlit**, ChefBot dapat mengubah daftar bahan acak menjadi panduan memasak langkah-demi-langkah yang terstruktur dan menggugah selera.

---

## 📸 Fitur Utama

- 🥑 **Rekomendasi Berbasis Bahan:** Masukkan bahan apa saja yang Anda punya, dan ChefBot akan meracik resep terbaik.
- 📝 **Panduan Langkah Terstruktur:** Setiap resep dilengkapi dengan nama masakan, pemisahan bahan utama vs bumbu tambahan, langkah memasak runtut, serta tips koki.
- 💬 **Percakapan Interaktif:** Mendukung pertanyaan lanjutan (misal: *"Ubah resep ini jadi versi tidak pedas"* atau *"Berapa estimasi waktu masaknya?"*).
- 🔑 **Pengaturan API Key Fleksibel:** Bisa diinput langsung melalui antarmuka (sidebar) atau diset via *environment variable*.
- ⚡ **Ringan & Cepat:** Antarmuka responsif dan ramah pengguna bertenaga Streamlit.

---

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** [Python 3.9+](https://www.python.org/)
- **Environment Manager:** [Conda](https://docs.conda.io/)
- **Frontend / Framework:** [Streamlit](https://streamlit.io/)
- **AI / LLM Engine:** [Google GenAI SDK](https://github.com/googleapis/python-genai) (`google-genai`)
- **Model LLM:** `gemini-3.6-flash`

---

## 🚀 Petunjuk Instalasi & Penggunaan

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek secara lokal di komputer Anda:

### 1. Kloning Repositori

```bash
git clone https://github.com/rahardian-dwi-saputra/chefbot-streamlit.git
cd chefbot-streamlit
```

### 2. Buat Virtual Environment dengan Conda
```bash
conda create --name <env> --file requirements.txt
```

### 3. Dapatkan Gemini API Key
1. Buka [Google AI Studio](https://aistudio.google.com/).
2. Buat dan salin API Key Anda.

### 4. Jalankan Aplikasi
Langsung jalankan Streamlit dan masukkan API Key di sidebar aplikasi:
```bash
streamlit run app.py
```
Aplikasi akan otomatis berjalan dan terbuka di browser pada alamat `http://localhost:8501`.

---

## 📂 Struktur Repositori
```
chefbot-streamlit/
├── app.py              # Kode utama aplikasi Streamlit & integrasi Gemini API
├── requirements.txt    # Daftar dependensi pip
├── README.md           # Dokumentasi proyek
└── .gitignore          # File dan folder yang diabaikan oleh Git
```

---

## 💡 Contoh Penggunaan
1. Ketik bahan yang Anda punya di kolom chat, contoh:
    > Tahu, telur, kecap manis, bawang putih, cabai rawit
2. ChefBot akan meracik resep seperti Tahu Telur Bumbu Kecap Pedas Gurih beserta estimasi bahan dan langkah memasaknya.
3. Ajukan pertanyaan lanjutan jika diperlukan:
    > Ada saran bahan pendamping lain yang cocok?