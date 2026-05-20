import streamlit as st
import hashlib
import time
import numpy as np
import plotly.graph_objects as go
from Crypto.Cipher import AES

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="ZetaWave | Crypto Vault Pro",
    page_icon="🔒",
    layout="centered"
)

# حقن واجهة التشفير والـ CSS المتوافق مع شاشات الموبايل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600&family=Space+Grotesk:wght=500;700&family=Cairo:wght=400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    [data-testid="stToolbar"] {visibility: hidden;}
    
    .hero-container {
        text-align: center;
        padding: 25px 15px;
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.05) 0%, rgba(121, 40, 202, 0.05) 100%);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        margin-bottom: 20px;
    }
    
    .hero-title {
        font-family: 'Space Grotesk', 'Cairo', sans-serif;
        font-size: 26px;
        font-weight: 700;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    .hero-subtitle {
        color: #9ca3af;
        font-size: 13px;
        max-width: 500px;
        margin: 0 auto;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        background-color: rgba(17, 24, 39, 0.6);
        padding: 5px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .stTabs [data-baseweb="tab"] {
        height: 40px;
        font-size: 13px;
        background-color: transparent;
        border-radius: 8px;
        color: #9ca3af;
        font-family: 'Cairo', sans-serif;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.15) 0%, rgba(121, 40, 202, 0.15) 100%) !important;
        color: #00d2ff !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
    }

    .saas-card {
        background: rgba(17, 24, 39, 0.45);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 18px;
        margin-top: 10px;
    }
    
    .analytics-panel {
        background: rgba(10, 15, 28, 0.8);
        border-radius: 14px;
        border: 1px solid rgba(0, 210, 255, 0.2);
        padding: 15px;
        margin-top: 15px;
    }
    
    .panel-title {
        font-family: 'Cairo', sans-serif;
        color: #00d2ff;
        font-size: 15px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 12px;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
    }
    
    @media (max-width: 600px) {
        .grid-container { grid-template-columns: 1fr; }
    }
    
    .grid-box {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    
    .box-lbl { color: #9ca3af; font-size: 11px; font-family: 'Cairo', sans-serif; }
    .box-val { font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700; color: #ffffff; }
    .glow-txt { color: #00d2ff; text-shadow: 0 0 8px rgba(0, 210, 255, 0.5); }

    .stTextArea textarea, .stTextInput input {
        background-color: rgba(10, 11, 18, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #f3f4f6 !important;
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة الـ States الأساسية
if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-3D-INF-9923-881A-QUANTUM"
if 'logs' not in st.session_state:
    st.session_state['logs'] = []
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

# زر العودة السريعة للصفحة الرئيسية
if st.button("⬅️ العودة لبوابة الحساب والاشتراكات الرئيسية", use_container_width=True):
    st.switch_page("app.py")

# عرض ترويسة الصفحة
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🛡️ CRYPTO VAULT PRO</div>
    <div class="hero-subtitle">نظام الحماية الفوق-أمنية القائم على معيار التشفير العسكري AES-256-GCM وطيف ريمان الكمي.</div>
</div>
""", unsafe_allow_html=True)

# عرض حالة الحساب العلوية
if st.session_state.get('is_pro', False):
    st.markdown("<div style='background: linear-gradient(90deg, rgba(0,210,255,0.1), rgba(121,40,202,0.1)); border: 1px dashed #00d2ff; padding: 10px; border-radius: 12px; text-align: center; margin-bottom: 15px;'><span style='color: #00d2ff; font-weight: bold; font-family: Cairo; font-size:13px;'>👑 نوع باقتك الحالية: باقة المطور المالك (كل الميزات مفتوحة)</span></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='background: rgba(255,30,30,0.1); border: 1px solid #ff3333; padding: 10px; border-radius: 12px; text-align: center; margin-bottom: 15px;'><span style='color: #ff3333; font-weight: bold; font-family: Cairo; font-size:13px;'>👤 أنت تستخدم الحساب المجاني المحدود (يرجى الترقية من الصفحة الرئيسية)</span></div>", unsafe_allow_html=True)

st.caption(f"🔒 بصمة مفتاح ريمان الثابت: `{st.session_state['master_key']}`")

# 🛠️ إضافة التبويب الجديد "🌌 النطاق الكمي والمعاملات" إلى القائمة
tab1, tab2, tab5, tab3, tab4 = st.tabs(["🔒 التشفير الآمن", "🔓 فك التشفير", "🌌 النطاق الكمي والمعاملات", "📜 السجل الحي", "🎛️ المحلل الذكي"])

# دالات التشفير الأساسية
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


# --- 🌌 تبويب النطاق الكمي والمعاملات والمخططات البيانية الجديد ---
with tab5:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🌌 نظام التعديل الرياضي والمحاكاة ثلاثية الأبعاد")
    
    # 1. تفعيل وضع اللانهاية الكمي
    q_infinity = st.toggle("♾️ تفعيل وضع النطاق اللامتناهي (Quantum Infinity Mode)", value=True, key="quantum_inf_tg")
    
    if q_infinity:
        st.markdown("""
        <div style="background: rgba(0,210,255,0.07); border: 1px solid rgba(0,210,255,0.3); padding: 12px; border-radius: 10px; margin-bottom: 15px;">
            <span style="color: #00d2ff; font-weight: bold; font-family: Cairo; font-size: 13px;">⚡ وضع اللانهاية نشط: يتم حساب طيف التداخل كدالة تكاملية متصلة تمثل كافة الأصفار.</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. المعامل الحركي الأول: حجم الأصفار بالتريليون
        zero_size = st.slider("🎚️ حدد حجم الأصفار (بالتريليون):", min_value=10, max_value=1000, value=810, step=10)
    else:
        zero_size = 100
        
    # 3. المعامل الحركي الثاني: عامل التغيير الديناميكي (Seed Factor) بدون قيود تجميد القيمة
    seed_factor = st.number_input("🔑 عامل التغيير الديناميكي (Seed Factor):", min_value=1, max_value=999999999999999, value=77777, step=1)
    
    st.write("---")
    st.write("### 📊 محاكاة التداخل الموجي ثلاثي الأبعاد لطيف ريمان الكمي")
    
    # بناء الرسم البياني الرياضي ثلاثي الأبعاد تفاعلياً بناءً على المعاملات المحددة
    with st.spinner("⏳ جاري توليد البنية الرياضية للموجة الكوانتية..."):
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        
        # دالة رياضية موجية تتأثر بالـ Seed Factor وحجم الأصفار ديناميكياً
        Z = np.sin(np.sqrt(X**2 + Y**2) + (seed_factor % 100)) * np.cos(X / (zero_size / 200)) + 1
        
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
        fig.update_layout(
            title='كثافة الموجة الحركية المشفرة للأبعاد',
            autosize=True,
            margin=dict(l=0, r=0, b=0, t=40),
            scene=dict(
                xaxis_title='البعد X',
                yaxis_title='البعد Y',
                zaxis_title='كثافة الموجة'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#f3f4f6')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


# --- تبويب التشفير ---
with tab1:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🚀 تشفير المخرجات")
    mode = st.pills("اختر الهدف المُراد حمايته:", ["نص سري للغاية", "ملف رقمي حقيقي (Pro)"], selection_mode="single", default="نص سري للغاية", key="pills_vault_mode")
    
    if mode == "نص سري للغاية":
        user_text = st.text_area("أدخل أو الصق المحتوى النصي هنا:", height=90, key="txt_enc_vault")
        if st.button("✨ تشفير وتوليد الرمز الهاشي", use_container_width=True, key="btn_enc_txt_vault"):
            if user_text:
                t_start = time.time()
                enc_bytes = aes_encrypt(user_text.encode('utf-8'), st.session_state['master_key'])
                t_end = time.time()
                st.info("🔒 الرمز المشفر النهائي (HEX):")
                st.code(enc_bytes.hex().upper(), language="text")
                st.session_state['logs'].append(f"⏱️ {time.strftime('%H:%M:%S')} - تم تشفير نص سري بنجاح.")
                
                st.markdown(f"""
                <div class="analytics-panel">
                    <div class="panel-title">لوحة التحليل السيبراني الفوري</div>
                    <div class="grid-container">
                        <div class="grid-box"><div class="box-lbl">معيار الحصانة</div><div class="box-val glow-txt">Quantum-Safe</div></div>
                        <div class="grid-box"><div class="box-lbl">سرعة التشفير</div><div class="box-val">{(t_end - t_start)*1000:.2f} ms</div></div>
                        <div class="grid-box"><div class="box-lbl">طول المفتاح</div><div class="box-val">256-Bit</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else: st.error("⚠️ الرجاء كتابة نص أولاً.")
                
    else:
        if not st.session_state.get('is_pro', False):
            st.warning("🔒 ميزة تشفير الملفات مخصصة لمشتركي الباقة الاحترافية (Pro) فقط.")
        else:
            uploaded_file = st.file_uploader("قم برفع الملف هنا:", key="file_vault_uploader")
            if st.button("⚡ بدء التشفير العسكري للملف", use_container_width=True, key="btn_run_file_vault"):
                if uploaded_file is not None:
                    t_start = time.time()
                    f_bytes = uploaded_file.read()
                    enc_f_bytes = aes_encrypt(f_bytes, st.session_state['master_key'])
                    t_end = time.time()
                    st.session_state['file_output'] = enc_f_bytes
                    st.session_state['file_name_out'] = uploaded_file.name + ".zeta"
                    st.success("✅ تم تشفير وتأمين هيكل الملف بالكامل.")
                    st.session_state['logs'].append(f"📁 {time.strftime('%H:%M:%S')} - تم تشفير ملف: {uploaded_file.name}")
                else: st.error("❌ لم تقم برفع أي ملف بعد.")
                
            if 'file_output' in st.session_state:
                st.download_button(label="📥 تحميل الملف الآمن المشفر (.zeta)", data=st.session_state['file_output'], file_name=st.session_state['file_name_out'], mime="application/octet-stream", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- تبويب فك التشفير ---
with tab2:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🔓 فك التشفير والاسترجاع")
    dec_mode = st.pills("نوع البيانات المستهدفة:", ["نص مشفر (HEX)", "ملف محمي (.zeta)"], selection_mode="single", default="نص مشفر (HEX)", key="pills_dec_vault_mode")
    
    if dec_mode == "نص مشفر (HEX)":
        hex_input = st.text_area("أدخل رمز الـ HEX المراد كشفه هنا:", key="hex_vault_in")
        if st.button("🔓 تنفيذ عملية الكشف الفوري", use_container_width=True, key="btn_dec_hex_vault"):
            if hex_input:
                try:
                    clean_hex = hex_input.strip().replace(" ", "")
                    dec_bytes = aes_decrypt(bytes.fromhex(clean_hex), st.session_state['master_key'])
                    st.success("🔓 تم استعادة الرسالة بنجاح:")
                    st.info(dec_bytes.decode('utf-8'))
                    st.session_state['logs'].append(f"🔓 {time.strftime('%H:%M:%S')} - تم فك شفرة نص سري.")
                except Exception: st.error("❌ فشل أمني حرج: الرمز أو المفتاح الموجي غير متطابق!")
            else: st.warning("الرجاء إدخال الرمز.")
            
    else:
        uploaded_zeta = st.file_uploader("ارفع الملف المشفر (.zeta):", type=["zeta"], key="zeta_vault_uploader")
        if st.button("🔓 استعادة الملف الأصلي", use_container_width=True, key="btn_dec_file_vault"):
            if uploaded_zeta is not None:
                try:
                    z_bytes = uploaded_zeta.read()
                    dec_file_bytes = aes_decrypt(z_bytes, st.session_state['master_key'])
                    st.session_state['file_dec_out'] = dec_file_bytes
                    st.session_state['file_name_dec_out'] = "RECOVERED_" + uploaded_zeta.name.replace(".zeta", "")
                    st.success("✅ تم التحقق من البصمة واسترجاع الملف كاملاً!")
                except Exception: st.error("❌ فشل فك التشفير العسكري: الملف تالف أو المفتاح خاطئ.")
            else: st.error("الرجاء رفع ملف .zeta أولاً.")
            
        if 'file_dec_out' in st.session_state:
            st.download_button(label="📤 تحميل الملف الأصلي المسترجع فوراً", data=st.session_state['file_dec_out'], file_name=st.session_state['file_name_dec_out'], mime="application/octet-stream", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- تبويب السجل ---
with tab3:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 📜 سجل الرصد الحركي (Audit Logs)")
    if st.session_state['logs']:
        for log in reversed(st.session_state['logs']): st.code(log, language="text")
    else: st.caption("🪐 السجل فارغ حالياً.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- تبويب محلل الشفرات الذكي ---
with tab4:
    if not st.session_state.get('is_pro', False):
        st.warning("🎛️ نظام التحليل الجنائي ومحلل الشفرات الذكي مقفل ومخصص لحسابات (Pro) فقط.")
    else:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        st.write("### 🎛️ نظام التحليل الجنائي للمخرجات")
        analysis_input = st.text_area("أدخل النص المشفر المراد فحصه عشوائياً:", key="analysis_vault_txt")
        
        if st.button("🔍 بدء الفحص والتحليل الجنائي", use_container_width=True, key="btn_run_ana_vault"):
            if analysis_input:
                text_pure = analysis_input.strip()
                length = len(text_pure)
                import math
                from collections import Counter
                
                prob_dict = [float(c) / length for c in Counter(text_pure).values()]
                entropy = - sum(p * math.log(p, 2) for p in prob_dict)
                
                predicted_type = "غير معروف (بيانات مبهمة عشوائية)"
                strength_status = "ضعيف أو متوسط"
                glow_color = "#ff3333"
                
                if length == 32 and all(c in "0123456789ABCDEFabcdef" for c in text_pure):
                    predicted_type = "بصمة رقمية من نوع MD5 Hash"
                    strength_status = "ضعيف"
                elif length == 64 and all(c in "0123456789ABCDEFabcdef" for c in text_pure):
                    predicted_type = "تشفير أحادي الاتجاه SHA-256"
                    strength_status = "آمن جداً (معيار عالمي موثوق)"
                    glow_color = "#00d2ff"
                elif all(c in "0123456789ABCDEFabcdef \n" for c in text_pure) and length > 40:
                    predicted_type = "تشفير كتلي متناظر (AES-GCM / HEX Stream)"
                    strength_status = "حصانة عسكرية (مقاوم للاختراق)"
                    glow_color = "#00d2ff"
                elif (length % 4 == 0) and all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in text_pure):
                    predicted_type = "نص مرمز بصيغة Base64 Encoding"
                    strength_status = "ترميز فقط"
                    glow_color = "#7928ca"
                    
                st.markdown(f"""
                <div class="analytics-panel" style="border-color: {glow_color};">
                    <div class="panel-title" style="color: {glow_color}; text-shadow: 0 0 10px {glow_color};">📊 نتائج الفحص الهيكلي والتحليل</div>
                    <div class="grid-container">
                        <div class="grid-box"><div class="box-lbl">النوع المتوقع (Prediction)</div><div class="box-val" style="font-size:12px;">{predicted_type}</div></div>
                        <div class="grid-box"><div class="box-lbl">معدل العشوائية (Entropy)</div><div class="box-val" style="color:{glow_color}; font-size:18px;">{entropy:.2f} / 8.00</div></div>
                        <div class="grid-box"><div class="box-lbl">تقييم الأمان الأولي</div><div class="box-val" style="font-size:12px;">{strength_status}</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else: st.error("الرجاء إدخال نص أولاً.")
        st.markdown("</div>", unsafe_allow_html=True)

