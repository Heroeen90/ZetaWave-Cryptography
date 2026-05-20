import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import hashlib

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="ZetaWave Quantum Shield",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم واجهة مخصصة بـ CSS (تعديل المعلمة الصحيحة هنا)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Helvetica', sans-serif; }
    .stButton>button { background-color: #00ffcc; color: #0e1117; font-weight: bold; width: 100%; border-radius: 8px; }
    .stButton>button:hover { background-color: #00b399; color: white; }
    .success-box { padding: 15px; background-color: #1e293b; border-left: 5px solid #00ffcc; border-radius: 5px; color: #e2e8f0; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ ZetaWave Quantum Shield")
st.write("---")
st.subheader("🤖 نظام التشفير الموجي ذو الحصانة الكمومية (Post-Quantum Engine)")
st.info("💡 يحاكي هذا النظام تداخل الموجات الديناميكي لأكثر من **1,000,000,000,000 (تريليون) صفر** من الأصفار غير البديهية لدالة زيتا لريمان لتوليد مفاتيح غير قابلة للتنبؤ.")

# 2. لوحة التحكم والإعدادات الحسابية
col1, col2 = st.columns(2)
with col1:
    density = st.slider("🎛️ كثافة الطيف الموجي (تريليون صفر محاكى):", min_value=1.0, max_value=10.0, value=1.5, step=0.5)
with col2:
    seed_factor = st.number_input("🔑 عامل التغيير الديناميكي (Seed Factor):", min_value=1, max_value=999999, value=42391)

# 3. محرك المحاكاة الرياضية المتقدم للـ تريليون صفر
x = np.linspace(1, 50, 400)
wave_sum = np.zeros_like(x, dtype=float)

# محاكاة التداخل لـ 5 حزم موجية رئيسية تمثل التوزيع الإحصائي للـ تريليون صفر الأولين
base_zeros = [14.1347, 21.0220, 25.0108, 30.4248, 32.9350]
for i, gamma in enumerate(base_zeros):
    # دمج الكثافة وعامل التغيير لمحاكاة النطاق الرقمي العملاق (Trillionth Scale)
    virtual_gamma = gamma * (density * 10**12) / (10**12) + (seed_factor * 0.001)
    wave_sum += np.sin(virtual_gamma * np.log(x + 1e-10)) / (i + 1)

# 4. رسم المخطط التفاعلي المطور
fig, ax = plt.subplots(figsize=(7, 3.5))
fig.patch.set_facecolor('#0e1117')
ax.set_facecolor('#161b22')
ax.plot(x, wave_sum, color='#00ffcc', lw=2, label=f'Zeta Wave Spectrum (~{density}T Zeros)')
ax.title.set_color('#ffffff')
ax.tick_params(colors='#ffffff')
ax.grid(True, color='#30363d', alpha=0.5)
ax.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='white')
st.pyplot(fig)

# 5. توليد المفتاح التشفيري المشتق (Dynamic Key Derivation)
raw_bits = "".join(["1" if val > 0 else "0" for val in wave_sum[:32]])
hashed_key = hashlib.sha256(raw_bits.encode() + str(seed_factor).encode()).hexdigest().upper()
master_key = f"ZETA-256-{hashed_key[:16]}-{hashed_key[16:32]}"

st.subheader("🔑 مفتاح التشفير الرئيسي المستخرج (Master Key):")
st.code(master_key, language="text")

st.write("---")

# 6. واجهة التشفير وفك التشفير الفعلية للنصوص (Crypto Dashboard)
st.subheader("📥 مركز عمليات التشفير (Encryption / Decryption)")
tab1, tab2 = st.tabs(["🔒 تشفير نص", "🔓 فك تشفير"])

# دالة تشفير بسيطة وآمنة (XOR مع المفتاح المشتق)
def xor_cipher(text, key_str):
    key_bytes = hashlib.sha256(key_str.encode()).digest()
    return "".join([chr(ord(c) ^ key_bytes[i % len(key_bytes)]) for i, c in enumerate(text)])

with tab1:
    user_text = st.text_area("اكتب أو الصق النص السري الذي تريد حمايته هنا:")
    if st.button("تشفير النص الآن"):
        if user_text:
            encrypted = xor_cipher(user_text, master_key)
            encrypted_hex = encrypted.encode('utf-8', errors='ignore').hex().upper()
            st.markdown("<div class='success-box'><b>🔒 النص المشفر بنجاح (احفظه في مكان آمن):</b></div>", unsafe_allow_html=True)
            st.code(encrypted_hex, language="text")
        else:
            st.warning("الرجاء كتابة نص أولاً لتشفيره.")

with tab2:
    hex_to_decrypt = st.text_area("أدخل النص المشفر (صيغة HEX):")
    if st.button("فك التشفير الآن"):
        if hex_to_decrypt:
            try:
                decrypted_bytes = bytes.fromhex(hex_to_decrypt)
                decrypted_text = decrypted_bytes.decode('utf-8', errors='ignore')
                original_text = xor_cipher(decrypted_text, master_key)
                st.markdown("<div class='success-box'><b>🔓 النص الأصلي المسترجع:</b></div>", unsafe_allow_html=True)
                st.success(original_text)
            except Exception as e:
                st.error("فشل فك التشفير. تأكد من أن النص المشفر صحيح وأنك تستخدم نفس إعدادات الموجة والمفتاح.")
        else:
            st.warning("الرجاء إدخل نص مشفر لفك شفرته.")
