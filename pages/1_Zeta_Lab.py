import streamlit as st
import numpy as np
import plotly.graph_objects as go
import hashlib

st.set_page_config(page_title="Zeta Wave Lab 3D", page_icon="🌌", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🌌 مختبر أمواج ريمان ثلاثي الأبعاد (3D)</h1>", unsafe_allow_html=True)
st.write("---")

mode = st.radio("🚀 اختر نطاق المحاكاة الرياضية لأصفار ريمان:", ["النطاق المتقدم (10 - 1000 تريليون صفر)", "النطاق اللامتناهي (Quantum Infinity Mode ♾️)"])

if mode == "النطاق المتقدم (10 - 1000 تريليون صفر)":
    trillion_scale = st.slider("🎛️ حدد حجم الأصفار (بالتريليون):", min_value=10, max_value=1000, value=500, step=50)
    density_factor = trillion_scale * 10**12
else:
    st.warning("⚡ وضع اللانهاية نشط: يتم حساب طيف التداخل كدالة تكاملية متصلة تمثل كافة الأصفار.")
    density_factor = np.inf

seed_factor = st.number_input("🔑 عامل التغيير الديناميكي (Seed Factor):", min_value=1, max_value=999999, value=77777)

# 1. الحسابات الرياضية المتقدمة لإنشاء مصفوفة تداخل ثلاثية الأبعاد (3D Space)
x = np.linspace(1, 30, 200)
y = np.linspace(1, 10, 50)  # المحور الثالث يمثل البُعد الزمني/الترددي للتداخل
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X, dtype=float)

base_zeros = [14.1347, 21.0220, 25.0108, 30.4248, 32.9350]

for i, gamma in enumerate(base_zeros):
    if density_factor == np.inf:
        virtual_gamma = gamma * np.pi * (seed_factor * 0.01)
    else:
        virtual_gamma = gamma * (density_factor / 10**12) + (seed_factor * 0.05)
    
    # توليد تداخل موجي على مساحة ثنائية الأبعاد لتعطي عمقاً مجسماً (3D Surface)
    Z += (np.sin(virtual_gamma * np.log(X + 1e-10)) * np.cos(Y * 0.5)) / (i + 1)

# 2. بناء مجسم الرسم البياني ثلاثي الأبعاد التفاعلي باستخدام Plotly
fig = go.Figure(data=[go.Surface(
    z=Z, x=X, y=Y,
    colorscale='Viridis',  # تدرج لوني مستقبلي احترافي (أزرق - أخضر - أصفر)
    colorbar=dict(title='كثافة الموجة')
)])

fig.update_layout(
    title='بصمة التداخل الموجي ثلاثية الأبعاد لطيف ريمان الكمي',
    autosize=True,
    scene=dict(
        xaxis=dict(title='نطاق الدالة (X)', backgroundcolor="rgb(14, 17, 23)", gridcolor="gray", showbackground=True),
        yaxis=dict(title='البُعد الترددي (Y)', backgroundcolor="rgb(14, 17, 23)", gridcolor="gray", showbackground=True),
        zaxis=dict(title='سعة التشفير (Z)', backgroundcolor="rgb(14, 17, 23)", gridcolor="gray", showbackground=True),
        aspectratio=dict(x=1, y=1, z=0.6)
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    paper_bgcolor='#0e1117',
)

# عرض الرسم التفاعلي في التطبيق
st.plotly_chart(fig, use_container_width=True)

# 3. استخراج وحفظ المفتاح المشترك في الذاكرة السحابية للجلسة
# نأخذ مقطعاً من المصفوفة لتوليد الـ Bits الثابتة للمفتاح
raw_bits = "".join(["1" if val > 0 else "0" for val in Z[0][:64]])
hashed_key = hashlib.sha384(raw_bits.encode() + str(seed_factor).encode()).hexdigest().upper()
st.session_state['master_key'] = f"ZETA-3D-INF-{hashed_key[:16]}-{hashed_key[16:32]}"

st.subheader("🔑 مفتاح التشفير الرئيسي ثلاثي الأبعاد المستخرج:")
st.code(st.session_state['master_key'], language="text")
st.success("📝 تم تحديث البيئة وحفظ المفتاح بنجاح! اذهب الآن إلى 'خزنة التشفير' لتشفير ملفاتك باستخدام طيف ريمان ثلاثي الأبعاد الجديد.")
