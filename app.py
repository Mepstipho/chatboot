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
/* Background halaman */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #e4ebf5);
}

/* Container chat */
.chat-container {
    max-width: 700px;
    margin: auto;
}

/* Bubble User */
.chat-bubble-user {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    color: white;
    padding: 12px 16px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0 8px auto;
    width: fit-content;
    max-width: 80%;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    font-size: 15px;
}

/* Bubble Bot */
.chat-bubble-bot {
    background: #ffffff;
    color: #333;
    padding: 12px 16px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px auto 8px 0;
    width: fit-content;
    max-width: 80%;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    font-size: 15px;
}

/* Judul */
h1 {
    text-align: center;
    color: #1f2937;
}

/* Caption */
.stCaption {
    text-align: center;
    color: #6b7280;
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
