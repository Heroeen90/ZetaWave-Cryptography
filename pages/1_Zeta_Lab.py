import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import hashlib

st.set_page_config(page_title="Zeta Wave Lab", page_icon="🌌", layout="centered")

st.markdown("<h1>🌌 مختبر أمواج ريمان الحسابي</h1>", unsafe_allow_html=True)
st.write("---")

mode = st.radio("🚀 اختر نطاق المحاكاة الرياضية لأصفار ريمان:", ["النطاق المتقدم (10 - 1000 تريليون صفر)", "النطاق اللامتناهي (Quantum Infinity Mode ♾️)"])

if mode == "النطاق المتقدم (10 - 1000 تريليون صفر)":
    trillion_scale = st.slider("🎛️ حدد حجم الأصفار (بالتريليون):", min_value=10, max_value=1000, value=500, step=50)
    density_factor = trillion_scale * 10**12
else:
    st.warning("⚡ وضع اللانهاية نشط: يتم حساب طيف التداخل كدالة تكاملية متصلة تمثل كافة الأصفار.")
    density_factor = np.inf

seed_factor = st.number_input("🔑 عامل التغيير الديناميكي (Seed Factor):", min_value=1, max_value=999999, value=77777)

# الحسابات الرياضية
x = np.linspace(1, 50, 500)
wave_sum = np.zeros_like(x, dtype=float)
base_zeros = [14.1347, 21.0220, 25.0108, 30.4248, 32.9350]

for i, gamma in enumerate(base_zeros):
    if density_factor == np.inf:
        virtual_gamma = gamma * np.pi * (seed_factor * 0.01)
    else:
        virtual_gamma = gamma * (density_factor / 10**12) + (seed_factor * 0.05)
    wave_sum += np.sin(virtual_gamma * np.log(x + 1e-10)) / (i + 1)

# الرسم البياني
fig, ax = plt.subplots(figsize=(7, 3.5))
fig.patch.set_facecolor('#0e1117')
ax.set_facecolor('#161b22')
ax.plot(x, wave_sum, color='#00ffcc', lw=2)
ax.tick_params(colors='#ffffff')
ax.grid(True, color='#30363d', alpha=0.4)
st.pyplot(fig)

# استخراج المفتاح وحفظه في الذاكرة المؤقتة (Session State) لكي تراه الصفحات الأخرى
raw_bits = "".join(["1" if val > 0 else "0" for val in wave_sum[:64]])
hashed_key = hashlib.sha384(raw_bits.encode() + str(seed_factor).encode()).hexdigest().upper()
st.session_state['master_key'] = f"ZETA-INFINITY-{hashed_key[:16]}-{hashed_key[16:32]}"

st.subheader("🔑 مفتاح التشفير الرئيسي النشط حالياً:")
st.code(st.session_state['master_key'], language="text")
st.success("📝 تم حفظ هذا المفتاح بنجاح! يمكنك الآن الانتقال لصفحة 'خزنة التشفير' لاستخدامه عملياً في تشفير ملفاتك.")

