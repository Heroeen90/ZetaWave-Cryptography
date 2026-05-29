import streamlit as st
import base64
import numpy as np
import plotly.graph_objects as go

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import hashlib

# ==============================
# إعداد الصفحة
# ==============================
st.set_page_config(
    page_title="ZetaWave Crypto Vault Pro",
    page_icon="💻",
    layout="centered"
)

# ==============================
# 🔐 تحويل الـ Seed إلى مفتاح قوي AES
# ==============================
def derive_key(seed: str, salt: bytes) -> bytes:
    seed = str(seed).encode()
    return PBKDF2(seed, salt, dkLen=32, count=200000)

# ==============================
# 🔐 AES-GCM Encryption
# ==============================
def encrypt(data: bytes, seed: str):
    salt = get_random_bytes(16)
    key = derive_key(seed, salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return base64.b64encode(salt + cipher.nonce + tag + ciphertext)

# ==============================
# 🔓 AES-GCM Decryption
# ==============================
def decrypt(token: str, seed: str):
    raw = base64.b64decode(token)

    salt = raw[:16]
    nonce = raw[16:32]
    tag = raw[32:48]
    ciphertext = raw[48:]

    key = derive_key(seed, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(ciphertext, tag)

# ==============================
# UI Style (بدون تغيير)
# ==============================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
    color: #f3f4f6;
    font-family: 'Inter', 'Cairo', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center">
<h2>💻 CRYPTO VAULT PRO</h2>
<p>نظام تشفير آمن AES-256-GCM</p>
</div>
""", unsafe_allow_html=True)

# ==============================
# Session State
# ==============================
if "global_seed_factor" not in st.session_state:
    st.session_state["global_seed_factor"] = "767777664646466464646"

if "quantum_infinity_active" not in st.session_state:
    st.session_state["quantum_infinity_active"] = False

current_mode_label = "INFINITY MODE 🌌" if st.session_state["quantum_infinity_active"] else "STANDARD MODE 🔒"

st.markdown(f"""
<div style="text-align:center; padding:10px;">
<b>MODE:</b> {current_mode_label}
</div>
""", unsafe_allow_html=True)

# ==============================
# MENU
# ==============================
options = ["المحلل الذكي 🎛️", "السجل الحي 📜", "النطاق الكمي والمعاملات 📑", "مفكك الشفرات العام 🔓"]
selected_option = st.radio("اختر الأداة:", options)

st.write("---")

# ==============================
# 1 - ENCRYPT / DECRYPT
# ==============================
if selected_option == "المحلل الذكي 🎛️":

    st.subheader("🔐 التشفير / فك التشفير")

    mode = st.radio("نوع العملية:", ["تشفير", "فك تشفير"])

    seed = st.text_input("🔑 المفتاح (Seed)", st.session_state["global_seed_factor"])

    if mode == "تشفير":
        text = st.text_area("أدخل النص")

        if st.button("تشفير"):
            if text:
                enc = encrypt(text.encode(), seed)
                st.code(enc.decode())
            else:
                st.warning("أدخل نص")

    if mode == "فك تشفير":
        text = st.text_area("أدخل النص المشفر")

        if st.button("فك التشفير"):
            try:
                dec = decrypt(text, seed)
                st.success(dec.decode())
            except Exception:
                st.error("فشل فك التشفير (مفتاح خاطئ أو بيانات تالفة)")

# ==============================
# 2 - LOG
# ==============================
elif selected_option == "السجل الحي 📜":
    st.code(f"""
[SECURE] AES-GCM ACTIVE
[MODE] {current_mode_label}
[SEED] {st.session_state['global_seed_factor']}
""")

# ==============================
# 3 - QUANTUM MODE VISUAL (محسن فقط)
# ==============================
elif selected_option == "النطاق الكمي والمعاملات 📑":

    st.subheader("📊 تمثيل بصري للنظام")

    x = np.linspace(-5, 5, 60)
    y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(x, y)

    seed_num = sum([int(d) for d in str(st.session_state["global_seed_factor"]) if d.isdigit()] or [1])

    Z = np.sin(X * seed_num * 0.01) * np.cos(Y)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# 4 - DECODER
# ==============================
elif selected_option == "مفكك الشفرات العام 🔓":

    st.subheader("🔍 محلل البيانات")

    text = st.text_area("أدخل النص")

    if st.button("تحليل"):
        try:
            decoded = base64.b64decode(text).decode(errors="ignore")
            st.write(decoded)
        except:
            st.warning("ليس Base64 صالح")
