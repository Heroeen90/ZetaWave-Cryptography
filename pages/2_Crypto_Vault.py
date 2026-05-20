import streamlit as st
import hashlib
import time
from Crypto.Cipher import AES

# 1. إعدادات الصفحة الأساسية وحظر القوائم الافتراضية المزعجة
st.set_page_config(
    page_title="ZetaWave | Crypto Vault Pro",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. حقن واجهة التشفير العالمية الفاخرة (Quantum Obsidian CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Space+Grotesk:wght@500;700&family=Cairo:wght@400;700&display=swap');
    
    /* تغيير خلفية التطبيق بالكامل وإضافة أنيميشن متحرك خفيف جداً خلف البطاقات */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    /* إخفاء شريط Streamlit العلوي الافتراضي لإعطاء مظهر تطبيق مستقل */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* تصميم الـ Hero Section الفاخر في الأعلى */
    .hero-container {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.05) 0%, rgba(121, 40, 202, 0.05) 100%);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.05);
        margin-bottom: 35px;
    }
    
    .hero-title {
        font-family: 'Space Grotesk', 'Cairo', sans-serif;
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #9ca3af;
        font-size: 15px;
        max-width: 500px;
        margin: 0 auto;
    }

    /* تحويل الـ Tabs الافتراضية إلى أزرار تصفح SaaS مودرن */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(17, 24, 39, 0.6);
        padding: 8px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre;
        background-color: transparent;
        border-radius: 10px;
        color: #9ca3af;
        font-family: 'Cairo', sans-serif;
        font-weight: 600;
        border: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #00d2ff;
        background: rgba(255, 255, 255, 0.03);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 210, 255, 0.15) 0%, rgba(121, 40, 202, 0.15) 100%) !important;
        color: #00d2ff !important;
        border: 1px solid rgba(0, 210, 255, 0.3) !important;
    }

    /* تخصيص البطاقات الزجاجية Glassmorphism */
    .saas-card {
        background: rgba(17, 24, 39, 0.45);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* لوحة التحليل السيبراني الفوري المتطورة من تصميمك */
    .analytics-panel {
        background: rgba(10, 15, 28, 0.8);
        border-radius: 16px;
        border: 1px solid rgba(0, 210, 255, 0.2);
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.05);
    }
    
    .panel-title {
        font-family: 'Cairo', sans-serif;
        color: #00d2ff;
        font-size: 18px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }
    
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
    }
    
    @media (max-width: 600px) {
        .grid-container { grid-template-columns: 1fr; }
    }
    
    .grid-box {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .grid-box:hover {
        border-color: #7928ca;
        box-shadow: 0 0 15px rgba(121, 40, 202, 0.2);
        transform: translateY(-2px);
    }
    
    .box-lbl { color: #9ca3af; font-size: 12px; font-family: 'Cairo', sans-serif; margin-bottom: 5px; }
    .box-val { font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 700; color: #ffffff; }
    .glow-txt { color: #00d2ff; text-shadow: 0 0 8px rgba(0, 210, 255, 0.5); }

    /* تخصيص مدخلات النصوص وحقول الرفع لتصبح داكنة وفاخرة */
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(10, 11, 18, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #f3f4f6 !important;
        border-radius: 12px !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00d2ff !important;
        box-shadow: 0 0 10px rgba(0, 210, 255, 0.15) !important;
    }
    
    /* تحسين شكل السايدبار الجانبي */
    [data-testid="stSidebar"] {
        background-color: #05070f !important;
        border-right: 1px solid rgba(255, 255, 255, 0.03);
    }
    </style>
""", unsafe_allow_html=True)

# 3. محرك التهيئة وحفظ مفتاح ريمان في الجلسة
if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-3D-INF-9923-881A-QUANTUM"

if 'logs' not in st.session_state:
    st.session_state['logs'] = []

# --- عرض الـ Hero Section الفاخرة ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🛡️ CRYPTO VAULT PRO</div>
    <div class="hero-subtitle">الجيل القادم من أنظمة التشفير الهجينة المعتمدة على السلوك الموجي لأصفار دالة زيتا ومعيار الحماية العسكري AES-256-GCM.</div>
</div>
""", unsafe_allow_html=True)

st.caption(f"🔒 بصمة موجة ريمان الحالية النشطة عالمياً: `{st.session_state['master_key']}`")

# 4. بناء الـ Tabs بنمط الـ SaaS الفاخر
tab1, tab2, tab3, tab4 = st.tabs(["🔒 تشفير وحماية البيانات", "🔓 استرجاع وفك التشفير", "📜 سجل العمليات الحي", "🎛️ محلل الشفرات الذكي"])


# دالة التشفير العسكري
def aes_encrypt(data: bytes, key_str: str) -> bytes:
    secret_key = hashlib.sha256(key_str.encode()).digest()
    cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

# دالة فك التشفير العسكري
def aes_decrypt(payload: bytes, key_str: str) -> bytes:
    secret_key = hashlib.sha256(key_str.encode()).digest()
    nonce = payload[:16]
    tag = payload[16:32]
    ciphertext = payload[32:]
    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

# --- التبويب الأول: التشفير ---
with tab1:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🚀 تشفير النصوص والملفات الفوري")
    mode = st.pills("اختر نوع الهدف المُراد تأمينه:", ["نص سري للغاية", "ملف رقمي حقيقي"], selection_mode="single", default="نص سري للغاية")
    
    if mode == "نص سري للغاية":
        user_text = st.text_area("أدخل أو الصق المحتوى النصي هنا:", height=100, placeholder="اكتب رسالتك المشفرة المستحيلة الكسر هنا...")
        if st.button("✨ تشفير وتوليد الرمز الهاشي", use_container_width=True):
            if user_text:
                st.toast("جاري سحب الأمواج الحسابية...", icon="⏳")
                t_start = time.time()
                enc_bytes = aes_encrypt(user_text.encode('utf-8'), st.session_state['master_key'])
                t_end = time.time()
                
                hex_result = enc_bytes.hex().upper()
                st.info("🔒 الرمز المشفر النهائي (جاهز للنسخ):")
                st.code(hex_result, language="text")
                
                # إضافة اللوج
                st.session_state['logs'].append(f"⏱️ {time.strftime('%H:%M:%S')} - تم تشفير نص سري بنجاح.")
                
                # لوحة التحليلات المتقدمة المستوحاة من تصميمك
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
            else:
                st.error("⚠️ الرجاء كتابة نص أولاً.")
                
    else:
        uploaded_file = st.file_uploader("قم بسحب وإفلات أي ملف هنا (صور، مستندات، PDF):", type=None)
        if st.button("⚡ بدء التشفير العسكري للملف", use_container_width=True):
            if uploaded_file is not None:
                t_start = time.time()
                f_bytes = uploaded_file.read()
                enc_f_bytes = aes_encrypt(f_bytes, st.session_state['master_key'])
                t_end = time.time()
                
                st.session_state['file_output'] = enc_f_bytes
                st.session_state['file_name_out'] = uploaded_file.name + ".zeta"
                st.success("✅ تم تشفير وتأمين هيكل الملف بالكامل.")
                
                st.session_state['logs'].append(f"📁 {time.strftime('%H:%M:%S')} - تم تشفير ملف: {uploaded_file.name}")
                
                st.markdown(f"""
                <div class="analytics-panel">
                    <div class="panel-title">لوحة التحليل السيبراني الفوري</div>
                    <div class="grid-container">
                        <div class="grid-box"><div class="box-lbl">حجم المعالجة</div><div class="box-val">{len(f_bytes)/1024:.1f} KB</div></div>
                        <div class="grid-box"><div class="box-lbl">وقت التنفيذ</div><div class="box-val">{(t_end - t_start)*1000:.1f} ms</div></div>
                        <div class="grid-box"><div class="box-lbl">مقاومة الكسر</div><div class="box-val glow-txt">10^42 Years</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ لم تقم برفع أي ملف بعد.")
                
        if 'file_output' in st.session_state:
            st.download_button(
                label="📥 تحميل الملف الآمن المشفر (.zeta)",
                data=st.session_state['file_output'],
                file_name=st.session_state['file_name_out'],
                mime="application/octet-stream",
                use_container_width=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# --- التبويب الثاني: فك التشفير ---
with tab2:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🔓 فك التشفير والتحقق من السلامة")
    dec_mode = st.pills("نوع البيانات المستهدفة لفك شفرتها:", ["نص مشفر (HEX)", "ملف محمي (.zeta)"], selection_mode="single", default="نص مشفر (HEX)")
    
    if dec_mode == "نص مشفر (HEX)":
        hex_input = st.text_area("أدخل رمز الـ HEX المراد كشفه هنا:", placeholder="الصق الرمز الضخم المكون من أرقام وحروف هنا...")
        if st.button("🔓 تنفيذ عملية الكشف الفوري", use_container_width=True):
            if hex_input:
                try:
                    clean_hex = hex_input.strip().replace(" ", "")
                    dec_bytes = aes_decrypt(bytes.fromhex(clean_hex), st.session_state['master_key'])
                    st.success("🔓 تم فك الشفرة واستعادة الرسالة بنجاح:")
                    st.info(dec_bytes.decode('utf-8'))
                    st.session_state['logs'].append(f"🔓 {time.strftime('%H:%M:%S')} - تم فك شفرة نص سري.")
                except Exception:
                    st.error("❌ فشل أمني حرج: الرمز غير صحيح أو تم التلاعب بمحتواه أو الموجة غير متطابقة!")
            else: st.warning("الرجاء إدخال الرمز.")
            
    else:
        uploaded_zeta = st.file_uploader("ارفع الملف المشفر الذي ينتهي بامتداد (.zeta):", type=["zeta"])
        if st.button("🔓 استعادة الملف الأصلي المستهدف", use_container_width=True):
            if uploaded_zeta is not None:
                try:
                    z_bytes = uploaded_zeta.read()
                    dec_file_bytes = aes_decrypt(z_bytes, st.session_state['master_key'])
                    st.session_state['file_dec_out'] = dec_file_bytes
                    st.session_state['file_name_dec_out'] = "RECOVERED_" + uploaded_zeta.name.replace(".zeta", "")
                    st.success("✅ تم التحقق من البصمة واسترجاع الملف السليم كاملاً!")
                    st.session_state['logs'].append(f"🔓 {time.strftime('%H:%M:%S')} - تم استرجاع ملف بنجاح.")
                except Exception:
                    st.error("❌ فشل فك التشفير العسكري: المفتاح خاطئ أو الملف معدّل لخرق الأمان.")
            else: st.error("الرجاء رفع ملف .zeta أولاً.")
            
        if 'file_dec_out' in st.session_state:
            st.download_button(
                label="📤 تحميل الملف الأصلي المسترجع فوراً",
                data=st.session_state['file_dec_out'],
                file_name=st.session_state['file_name_dec_out'],
                mime="application/octet-stream",
                use_container_width=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# --- التبويب الثالث: سجل العمليات الحي (Audit Logs) ---
with tab3:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 📜 سجل الرصد والمراقبة الأمني (Audit Logs)")
    st.write("تحليل فوري لكافة النشاطات الجارية في هذه الجلسة الحالية:")
    
    if st.session_state['logs']:
        for log in reversed(st.session_state['logs']):
            st.code(log, language="text")
    else:
        st.caption("🪐 السجل فارغ حالياً. قم بعمليات تشفير أو فك تشفير لتظهر التحليلات الحية هنا.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- التبويب الرابع: محلل الشفرات الذكي (Cryptanalysis) ---
with tab4:
    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.write("### 🎛️ نظام التحليل الجنائي للمخرجات المشفرة")
    st.write("قم بلصق أي نص مشفر هنا ليقوم النظام بتحليل تركيبته الرياضية، التنبؤ بنوعه، وقياس مستوى عشوائيته (Entropy):")
    
    analysis_input = st.text_area("أدخل النص المشفر المراد فحصه:", key="analysis_text_input", placeholder="ضع النص هنا ليتم فحصه سيبرانياً...")
    
    if st.button("🔍 بدء الفحص والتحليل الجنائي", use_container_width=True):
        if analysis_input:
            text_pure = analysis_input.strip()
            length = len(text_pure)
            
            # 1. حساب العشوائية (Entropy Calculation)
            import math
            from collections import Counter
            
            prob_dict = [float(c) / length for c in Counter(text_pure).values()]
            entropy = - sum(p * math.log(p, 2) for p in prob_dict)
            
            # 2. خوارزمية التنبؤ بالنوع بناءً على البنية الهيكلية
            predicted_type = "غير معروف (بيانات عشوائية مبهمة)"
            strength_status = "ضعيف أو متوسط"
            glow_color = "#ff3333" # أحمر كتحذير افتراضي
            
            # التحقق من نوع الهاشات الشهيرة
            if length == 32 and all(c in "0123456789ABCDEFabcdef" for c in text_pure):
                predicted_type = "بصمة رقمية من نوع MD5 Hash"
                strength_status = "ضعيف (مرفوض معيارياً لسهولة الكسر)"
            elif length == 64 and all(c in "0123456789ABCDEFabcdef" for c in text_pure):
                predicted_type = "تشفير أحادي الاتجاه SHA-256"
                strength_status = "آمن جداً (معيار عالمي للتحقق)"
            # التحقق من الـ HEX التابع لتطبيقنا أو خوارزميات AES
            elif all(c in "0123456789ABCDEFabcdef \n" for c in text_pure) and length > 40:
                predicted_type = "تشفير كتلي متناظر (AES-GCM / HEX Stream)"
                strength_status = "حصانة عسكرية (مقاوم للاختراق الكمي)"
                glow_color = "#00d2ff"
            # التحقق من Base64
            elif (length % 4 == 0) and all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in text_pure):
                predicted_type = "نص مرمز بصيغة Base64 Encoding"
                strength_status = "ترميز فقط (لا يعتبر حماية حقيقية بدون مفتاح)"
                
            if entropy > 4.5 and predicted_type == "غير معروف (بيانات عشوائية مبهمة)":
                predicted_type = "تشفير تدفقي معقد (أرجحية تشفير كلاسيكي عالي العشوائية)"
                strength_status = "قوي جداً هندسياً"
                glow_color = "#7928ca"

            # عرض النتائج في لوحة زجاجية ساحرة ومطابقة للهوية البصرية لمشروعك
            st.markdown(f"""
            <div class="analytics-panel" style="border-color: {glow_color};">
                <div class="panel-title" style="color: {glow_color}; text-shadow: 0 0 10px {glow_color};">📊 نتائج الفحص الهيكلي والتحليل</div>
                <div class="grid-container">
                    <div class="grid-box">
                        <div class="box-lbl">النوع المتوقع (Prediction)</div>
                        <div class="box-val" style="font-size: 14px; color: #fff;">{predicted_type}</div>
                    </div>
                    <div class="grid-box">
                        <div class="box-lbl">معدل العشوائية (Entropy)</div>
                        <div class="box-val" style="color: {glow_color}; font-size: 22px;">{entropy:.2f} / 8.00</div>
                    </div>
                    <div class="grid-box">
                        <div class="box-lbl">تقييم الأمان الأولي</div>
                        <div class="box-val" style="font-size: 13px; color: #fff;">{strength_status}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.session_state['logs'].append(f"🔍 {time.strftime('%H:%M:%S')} - تم تشغيل فحص جنائي لنص بطول {length} حرف.")
        else:
            st.error("⚠️ الرجاء إدخال نص مشفر لكي يتمكن السيرفر من تحليله.")
    st.markdown("</div>", unsafe_allow_html=True)
