import streamlit as st
import google.generativeai as genai

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="AI Chatbot Gemini",
    page_icon="🤖",
    layout="centered"
)

# =========================
# CSS SEDERHANA (Modern UI)
# =========================
st.markdown("""
<style>
.chat-bubble-user {
    background-color: #DCF8C6;
    padding: 10px 14px;
    border-radius: 10px;
    margin-bottom: 8px;
    text-align: right;
}
.chat-bubble-bot {
    background-color: #F1F0F0;
    padding: 10px 14px;
    border-radius: 10px;
    margin-bottom: 8px;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# =========================
# JUDUL
# =========================
st.title("🤖 Gemini AI Chatbot")
st.caption("Powered by Google Gemini • Streamlit")

# =========================
# INPUT API KEY
# =========================
api_key = st.text_input(
    "🔑 Masukkan Gemini API Key",
    type="password"
)

if api_key:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-3-flash-preview')

    # =========================
    # SESSION STATE
    # =========================
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # =========================
    # TAMPILKAN CHAT
    # =========================
    for role, message in st.session_state.chat_history:
        if role == "user":
            st.markdown(
                f'<div class="chat-bubble-user">{message}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-bubble-bot">{message}</div>',
                unsafe_allow_html=True
            )

    # =========================
    # INPUT USER
    # =========================
    prompt = st.chat_input("Ketik pesan...")

    if prompt:
        # Simpan pesan user
        st.session_state.chat_history.append(("user", prompt))

        try:
            response = model.generate_content(prompt)
            bot_reply = response.text
        except Exception as e:
            bot_reply = f"Terjadi error: {e}"

        # Simpan balasan bot
        st.session_state.chat_history.append(("bot", bot_reply))

        st.rerun()

else:
    st.info("Masukkan **Gemini API Key** untuk mulai chatting.")
