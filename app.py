import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="ZetaWave Crypto", layout="centered")

st.title("⚡ محرك تشفير موجات ريمان")
st.write("نظام تجريبي لتوليد مفاتيح تشفير ديناميكية بناءً على أصفار ريمان.")

# أصفار ريمان الثابتة
RIEMANN_ZEROS = [14.134725142, 21.022039639, 25.010857580, 30.424876126]

# لوحة تحكم مبسطة متوافقة مع الموبايل (ليست في القائمة الجانبية لتسهيل العرض)
num_zeros = st.slider("عدد الأصفار النشطة:", min_value=1, max_value=4, value=2)

# توليد البيانات الحسابية
x = np.linspace(2, 40, 300)
wave_sum = np.zeros_like(x, dtype=float)
for gamma in RIEMANN_ZEROS[:num_zeros]:
    wave_sum += np.sin(gamma * np.log(x + 1e-9)) / (gamma * 0.5)

# بناء الرسم البياني بحجم مرن ومتوافق مع الموبايل
fig, ax = plt.subplots(figsize=(6, 3.5)) # أبعاد أصغر مخصصة للموبايل
ax.plot(x, wave_sum, color='#0088ff', lw=2)
ax.grid(True, alpha=0.3)

# عرض الرسم البياني داخل التطبيق
st.pyplot(fig)

# توليد وعرض المفتاح
peaks = np.where(wave_sum > 0.2, 1, 0)
binary_str = "".join(map(str, peaks[:16]))
try:
    hex_key = hex(int(binary_str, 2))[2:].upper().zfill(4)
except ValueError:
    hex_key = "A9F4"

st.subheader("🔑 المفتاح الموجي المستخرج:")
st.code(f"ZETA-{hex_key}", language="text")
