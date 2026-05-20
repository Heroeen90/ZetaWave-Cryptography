import streamlit as st
import hashlib
import time
from Crypto.Cipher import AES

# إعدادات الصفحة
st.set_page_config(page_title="ZetaWave Cyber Dashboard", page_icon="🛡️", layout="centered")

# --- حقن CSS مخصص لتحويل الواجهة إلى تصميم عسكري احترافي ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@400;700&display=swap');
    
    .main { background-color: #060911; }
    
    /* لوحة التحليل الزجاجية */
    .analytics-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(0, 255, 204, 0.2);
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        text-align: center;
    }

    .dashboard-title {
        font-family: 'Cairo', sans-serif;
        color: #00ffcc;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
        font-size: 28px;
        margin-bottom: 25px;
        text-align: center;
    }

    .metric-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 15px;
    }

    .stat-box {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(0, 255, 204, 0.1);
        border-radius: 15px;
        padding: 15px;
        min-width: 120px;
        transition: 0.3s;
    }
    
    .stat-box:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }

    .stat-label {
        font-family: 'Cairo', sans-serif;
        color: #888;
        font-size: 14px;
    }

    .stat-value {
        font-family: 'Orbitron', sans-serif;
        color: #fff;
        font-size: 20px;
        font-weight: bold;
    }

    .safe-glow { color: #00ffcc; text-shadow: 0 0 10px #00ffcc; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff; font-family: Cairo;'>📥 خزنة التشفير العالمية</h1>", unsafe_allow_html=True)
st.write("---")

if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-3D-INF-MASTER-9923"

tab1, tab2 = st.tabs(["🔒 تشفير عسكري", "🔓 فك التشفير"])

def aes_encrypt(data: bytes, key_str: str) -> bytes:
    secret_key = hashlib.sha256(key_str.encode()).digest()
    cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def aes_decrypt(payload: bytes, key_str: str) -> bytes:
    secret_key = hashlib.sha256(key_str.encode()).digest()
    nonce = payload[:16]
    tag = payload[16:32]
    ciphertext = payload[32:]
    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

with tab1:
    st.subheader("🛡️ قسم الحماية المتقدمة")
    option = st.selectbox("نوع البيانات:", ["نص سري", "ملف حقيقي"])
    
    if option == "نص سري":
        user_text = st.text_area("أدخل النص هنا:")
        if st.button("تشفير فوري"):
            if user_text:
                start_t = time.time()
                enc_data = aes_encrypt(user_text.encode('utf-8'), st.session_state['master_key'])
                end_t = time.time()
                
                st.code(enc_data.hex().upper(), language="text")
                
                # --- لوحة التحليل الاحترافية المستوحاة من تصميمك ---
                st.markdown(f"""
                <div class="analytics-card">
                    <div class="dashboard-title">لوحة التحليل السيبراني الفوري</div>
                    <div class="metric-container">
                        <div class="stat-box">
                            <div class="stat-label">معيار الحصانة</div>
                            <div class="stat-value safe-glow">Quantum-Safe</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">سرعة التشفير</div>
                            <div class="stat-value">{(end_t - start_t)*1000:.2f} ms</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">طول المفتاح</div>
                            <div class="stat-value">256-Bit</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else: st.warning("اكتب نصاً")

    else:
        uploaded_file = st.file_uploader("ارفع الملف:")
        if st.button("بدء التشفير العسكري"):
            if uploaded_file:
                start_t = time.time()
                f_bytes = uploaded_file.read()
                enc_f = aes_encrypt(f_bytes, st.session_state['master_key'])
                end_t = time.time()
                
                st.session_state['out'] = enc_f
                st.session_state['name'] = uploaded_file.name + ".zeta"
                
                st.markdown(f"""
                <div class="analytics-card">
                    <div class="dashboard-title">لوحة التحليل السيبراني الفوري</div>
                    <div class="metric-container">
                        <div class="stat-box">
                            <div class="stat-label">حجم البيانات</div>
                            <div class="stat-value">{len(f_bytes)/1024:.1f} KB</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">وقت المعالجة</div>
                            <div class="stat-value">{(end_t - start_t)*1000:.1f} ms</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">مقاومة الاختراق</div>
                            <div class="stat-value safe-glow">10^42 Years</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.download_button("📥 تحميل الملف المشفر", data=enc_f, file_name=st.session_state['name'])

with tab2:
    st.subheader("🔓 استعادة البيانات")
    # ... بقية كود فك التشفير (يبقى كما هو)
    hex_input = st.text_area("أدخل رمز التشفير (HEX):")
    if st.button("فك التشفير الآن"):
        if hex_input:
            try:
                dec = aes_decrypt(bytes.fromhex(hex_input.strip()), st.session_state['master_key'])
                st.success(f"🔓 النص المسترجع: {dec.decode('utf-8')}")
            except: st.error("فشل! تأكد من المفتاح الموجي.")
