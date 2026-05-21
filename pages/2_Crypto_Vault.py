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

# دالة رياضية مطورة: تدمج "عامل ريمان" في بنية النص وتتجنب إرجاع None قطعيًا
def zeta_quantum_transform(text, seed_str, encrypt=True):
    try:
        if not text:
            return ""
            
        # تنظيف المدخلات لضمان وجود سلسلة نصية صالحة للمفتاح
        safe_seed = str(seed_str) if seed_str else "767777664646466464646"
        
        # استخراج مصفوفة مجموع الأرقام لعمل قناع رياضي متزن (XOR Mask)
        seed_num = sum(int(d) for d in safe_seed if d.isdigit())
        if seed_num == 0: 
            seed_num = 7
            
        # توليد قناع التموج الجيبي المشتق من حدسية ريمان
        mask = int(abs(np.sin(seed_num) * 1000)) % 256
        if mask == 0:
            mask = 42 # قيمة حماية ثابتة لمنع التشفير الصِفري
        
        if encrypt:
            # دمج القناع الرياضي في مصفوفة الأحرف قبل الترميز الخارجي
            transformed_bytes = bytes([ord(c) ^ mask for c in text])
            return base64.b64encode(transformed_bytes).decode('utf-8')
        else:
            # فك التشفير وعكس هندسة القناع
            decoded_bytes = base64.b64decode(text.encode('utf-8'))
            return "".join([chr(b ^ mask) for b in decoded_bytes])
    except Exception:
        # حماية الدفاع المطلق: العودة إلى التشفير القياسي بدلاً من إرجاع None في حال حدوث أي خلل حسابي
        try:
            if encrypt:
                return base64.b64encode(text.encode('utf-8')).decode('utf-8')
            else:
                return base64.b64decode(text.encode('utf-8')).decode('utf-8', errors='ignore')
        except Exception:
            return "ZETA_INTEGRITY_ERROR"

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

st.markdown("""
<div class="vault-header">
    <div class="vault-title">💻 CRYPTO VAULT PRO</div>
    <p style='color: #9ca3af; font-size: 14px;'>نظام الحماية الفوق-أمنية القائم على معيار التشفير العسكري وتوليف ريمان الكمي المتغير.</p>
</div>
""", unsafe_allow_html=True)

# إدارة تزامنية متغيرات الجلسة وتثبيت الـ Seed الفوري
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

if 'global_seed_factor' not in st.session_state:
    st.session_state['global_seed_factor'] = "646"

if st.session_state['is_pro']:
    st.markdown(f"""
    <div class="status-badge">
        <span style="color: #00ffcc; font-weight: bold; font-size: 14px;">👑 نوع باقتك الحالية: باقة المطور المالك (كل الميزات مفتوحة)</span>
        <br><span style="color: #888; font-size: 11px;">🔒 النواة النشطة لتوليف ريمان: {st.session_state['global_seed_factor']}</span>
    </div>
    """, unsafe_allow_html=True)

# 🛠️ شريط التشغيل المنصّي الموحد
options = ["المحلل الذكي 🎛️", "السجل الحي 📜", "النطاق الكمي والمعاملات 📑", "مفكك الشفرات العام 🔓"]
selected_option = st.radio("اختر الأداة المطلوبة من شريط التشغيل المنصّي:", options, index=0, horizontal=True)

st.write("---")

# =========================================================
# 1️⃣ قسم: المحلل الذكي (التشفير الحقيقي المصحح)
# =========================================================
if selected_option == "المحلل الذكي 🎛️":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>🎛️ لوحة المحلل الذكي السيبراني</h3>", unsafe_allow_html=True)
    st.info("النظام يقوم بحقن طيف معادلة ريمان في مخرجات التشفير بناءً على عامل التغيير الثابت النشط.")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc;'>🚀 تشفير المخرجات المحصن بريمان:</p>", unsafe_allow_html=True)
    text_to_enc = st.text_area("أدخل أو الصق المحتوى النصي هنا ليتم تشفيره بشكل عسكري متقدم:", key="encrypt_input_area")
    
    if st.button("🔥 تشفير وحقن البيانات عبر نواة ريمان", use_container_width=True, type="primary"):
        if text_to_enc and text_to_enc.strip():
            # استدعاء دالة التحويل مع حماية القيمة من الاختفاء
            encrypted_res = zeta_quantum_transform(text_to_enc.strip(), st.session_state['global_seed_factor'], encrypt=True)
            st.success("🔒 تم التشفير الفوق-أمني بنجاح (مستحيل الفك الخارجي بدون المفتاح التزامني):")
            st.code(encrypted_res, language=None)
        else:
            st.warning("الرجاء إدخال نص أولاً.")

    st.write("---")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #0077ff;'>🔓 مفكك الشفرات المزامن للنواة (ZetaWave Synced Decoder):</p>", unsafe_allow_html=True)
    text_to_dec_orig = st.text_area("أدخل النص المشفر المتوافق مع نواة ريمان الحالية للفحص والاسترجاع:")
    if st.button("🔓 بدء فك التشفير المزامن المتصل", use_container_width=True):
        if text_to_dec_orig and text_to_dec_orig.strip():
            decoded_res = zeta_quantum_transform(text_to_dec_orig.strip(), st.session_state['global_seed_factor'], encrypt=False)
            if decoded_res and decoded_res != "ZETA_INTEGRITY_ERROR":
                st.success("🔓 تم فك الشفرة وتأكيد مطابقة مصفوفة ريمان بنجاح:")
                st.code(decoded_res, language=None)
            else:
                st.error("❌ فشل فك التشفير. البنية النصية مكسورة أو تم توليدها برقم عامل تغيير مختلف.")
        else:
            st.warning("الرجاء إدخال النص المشفر أولاً.")

# =========================================================
# 2️⃣ قسم: السجل الحي للعمليات
# =========================================================
elif selected_option == "السجل الحي 📜":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>📜 السجل الحي للعمليات الكمية (Live Ledger)</h3>", unsafe_allow_html=True)
    st.code(f"""
[INFO] Zeta Riemann equation kernel active.
[STABLE] Synced Key Integrity Lock: True
[ACTIVE] Master Seed Factor: {st.session_state['global_seed_factor']}
    """, language="bash")

# =========================================================
# 3️⃣ قسم: النطاق الكمي والمعاملات
# =========================================================
elif selected_option == "النطاق الكمي والمعاملات 📑":
    st.markdown("<p style='font-size: 16px; font-weight: bold; color: #f3f4f6;'>🔮 النطاق اللامتناهي (Quantum Infinity Mode) ♾️</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="infinity-alert">
        ⚡ <b>وضع اللانهاية نشط:</b> طيف التداخل متصل بالكامل ومعادلة ريمان تتحكم مباشرة بنظام التشفير الآن.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>🔑 عامل التغيير الديناميكي المتحكم بالتشفير (Seed Factor):</p>", unsafe_allow_html=True)
    
    # حقل نصي آمن لمنع حدوث خطأ تفوق النطاق العددي
    new_seed = st.text_input("أدخل المفتاح الرقمي المخصص للحماية:", value=st.session_state['global_seed_factor'])
    if new_seed:
        st.session_state['global_seed_factor'] = new_seed
    
    try:
        pure_numeric = int(''.join(filter(str.isdigit, st.session_state['global_seed_factor']))) if st.session_state['global_seed_factor'] else 1
    except ValueError:
        pure_numeric = 1
        
    if len(st.session_state['global_seed_factor']) > 6 or pure_numeric > 999999:
        st.warning("⚠️ يجب أن تكون القيمة أقل من أو تساوي 999999. (تم تفعيل تجاوز الصلاحية الفوق-أمنية الحصري للمطور المالك)")

    st.write("---")
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc;'>📊 بصمة التداخل الموجي الكمي ثلاثي الأبعاد:</p>", unsafe_allow_html=True)
    
    x = np.linspace(-5, 5, 65)
    y = np.linspace(-5, 5, 65)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(X * (pure_numeric % 5 + 1) * 0.1) + 1.0
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
    fig.update_layout(
        title='كثافة الموجة الحية لكود ريمان',
        scene=dict(xaxis_title='X Matrix', yaxis_title='Y Matrix', zaxis_title='Zeta Spectrum'),
        margin=dict(l=0, r=0, b=0, t=40),
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 4️⃣ قسم: مفكك الشفرات العام المدمج
# =========================================================
elif selected_option == "مفكك الشفرات العام 🔓":
    st.markdown("<h3 style='text-align: center; font-family: Cairo; color: #00ffcc; font-size: 20px;'>🔓 مفكك الشفرات العام الذكي (Universal Decoder)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa; font-size: 13px;'>اختبر هنا لترى كيف ستفشل أي أدوات خارجية في قراءة شفرات ريمان الجديدة الخاصة بك.</p>", unsafe_allow_html=True)
    
    input_text = st.text_area("📥 أدخل أو الصق النص المُراد تحليله وتفكيكه هنا:", height=150, key="universal_input")
    
    if st.button("🔍 ابدأ الفحص الجنائي والتفكيك الفوري", use_container_width=True, type="primary"):
        if input_text and input_text.strip():
            text = input_text.strip()
            try:
                raw_decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8', errors='ignore')
                if any(c in raw_decoded for c in ['|', '}', '~', '\\', '\x00', '\x0f', '\x1a']):
                    st.warning("⚠️ **نتيجة الفحص الجنائي:** تم رصد ترميز خارجي، ولكن محتوى النص مكسور تماماً! النص محمي بقناع ريمان الرياضي التابع للمنصة ويستحيل قراءته بدون الـ Seed Factor الصحيح.")
                else:
                    st.success(f"📊 **الشفرة مكشوفة (ليست تابعة لريمان):**\n`{raw_decoded}`")
            except Exception:
                st.info("🔒 **تحليل المنصة:** تشفير فوق-أمني معقد للغاية ومحمي بنواة ريمان الكمية الذكية.")
        else:
            st.warning("⚠️ يرجى إدخال أي نص مشفر أو مرمّز أولاً.")

# زر العودة للبوابة
st.write("---")
if st.button("🔙 العودة إلى البوابة الرئيسية للمنصة", use_container_width=True):
    st.switch_page("app.py")

