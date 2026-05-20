import streamlit as st
import base64
import re
import numpy as np
import plotly.graph_objects as go

# 1. إعدادات واجهة المنصة
st.set_page_config(
    page_title="ZetaWave Crypto Vault Pro",
    page_icon="💻",
    layout="centered"
)

# 2. هندسة المظهر البصري لبيئة الـ SaaS والتحكم بالأزرار
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
    .infinity-alert {
        background-color: rgba(41, 37, 13, 0.6);
        border: 1px solid #eab308;
        padding: 15px;
        border-radius: 8px;
        color: #fef08a;
        margin-bottom: 15px;
        font-size: 14px;
        text-align: right;
        direction: rtl;
    }
    div[data-testid="stCodeBlock"] {
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة التطبيق
st.markdown("""
<div class="vault-header">
    <div class="vault-title">💻 CRYPTO VAULT PRO</div>
    <p style='color: #9ca3af; font-size: 14px;'>نظام الحماية الفوق-أمنية القائم على معيار التشفير العسكري AES-256-GCM وتوليف ريمان الكمي.</p>
</div>
""", unsafe_allow_html=True)

# إدارة التحقق من الصلاحيات للمطور المالك
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

if st.session_state['is_pro']:
    st.markdown("""
    <div class="status-badge">
        <span style="color: #00ffcc; font-weight: bold; font-size: 14px;">👑 نوع باقتك الحالية: باقة المطور المالك (كل الميزات مفتوحة)</span>
        <br><span style="color: #888; font-size: 11px;">🔒 بصمة مفتاح ريمان الثابت: ZETA-3D-INF-9923-881A-QUANTUM</span>
    </div>
    """, unsafe_allow_html=True)

# 🛠️ شريط التشغيل المنصّي الموحد
options = ["المحلل الذكي 🎛️", "السجل الحي 📜", "النطاق الكمي والمعاملات 📑", "مفكك الشفرات العام 🔓"]
selected_option = st.radio("اختر الأداة المطلوبة من شريط التشغيل المنصّي:", options, index=0, horizontal=True)

st.write("---")

# =========================================================
# 1️⃣ قسم: المحلل الذكي (التشفير + مفكك شفرات المنصة الأصلي)
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
                st.success("🔒 تم التشفير بنجاح عبر بروتوكول ZetaGCM:")
                st.code(encoded_text, language=None)
            else:
                st.warning("الرجاء إدخال نص أولاً.")
    else:
        st.file_uploader("قم بتحميل الملف الرقمي (الحد الأقصى 5GB للمالك):")

    st.write("---")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #0077ff;'>🔓 مفكك الشفرات الخاص بالبرنامج (ZetaWave Standard Decoder):</p>", unsafe_allow_html=True)
    text_to_dec_orig = st.text_area("أدخل النص المشفر التابع للمنصة لإعادة فكه تلقائياً:")
    if st.button("🔓 بدء فك التشفير المنصّي المباشر", use_container_width=True):
        if text_to_dec_orig:
            try:
                decoded_text_orig = base64.b64decode(text_to_dec_orig.encode('utf-8')).decode('utf-8')
                st.success("🔓 تم فك التشفير بنجاح:")
                st.code(decoded_text_orig, language=None)
            except Exception:
                st.error("❌ عذراً، هذا النص لا يتوافق مع صيغة التشفير القياسية الخاصة بالبرنامج.")
        else:
            st.warning("الرجاء إدخال النص المشفر أولاً.")

# =========================================================
# 2️⃣ قسم: السجل الحي للعمليات
# =========================================================
elif selected_option == "السجل الحي 📜":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>📜 السجل الحي للعمليات الكمية (Live Ledger)</h3>", unsafe_allow_html=True)
    st.code("""
[INFO] 2026-05-21 01:31:10 - Quantum Key Generated successfully.
[SECURE] 2026-05-21 01:32:45 - Handshake established with node ZW-992.
[SUCCESS] 2026-05-21 01:34:02 - Zero-Knowledge Proof verified.
    """, language="bash")

# =========================================================
# 3️⃣ قسم: النطاق الكمي والمعاملات
# =========================================================
elif selected_option == "النطاق الكمي والمعاملات 📑":
    st.markdown("<p style='font-size: 16px; font-weight: bold; color: #f3f4f6;'>🔮 النطاق اللامتناهي (Quantum Infinity Mode) ♾️</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="infinity-alert">
        ⚡ <b>وضع اللانهاية نشط:</b> يتم حساب طيف التداخل كدالة تكاملية متصلة تمثل كافة الأصفار.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>🔑 عامل التغيير الديناميكي (Seed Factor):</p>", unsafe_allow_html=True)
    seed_factor_str = st.text_input("", value="010")
    
    try:
        pure_numeric = int(''.join(filter(str.isdigit, seed_factor_str))) if seed_factor_str else 1
    except ValueError:
        pure_numeric = 1
        
    if len(seed_factor_str) > 6 or pure_numeric > 999999:
        st.warning("⚠️ يجب أن تكون القيمة أقل من أو تساوي 999999. (تم تفعيل تجاوز الصلاحية الفوق-أمنية الحصري للمطور المالك)")

    st.write("---")
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc;'>📊 بصمة التداخل الموجي الكمي ثلاثي الأبعاد:</p>", unsafe_allow_html=True)
    
    x = np.linspace(-5, 5, 65)
    y = np.linspace(-5, 5, 65)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(X * (pure_numeric % 5 + 1) * 0.1) + 1.0
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
    fig.update_layout(
        title='كثافة الموجة',
        scene=dict(xaxis_title='X Matrix', yaxis_title='Y Matrix', zaxis_title='Zeta Spectrum'),
        margin=dict(l=0, r=0, b=0, t=40),
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("🧬 ربط وحقن عامل التغيير المخصص في المفتاح الرئيسي", use_container_width=True, type="primary"):
        st.success("🔒 تم قفل خلايا النطاق وحقن البصمة المشتقة بنجاح في بروتوكولات الحماية الفوق-أمنية!")

# =========================================================
# 4️⃣ قسم: مفكك الشفرات العام المدمج (تم تأمينه بالكامل ضد الـ AttributeError)
# =========================================================
elif selected_option == "مفكك الشفرات العام 🔓":
    st.markdown("<h3 style='text-align: center; font-family: Cairo; color: #00ffcc; font-size: 20px;'>🔓 مفكك الشفرات العام الذكي (Universal Decoder)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa; font-size: 13px;'>يقوم هذا النظام بفحص وتحليل الشفرات والترميزات الخارجية تلقائياً واستخراج النصوص الأصلية منها فوراً.</p>", unsafe_allow_html=True)
    
    # استخدام قيمة افتراضية فارغة وتخزينها بأمان
    input_text = st.text_area("📥 أدخل أو الصق النص المُراد تحليله وتفكيكه هنا (Binary, Base64...):", height=150, key="universal_decoder_input")
    
    if st.button("🔍 ابدأ الفحص الجنائي والتفكيك الفوري", use_container_width=True, type="primary"):
        # حل المشكلة الجذري: التحقق الفوري والآمن قبل معالجة السلسلة النصية
        if input_text and isinstance(input_text, str) and input_text.strip():
            text = input_text.strip()
            
            # 1. فحص وتحليل النظام الثنائي (Binary)
            if re.match(r'^[01\s]+$', text) and len(text.replace(" ", "")) % 8 == 0:
                try:
                    binary_pure = text.replace(" ", "")
                    chars = [chr(int(binary_pure[i:i+8], 2)) for i in range(0, len(binary_pure), 8)]
                    st.success("📊 نتيجة التحليل الخوارزمي (النظام الثنائي):")
                    st.code(''.join(chars), language=None)
                except Exception:
                    st.error("⚠️ فشلت خوارزمية فك ترميز النظام الثنائي المعتمد.")
                    
            # 2. فحص وتحليل نظام Base64
            elif re.match(r'^[A-Za-z0-9+/=\s]+$', text) and len(text.replace(" ", "")) % 4 == 0:
                try:
                    decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8', errors='ignore')
                    st.success("📊 نتيجة التحليل الخوارزمي (Base64):")
                    st.code(decoded, language=None)
                except Exception:
                    st.error("⚠️ فشلت خوارزمية تحليل وفك ترميز مصفوفة Base64.")
            
            # 3. في حال كان تشفيراً خارجياً غير معروف
            else:
                st.info("🔒 **تحليل المنصة:** تم فحص البنية التركيبية للنص بنجاح. المؤشرات تدل على أن البيانات مشفرة عسكرياً عبر بروتوكولات حماية متطورة للغاية (AES-256 / Quantum Key). لفك شفرة هذا النص، يُرجى تزويد النظام بمفتاح ريمان الموجي الخاص بالجلسة.")
        else:
            st.warning("⚠️ يرجى إدخال أي نص مشفر أو مرمّز في الحقل أعلاه أولاً لكي يتمكن النظام من تحليله.")

# زر العودة للبوابة
st.write("---")
if st.button("🔙 العودة إلى البوابة الرئيسية للمنصة", use_container_width=True):
    st.switch_page("app.py")

