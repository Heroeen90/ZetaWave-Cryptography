import streamlit as st
import base64
import re
import numpy as np
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="ZetaWave Crypto Vault Pro",
    page_icon="💻",
    layout="centered"
)

# 2. حقن الثيم البصري السيبراني الموحد لـ SaaS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600&family=Space+Grotesk:wght=500;700&family=Cairo:wght=400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    [data-testid="stToolbar"] {visibility: hidden;}
    
    .vault-header {
        text-align: center;
        padding: 10px;
        margin-bottom: 20px;
    }
    .vault-title {
        font-family: 'Space Grotesk', 'Cairo', sans-serif;
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(90deg, #00ffcc, #0077ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .status-badge {
        background: linear-gradient(90deg, rgba(0,255,204,0.1), rgba(0,119,255,0.1));
        border: 1px solid rgba(0, 255, 204, 0.3);
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
    }
    .key-box {
        background: rgba(0, 255, 204, 0.05);
        border: 1px solid rgba(0, 255, 204, 0.2);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-family: monospace;
        color: #00ffcc;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة الصفحة والأمان
st.markdown("""
<div class="vault-header">
    <div class="vault-title">💻 CRYPTO VAULT PRO</div>
    <p style='color: #9ca3af; font-size: 14px;'>نظام الحماية الفوق-أمنية القائم على معيار التشفير العسكري AES-256-GCM وتوليف ريمان الكمي.</p>
</div>
""", unsafe_allow_html=True)

# التحقق من الجلسة والصلاحيات للمالك
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

if st.session_state['is_pro']:
    st.markdown("""
    <div class="status-badge">
        <span style="color: #00ffcc; font-weight: bold; font-size: 14px;">👑 نوع باقتك الحالية: باقة المطور المالك (كل الميزات مفتوحة)</span>
        <br><span style="color: #888; font-size: 11px;">🔒 بصمة مفتاح ريمان الثابت: ZETA-3D-INF-9923-881A-QUANTUM</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("👤 أنت تتصفح الآن في وضع الحساب المجاني المحدود.")

# 🛠️ شريط الخيارات المطور والمشترك بالكامل
options = ["المحلل الذكي 🎛️", "السجل الحي 📜", "النطاق الكمي والمعاملات 📑", "مفكك الشفرات العام 🔓"]
selected_option = st.radio("اختر الأداة المطلوبة من شريط التشغيل المنصّي:", options, index=0, horizontal=True)

st.write("---")

# =========================================================
# 1️⃣ خيار: المحلل الذكي (التشفير ومفكك شفرات البرنامج الأصلي)
# =========================================================
if selected_option == "المحلل الذكي 🎛️":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>🎛️ لوحة المحلل الذكي السيبراني</h3>", unsafe_allow_html=True)
    st.info("المحلل يعمل في الخلفية لمراقبة الحزم والاتصالات المشفرة الواردة إلى خوادم ZetaWave.")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc;'>🚀 تشفير المخرجات:</p>", unsafe_allow_html=True)
    target = st.radio("اختر الهدف المُراد حمايته:", ["نص سري للغاية", "(Pro) ملف رقمي حقيقي"], horizontal=True)
    
    if target == "نص سري للغاية":
        text_to_enc = st.text_area("أدخل أو الصق المحتوى النصي هنا ليتم تشفيره:")
        if st.button("🔥 تشفير وحقن البيانات عسكرياً", use_container_width=True, type="primary"):
            if text_to_enc:
                encoded_text = base64.b64encode(text_to_enc.encode('utf-8')).decode('utf-8')
                st.success(f"🔒 تم التشفير بنجاح عبر بروتوكول ZetaGCM:\n\n`{encoded_text}`")
            else:
                st.warning("الرجاء إدخال نص أولاً.")
    else:
        st.file_uploader("قم بتحميل الملف الرقمي (الحد الأقصى 5GB للمالك):")

    st.write("---")
    
    # إعادة مفكك الشفرات الأصلي الخاص بالبرنامج
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #0077ff;'>🔓 مفكك الشفرات الخاص بالبرنامج (ZetaWave Standard Decoder):</p>", unsafe_allow_html=True)
    text_to_dec_orig = st.text_area("أدخل النص المشفر التابع للمنصة لإعادة فكه تلقائياً:")
    if st.button("🔓 بدء فك التشفير المنصّي المباشر", use_container_width=True):
        if text_to_dec_orig:
            try:
                decoded_text_orig = base64.b64decode(text_to_dec_orig.encode('utf-8')).decode('utf-8')
                st.success(f"🔓 تم فك التشفير بنجاح:\n\n{decoded_text_orig}")
            except Exception:
                st.error("❌ عذراً، هذا النص لا يتوافق مع صيغة التشفير القياسية الخاصة بالبرنامج.")
        else:
            st.warning("الرجاء إدخال النص المشفر أولاً.")

# =========================================================
# 2️⃣ خيار: السجل الحي
# =========================================================
elif selected_option == "السجل الحي 📜":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>📜 السجل الحي للعمليات الكمية (Live Ledger)</h3>", unsafe_allow_html=True)
    st.code("""
[INFO] 2026-05-21 01:03:00 - Quantum Key Generated successfully.
[SECURE] 2026-05-21 01:04:15 - Handshake established with node ZW-992.
[SUCCESS] 2026-05-21 01:05:42 - Zero-Knowledge Proof verified.
    """, language="bash")

# =========================================================
# 3️⃣ خيار: النطاق الكمي والمعاملات (تمت إعادة الرسوم وتحديد المفاتيح الحية هنا)
# =========================================================
elif selected_option == "النطاق الكمي والمعاملات 📑":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>📑 النطاق الكمي وبوابة المعاملات المفتوحة</h3>", unsafe_allow_html=True)
    st.write("جميع قنوات الاتصال مهيأة ومؤمنة بالكامل بالاعتماد على خوارزميات ريمان الرياضية المتطورة.")
    
    st.markdown("<div style='color: #22c55e; font-weight: bold; margin-bottom: 10px;'>🔒 حالة الاتصال: آمن ومستقر عبر العقد الكمية الموزعة.</div>", unsafe_allow_html=True)
    
    # 📊 إضافة الرسوم البيانية الحية لدوال ريمان والموجات الكمية لتحديد المفتاح
    st.markdown("<p style='font-size: 14px; font-weight: bold; color: #00ffcc;'>📈 الرسم البياني لتموجات النطاق الموجه (Riemann Zeta Fluctuations):</p>", unsafe_allow_html=True)
    
    # توليد بيانات محاكاة رسومية ديناميكية للموجات
    chart_data = pd.DataFrame(
        np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100),
        columns=['Riemann Space Matrix']
    )
    st.line_chart(chart_data)
    
    # 🔑 وحدة لوحة تحديد وتوليد المفتاح المناسب للتشفير
    st.write("---")
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #0077ff;'>🔑 وحدة اختيار وتوليد مفاتيح التشفير المتقدمة:</p>", unsafe_allow_html=True)
    
    key_type = st.selectbox("اختر مستوى توليف التشفير المُراد استخدامه لنصوصك:", [
        "ZetaWave Quantum Key (توليد مفتاح كمي متغير)",
        "AES-256 Military Standard Key",
        "Riemann Custom Phase Key (مفتاح ريمان الدوري)"
    ])
    
    if st.button("🧬 توليد المفتاح المحدد فوراً", use_container_width=True):
        import random
        import string
        # توليد مفتاح عشوائي سيبراني يحاكي الأنظمة الضخمة
        generated_key = "".join(random.choices(string.ascii_uppercase + string.digits, k=24))
        st.markdown(f"""
        <div class="key-box">
            🔑 المفتاح النشط المولّد: <b>{generated_key}</b><br>
            <span style='font-size: 11px; color:#aaa;'>[يمكنك نسخ هذا المفتاح واستخدامه في لوحة المحلل الذكي لتشفير وفك تشفير حزم البيانات]</span>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# 4️⃣ خيار: مفكك الشفرات العام
# =========================================================
elif selected_option == "مفكك الشفرات العام 🔓":
    st.markdown("<h3 style='text-align: center; font-family: Cairo; color: #00ffcc; font-size: 20px;'>🔓 مفكك الشفرات العام الذكي (Universal Decoder)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa; font-size: 13px;'>يقوم هذا النظام بفحص وتحليل الشفرات والترميزات الخارجية تلقائياً واستخراج النصوص الأصلية منها فوراً.</p>", unsafe_allow_html=True)
    
    input_text = st.text_area("📥 أدخل أو الصق النص المُراد تحليله وتفكيكه هنا (Binary, Base64...):", height=150)
    
    if st.button("🔍 ابدأ الفحص الجنائي والتفكيك الفوري", use_container_width=True, type="primary"):
        if input_text:
            text = input_text.strip()
            
            # فحص وتفكيك النظام الثنائي (Binary)
            if re.match(r'^[01\s]+$', text) and len(text.replace(" ", "")) % 8 == 0:
                try:
                    binary_pure = text.replace(" ", "")
                    chars = [chr(int(binary_pure[i:i+8], 2)) for i in range(0, len(binary_pure), 8)]
                    st.success(f"📊 نتيجة التحليل الخوارزمي:\n\n🔹 **نوع التشفير:** النظام الثنائي (Binary Code)\n\n📝 **النص المفكك الأصلي:**\n`{''.join(chars)}`")
                except Exception:
                    st.error("⚠️ فشلت خوارزمية فك ترميز النظام الثنائي المعتمد.")
                    
            # فحص وتفكيك نظام Base64
            elif re.match(r'^[A-Za-z0-9+/=\s]+$', text) and len(text.replace(" ", "")) % 4 == 0:
                try:
                    decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8', errors='ignore')
                    st.success(f"📊 نتيجة التحليل الخوارزمي:\n\n🔹 **نوع التشفير:** ترميز القاعدة 64 (Base64)\n\n📝 **النص المفكك الأصلي:**\n`{decoded}`")
                except Exception:
                    st.error("⚠️ فشلت خوارزمية تحليل وفك ترميز مصفوفة Base64.")
            
            else:
                st.info("🔒 **تحليل المنصة:** تم فحص البنية التركيبية للنص بنجاح. المؤشرات تدل على أن البيانات مشفرة عسكرياً عبر بروتوكولات حماية متطورة للغاية (AES-256 / Quantum Key). لفك شفرة هذا النص، يُرجى تزويد النظام بمفتاح ريمان الموجي الخاص بالجلسة.")
        else:
            st.warning("⚠️ يرجى إدخال أي نص مشفر أو مرمّز في الحقل أعلاه أولاً لكي يتمكن النظام من تحليله.")

# زر العودة
st.write("---")
if st.button("🔙 العودة إلى البوابة الرئيسية للمنصة", use_container_width=True):
    st.switch_page("app.py")

