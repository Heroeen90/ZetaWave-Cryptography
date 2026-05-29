import streamlit as st
import base64
import numpy as np
import plotly.graph_objects as go

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# =========================
# إعداد الصفحة (بدون تغيير)
# =========================
st.set_page_config(
    page_title="ZetaWave Crypto Vault Pro",
    page_icon="💻",
    layout="centered"
)

# =========================
# 🔐 طبقة التشفير الآمن (بديل النواة فقط)
# =========================

def _derive_key(seed: str, salt: bytes) -> bytes:
    """تحويل الـ Seed إلى مفتاح AES-256 باستخدام KDF آمن"""
    seed_bytes = str(seed).encode()
    return PBKDF2(seed_bytes, salt, dkLen=32, count=200000)


def _encrypt(data: bytes, seed: str) -> str:
    salt = get_random_bytes(16)
    key = _derive_key(seed, salt)

    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    package = salt + cipher.nonce + tag + ciphertext
    return base64.b64encode(package).decode()


def _decrypt(token: str, seed: str) -> bytes:
    raw = base64.b64decode(token)

    salt = raw[:16]
    nonce = raw[16:32]
    tag = raw[32:48]
    ciphertext = raw[48:]

    key = _derive_key(seed, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(ciphertext, tag)


# =========================
# 🎨 الواجهة الأصلية (بدون أي تغيير)
# =========================
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
<div class="vault-header">
    <div class="vault-title">💻 CRYPTO VAULT PRO</div>
    <p style='color: #9ca3af; font-size: 14px;'>نظام الحماية الفوق-أمنية النواة القائمة على طيف أصفار ريمان والاتصال التزامني الديناميكي.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# Session State (بدون تغيير)
# =========================
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

if 'global_seed_factor' not in st.session_state:
    st.session_state['global_seed_factor'] = "01"

if 'quantum_infinity_active' not in st.session_state:
    st.session_state['quantum_infinity_active'] = False

current_mode_label = "وضع اللانهاية الكلي 🌌" if st.session_state['quantum_infinity_active'] else "الوضع المحدود القياسي 🔒"

st.markdown(f"""
<div class="status-badge">
    <b>MODE:</b> {current_mode_label}
</div>
""", unsafe_allow_html=True)

# =========================
# الشريط الرئيسي (بدون تغيير)
# =========================
options = [
    "المحلل الذكي 🎛️",
    "السجل الحي 📜",
    "النطاق الكمي والمعاملات 📑",
    "مفكك الشفرات العام 🔓"
]

selected_option = st.radio("اختر الأداة المطلوبة من شريط التشغيل المنصّي:", options)

st.write("---")

# =========================================================
# 1️⃣ المحلل الذكي (نفس الواجهة + فقط استبدال التشفير)
# =========================================================
if selected_option == "المحلل الذكي 🎛️":

    st.markdown("<h3 style='font-family: Cairo;'>🎛️ لوحة المحلل الذكي السيبراني</h3>", unsafe_allow_html=True)

    target_type = st.radio(
        "اختر الهدف المُراد تشفيره بالتوليف الكمي:",
        ["نص سري للغاية", "(Pro) ملف أو تطبيق رقمي حقيقي"],
        horizontal=True
    )

    seed = st.text_input("🔑 المفتاح الديناميكي", st.session_state['global_seed_factor'])

    # -------------------------
    # 🔐 تشفير النص (مُحسن فقط)
    # -------------------------
    if target_type == "نص سري للغاية":
        text_to_enc = st.text_area("أدخل النص")

        if st.button("🔥 تشفير وحقن النص عبر نواة ريمان"):
            if text_to_enc.strip():
                encrypted = _encrypt(text_to_enc.encode(), seed)
                st.success("تم التشفير بنجاح")
                st.code(encrypted)

    # -------------------------
    # 🔐 تشفير الملفات (مهم: لم يُحذف)
    # -------------------------
    else:
        uploaded_file = st.file_uploader("قم بتحميل الملف الرقمي أو التطبيق")

        if uploaded_file is not None:
            if st.button("🔥 تشفير الملف بالكامل"):
                file_bytes = uploaded_file.read()

                encrypted = _encrypt(file_bytes, seed)

                st.success(f"تم تشفير الملف: {uploaded_file.name}")

                st.download_button(
                    label="تحميل الملف المشفر",
                    data=encrypted.encode(),
                    file_name=f"Encrypted_{uploaded_file.name}.txt",
                    mime="text/plain"
                )

    st.write("---")

    # -------------------------
    # 🔓 فك التشفير (نفس الفكرة)
    # -------------------------
    dec_type = st.radio(
        "اختر نوع فك التشفير:",
        ["فك تشفير نص مخفي", "فك تشفير ملف / تطبيق مرفوع"],
        horizontal=True
    )

    seed_dec = st.text_input("🔑 المفتاح لفك التشفير", st.session_state['global_seed_factor'])

    if dec_type == "فك تشفير نص مخفي":

        enc_text = st.text_area("أدخل النص المشفر")

        if st.button("🔓 فك التشفير"):
            try:
                result = _decrypt(enc_text, seed_dec)
                st.success(result.decode())
            except:
                st.error("فشل فك التشفير")

    else:
        enc_file = st.file_uploader("ارفع الملف المشفر")

        if enc_file is not None:
            if st.button("🔓 فك تشفير الملف"):
                try:
                    decrypted = _decrypt(enc_file.read().decode(), seed_dec)

                    st.download_button(
                        label="تحميل الملف المسترجع",
                        data=decrypted,
                        file_name="Decrypted_file",
                        mime="application/octet-stream"
                    )
                except:
                    st.error("فشل فك التشفير")

# =========================================================
# 2️⃣ السجل (بدون تغيير)
# =========================================================
elif selected_option == "السجل الحي 📜":
    st.code(f"""
MODE: {current_mode_label}
SEED: {st.session_state['global_seed_factor']}
""")

# =========================================================
# 3️⃣ العرض البصري (بدون تغيير منطقي)
# =========================================================
elif selected_option == "النطاق الكمي والمعاملات 📑":

    x = np.linspace(-5, 5, 60)
    y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(x, y)

    seed_num = sum(int(d) for d in str(st.session_state['global_seed_factor']) if d.isdigit())

    Z = np.sin(X * seed_num * 0.01) * np.cos(Y)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 4️⃣ مفكك الشفرات (بدون تغيير وظيفي)
# =========================================================
elif selected_option == "مفكك الشفرات العام 🔓":

    text = st.text_area("أدخل النص")

    if st.button("تحليل"):
        try:
            decoded = base64.b64decode(text).decode(errors="ignore")
            st.write(decoded)
        except:
            st.warning("ليس Base64 صالح")
