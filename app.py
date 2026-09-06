import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="ChefBot - Resep dari Bahan Dapur",
    page_icon="🍳",
    layout="centered"
)

st.title("🍳 ChefBot: Kreasikan Resep Dapurmu")
st.caption("Masukkan bahan-bahan yang kamu punya, ChefBot akan meracik resepnya!")


api_key = os.environ.get("GEMINI_API_KEY") or st.sidebar.text_input("Masukkan Gemini API Key:", type="password")

if not api_key:
    st.info("Silakan masukkan Gemini API Key di sidebar untuk mulai memasak.")
    st.stop()

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """
Anda adalah ChefBot, seorang koki kreatif dan ramah.
Tugas utama Anda adalah memberikan rekomendasi resep masakan berdasarkan bahan-bahan yang diberikan oleh pengguna.

Aturan Jawaban:
1. Prioritaskan resep yang menggunakan bahan-bahan yang disebutkan pengguna.
2. Anda boleh menyarankan beberapa bahan tambahan umum (seperti garam, minyak, gula, atau bumbu dapur standar).
3. Strukturkan setiap resep dengan format berikut:
   - 🍲 **Nama Masakan**
   - 📝 **Bahan Utama & Bumbu** (bedakan bahan yang disediakan user dan bahan tambahan)
   - 🔪 **Langkah-Langkah Memasak** (runtut dan jelas)
   - 💡 **Tips Tambahan** (opsional, misal pengganti bahan atau tingkat kepedasan)
4. Jika bahan yang diberikan kurang masuk akal atau terlalu sedikit untuk membuat masakan utuh, berikan opsi resep paling mendekati dan tanyakan apakah pengguna punya bahan tambahan lain.
5. Gunakan bahasa Indonesia yang santai, komunikatif, dan menggugah selera.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Contoh: Telur, tahu, kecap, cabai rawit..."):
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=msg["content"])]
            )
        )

    with st.chat_message("assistant"):
        with st.spinner("ChefBot sedang meracik resep..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.7,
                    )
                )
                bot_response = response.text
                st.markdown(bot_response)
               
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungkan ke API: {e}")