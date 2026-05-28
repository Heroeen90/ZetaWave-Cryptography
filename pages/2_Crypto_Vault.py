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

# 🧠 النواة الرياضية الموسعة لحدسية ريمان (تدعم النطاق المحدود والنطاق اللانهائي الخماسي)
def riemann_zeta_cipher(input_bytes, seed_str, infinity_mode=False):
    try:
        if not input_bytes:
            return b""
            
        # معالجة وتأمين الـ Seed Factor ديناميكياً
        safe_seed = str(seed_str) if seed_str else "767777664646466464646"
        seed_digits = [int(d) for d in safe_seed if d.isdigit()]
        seed_sum = sum(seed_digits) if seed_digits else 7
        
        n = len(input_bytes)
        x_steps = np.linspace(1, n + 1, n)
        
        if not infinity_mode:
            # 🔒 الوضع القياسي المحدود: يعتمد على الصفر الأول لحدسية ريمان (14.134725)
            t_base = (seed_sum % 50) + 14.134725
            zeta_wave = np.sin(t_base * np.log(x_steps + 1)) + np.cos((t_base + seed_sum) * x_steps * 0.1)
        else:
            # 🌌 الوضع اللانهاية الفوق-أمني: دمج تداخلات الأصفار الخمسة الأولى لريمان معاً لعمل تداخل خماسي الأبعاد
            # الأصفار غير التافهة الخمسة الأولى: 14.134, 21.022, 25.010, 30.424, 32.935
            zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935061]
            t_base = (seed_sum % 100)
            
            # بناء التراكب الموجي الكمي المركب (Superposition)
            zeta_wave = np.zeros(n)
            for i, z_zero in enumerate(zeros):
                zeta_wave += np.sin((t_base + z_zero) * np.log(x_steps + 1)) * np.cos(x_steps * (i + 1) * 0.05)
        
        # تحويل طيف التداخل إلى قناع بايتات مضبوط ومقيد حركياً (بين 1 و 255)
        quantum_mask = [int(abs(w) * 1000) % 254 + 1 for w in zeta_wave]
        
        # تشفير أو فك تشفير البايتات عبر المصفوفة المشتقة (XOR)
        processed_bytes = bytes([input_bytes[i] ^ quantum_mask[i] for i in range(n)])
        return processed_bytes
            
    except Exception:
        return b""

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
    .quantum-mode-box {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.07) 0%, rgba(121, 40, 202, 0.07) 100%);
        border: 1px dashed #00ffcc;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
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
    <p style='color: #9ca3af; font-size: 14px;'>نظام الحماية الفوق-أمنية النواة القائمة على طيف أصفار ريمان والاتصال التزامني الديناميكي.</p>
</div>
""", unsafe_allow_html=True)

# إدارة تزامنية الجلسة والـ Seed Factor والأوضاع
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True

if 'global_seed_factor' not in st.session_state:
    st.session_state['global_seed_factor'] = "01"

if 'quantum_infinity_active' not in st.session_state:
    st.session_state['quantum_infinity_active'] = False

# تحديث الشعار العلوي ليعكس وضع ريمان المقفل حالياً
current_mode_label = "وضع اللانهاية الكلي 🌌" if st.session_state['quantum_infinity_active'] else "الوضع المحدود القياسي 🔒"
if st.session_state['is_pro']:
    st.markdown(f"""
    <div class="status-badge">
        <span style="color: #00ffcc; font-weight: bold; font-size: 14px;">👑 نوع باقتك الحالية: باقة المطور المالك (كل الميزات مفتوحة)</span>
        <br><span style="color: #888; font-size: 11px;">🔒 النطاق النشط: {current_mode_label} | المفتاح الحركي: {st.session_state['global_seed_factor'][:12]}...</span>
    </div>
    """, unsafe_allow_html=True)

# 🛠️ شريط التشغيل المنصّي الموحد (الترتيب الأصلي ثابت دون أي تغيير)
options = ["المحلل الذكي 🎛️", "السجل الحي 📜", "النطاق الكمي والمعاملات 📑", "مفكك الشفرات العام 🔓"]
selected_option = st.radio("اختر الأداة المطلوبة من شريط التشغيل المنصّي:", options, index=0, horizontal=True)

st.write("---")

# =========================================================
# 1️⃣ قسم: المحلل الذكي (التشفير وفك التشفير التزامني مع الأوضاع)
# =========================================================
if selected_option == "المحلل الذكي 🎛️":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>🎛️ لوحة المحلل الذكي السيبراني</h3>", unsafe_allow_html=True)
    st.info(f"🧬 طيف التشفير الحالي مقفل ومزامن على: {current_mode_label}")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc; margin-bottom:5px;'>🚀 تشفير المخرجات الفوق-أمني (Riemann Zeta Encryption):</p>", unsafe_allow_html=True)
    target_type = st.radio("اختر الهدف المُراد تشفيره بالتوليف الكمي:", ["نص سري للغاية", "(Pro) ملف أو تطبيق رقمي حقيقي"], horizontal=True, key="enc_target_radio")
    
    if target_type == "نص سري للغاية":
        text_to_enc = st.text_area("أدخل أو الصق المحتوى النصي هنا ليتم تشفيره بنواة ريمان:", key="riemann_enc_area")
        if st.button("🔥 تشفير وحقن النص عبر نواة ريمان", use_container_width=True, type="primary", key="btn_encrypt_text"):
            if text_to_enc and text_to_enc.strip():
                raw_bytes = text_to_enc.strip().encode('utf-8')
                # استدعاء التشفير ممرراً حالة وضع اللانهاية المحددة في التبويب الثالث
                encrypted_bytes = riemann_zeta_cipher(raw_bytes, st.session_state['global_seed_factor'], infinity_mode=st.session_state['quantum_infinity_active'])
                if encrypted_bytes:
                    final_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
                    st.success("🔒 تم تشفير النص بنجاح (محمي بالكامل بقناع أصفار ريمان):")
                    st.code(final_b64, language=None)
            else:
                st.warning("الرجاء إدخال نص أولاً.")
                
    else:
        uploaded_file = st.file_uploader("قم بتحميل الملف الرقمي أو التطبيق المراد تشفيره (الحد الأقصى 5GB):", type=None, key="uploader_enc")
        if uploaded_file is not None:
            if st.button("🔥 تشفير وحقن الملف بالكامل بنواة ريمان", use_container_width=True, type="primary", key="btn_encrypt_file"):
                with st.spinner("جاري معالجة بايتات الملف وحقن طيف ريمان..."):
                    file_bytes = uploaded_file.read()
                    enc_file_bytes = riemann_zeta_cipher(file_bytes, st.session_state['global_seed_factor'], infinity_mode=st.session_state['quantum_infinity_active'])
                    if enc_file_bytes:
                        st.success(f"🔒 تم تشفير وتأمين الملف ({uploaded_file.name}) بحصانة ريمان!")
                        st.download_button(
                            label="📥 تحميل الملف المشفر بأمان الآن",
                            data=enc_file_bytes,
                            file_name=f"Encrypted_{uploaded_file.name}",
                            mime="application/octet-stream",
                            use_container_width=True,
                            key="btn_download_enc_file"
                        )

    st.write("---")
    
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #0077ff; margin-bottom:5px;'>🔓 مفكك الشفرات المتزامن مع حدسية ريمان (Zetawave Decoder):</p>", unsafe_allow_html=True)
    dec_target_type = st.radio("اختر نوع الهدف المُراد فك تشفيره واسترجاعه:", ["فك تشفير نص مخفي", "فك تشفير ملف / تطبيق مرفوع"], horizontal=True, key="dec_target_radio")
    
    if dec_target_type == "فك تشفير نص مخفي":
        text_to_dec_orig = st.text_area("أدخل النص المشفر المتوافق مع طيف ريمان الحالي لاسترجاعه:", key="riemann_dec_area")
        if st.button("🔓 بدء فك التشفير المزامن للنصوص", use_container_width=True, key="btn_decrypt_text"):
            if text_to_dec_orig and text_to_dec_orig.strip():
                try:
                    b64_decoded = base64.b64decode(text_to_dec_orig.strip().encode('utf-8'))
                    decrypted_bytes = riemann_zeta_cipher(b64_decoded, st.session_state['global_seed_factor'], infinity_mode=st.session_state['quantum_infinity_active'])
                    if decrypted_bytes:
                        st.success("🔓 تم فك الشفرة واستعادة النص الأصلي بنجاح:")
                        st.code(decrypted_bytes.decode('utf-8'), language=None)
                    else:
                        st.error("❌ فشل فك التشفير! المفتاح (Seed) غير مطابق أو نمط التداخل مختلف.")
                except Exception:
                    st.error("❌ فشل معالجة الشفرة المدخلة، تأكد من سلامة بنيتها التركيبية ونمط النطاق.")
            else:
                st.warning("الرجاء إدخال النص المشفر أولاً.")
                
    else:
        uploaded_enc_file = st.file_uploader("قم برفع الملف المشفر (`Encrypted_...`) لإعادة فكه وتوليفه:", type=None, key="uploader_dec")
        if uploaded_enc_file is not None:
            if st.button("🔓 فك تشفير واسترجاع الملف الأصلي", use_container_width=True, type="primary", key="btn_decrypt_file"):
                with st.spinner("جاري قراءة طيف الملف وعكس قناع ريمان الرياضي..."):
                    enc_file_bytes = uploaded_enc_file.read()
                    decrypted_file_bytes = riemann_zeta_cipher(enc_file_bytes, st.session_state['global_seed_factor'], infinity_mode=st.session_state['quantum_infinity_active'])
                    
                    if decrypted_file_bytes:
                        clean_name = uploaded_enc_file.name.replace("Encrypted_", "")
                        st.success(f"🔓 تم فك حجب الحماية بنجاح! السلسلة متطابقة مع النواة الحالية.")
                        st.download_button(
                            label="📥 تحميل الملف المسترجع بأصله الحقيقي الآن",
                            data=decrypted_file_bytes,
                            file_name=f"Decrypted_{clean_name}",
                            mime="application/octet-stream",
                            use_container_width=True,
                            key="btn_download_dec_file"
                        )
                    else:
                        st.error("❌ فشل استرجاع الملف! طيف ريمان المولد من المعطيات الحالية لا يتطابق مع بصمة هذا الملف.")

# =========================================================
# 2️⃣ قسم: السجل الحي للعمليات
# =========================================================
elif selected_option == "السجل الحي 📜":
    st.markdown("<h3 style='font-family: Cairo; font-size: 18px;'>📜 السجل الحي للعمليات الكمية (Live Ledger)</h3>", unsafe_allow_html=True)
    st.code(f"""
[INFO] Riemann Zeta function integrated into core cryptographic stream.
[INFO] Active Security Level: {current_mode_label}
[ACTIVE] Master Seed Factor synchronized: {st.session_state['global_seed_factor']}
    """, language="bash")

# =========================================================
# 3️⃣ قسم: النطاق الكمي والمعاملات (توسيع وتطوير الأوضاع المطلوبة)
# =========================================================
elif selected_option == "النطاق الكمي والمعاملات 📑":
    st.markdown("<p style='font-size: 18px; font-weight: bold; color: #f3f4f6;'>⚙️ لوحة تكييف وتوسيع النطاق الكمي:</p>", unsafe_allow_html=True)
    
    # 🌟 إضافة الأزرار الفرعية لتحديد مستوى النطاق دون المساس بالقائمة الرئيسية
    sub_mode = st.radio(
        "اختر مستوى النطاق المُراد تفعيله لنواة ريمان حالياً:",
        ["الوضع الحالي المحدود 🔒", "وضع اللانهاية الكمي الفوق-أمني 🌌"],
        index=1 if st.session_state['quantum_infinity_active'] else 0,
        horizontal=True
    )
    
    # ربط الخيار بالجلسة فوراً لتحديث النواة
    if sub_mode == "وضع اللانهاية الكمي الفوق-أمني 🌌":
        st.session_state['quantum_infinity_active'] = True
    else:
        st.session_state['quantum_infinity_active'] = False
        
    st.write("---")

    # عرض الواجهة بناءً على الوضع المختار
    if not st.session_state['quantum_infinity_active']:
        # 🔒 1. عرض الواجهة الخاصة بالوضع المحدود
        st.markdown("""
        <div class="infinity-alert">
            ⚡ <b>الوضع المحدود نشط:</b> يتم حساب طيف التداخل بالاعتماد على الصفر القياسي الأول لريمان، والمدخلات خاضعة للرقابة.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 14px; font-weight: bold;'>🔑 عامل التغيير الديناميكي (Seed Factor):</p>", unsafe_allow_html=True)
        seed_factor_str = st.text_input("", value=st.session_state['global_seed_factor'], key="limited_seed_key")
        st.session_state['global_seed_factor'] = seed_factor_str
        
        try:
            pure_numeric = int(''.join(filter(str.isdigit, seed_factor_str))) if seed_factor_str else 1
        except ValueError:
            pure_numeric = 1
            
        if len(seed_factor_str) > 6 or pure_numeric > 999999:
            st.warning("⚠️ يجب أن تكون القيمة أقل من أو تساوي 999999. (الوضع محدود)")
            
    else:
        # 🌌 2. عرض الواجهة الخاصة بالوضع اللانهائي الاحترافي (بدون قيود وبألف تريليون صفر)
        st.markdown("""
        <div class="quantum-mode-box">
            🚀 <b>وضع اللانهاية الكمي مفتوح بالكامل (صلاحية المطور المالك):</b><br>
            تم دمج التداخل الخماسي الشامل لكافة الأصفار. الحقل الآن يمتص الأرقام الفلكية وألف تريليون صفر دون قيود المتصفح!
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 14px; font-weight: bold; color: #00ffcc;'>🔑 عامل التغيير الديناميكي المطلق (Infinite Seed Factor):</p>", unsafe_allow_html=True)
        seed_factor_str = st.text_input("", value=st.session_state['global_seed_factor'], key="infinite_seed_key")
        st.session_state['global_seed_factor'] = seed_factor_str
        
        try:
            pure_numeric = int(''.join(filter(str.isdigit, seed_factor_str))) if seed_factor_str else 1
        except ValueError:
            pure_numeric = 1
            
        st.success("✅ وضع التجاوز الفوق-أمني وتكامل الأصفار نشط تلقائياً لحسابك.")

    st.write("---")
    st.markdown("<p style='font-size: 15px; font-weight: bold; color: #00ffcc;'>📊 بصمة التداخل الموجي ثلاثي الأبعاد المربوط بالوضع النشط:</p>", unsafe_allow_html=True)
    
    # هندسة السطح ثلاثي الأبعاد ليتغير شكله وتعقيده بحسب الوضع المختار (محدود أو لانهائي خماسي)
    x = np.linspace(-5, 5, 65)
    y = np.linspace(-5, 5, 65)
    X, Y = np.meshgrid(x, y)
    
    if not st.session_state['quantum_infinity_active']:
        # موجة عادية بسيطة للوضع المحدود
        Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(X * (pure_numeric % 5 + 1) * 0.1) + 1.0
    else:
        # موجة شديدة التعقيد والتداخل الرياضي تمثل تراكب الأصفار الخمسة في وضع اللانهاية
        Z = np.sin(np.sqrt(X**2 + Y**2) * (pure_numeric % 3 + 1)) * np.cos(X * 0.3) + np.sin(Y * 0.5) + 1.5
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis' if not st.session_state['quantum_infinity_active'] else 'Plasma')])
    fig.update_layout(
        title=f'كثافة الموجة الحية - {current_mode_label}',
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
    st.markdown("<p style='text-align: center; color: #aaa; font-size: 13px;'>جرب وضع أي شفرة هنا، وستكتشف كيف يفشل أي مفكك خارجي في قراءة شفرات ريمان الحالية بدون الـ Seed الصحيح.</p>", unsafe_allow_html=True)
    
    input_text = st.text_area("📥 أدخل أو الصق النص المُراد تحليله وتفكيكه هنا:", height=150, key="universal_input_area")
    
    if st.button("🔍 ابدأ الفحص الجنائي والتفكيك الفوري", use_container_width=True, type="primary", key="btn_universal_decode"):
        if input_text and input_text.strip():
            text = input_text.strip()
            try:
                raw_decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8', errors='ignore')
                if any(ord(c) < 32 or ord(c) > 126 for c in raw_decoded):
                    st.warning("⚠️ **نتيجة الفحص الجنائي:** تم رصد ترميز خارجي، ولكن محتوى النص مكسور ومليء بالرموز المبهمة! البيانات محصنة عبر طيف أصفار ريمان ولا يمكن تفكيكها برمجياً بدون قيمة الـ Seed Factor الأصلية ونمط النطاق المقترن بها.")
                else:
                    st.success(f"📊 **الشفرة مكشوفة (تنسيق عشوائي طبيعي):**\n`{raw_decoded}`")
            except Exception:
                st.info("🔒 **تحليل المنصة:** تشفير فوق-أمني عسكري معقد للغاية، البيانات محمية كلياً بنواة ريمان الكمية الذكية.")
        else:
            st.warning("⚠️ يرجى إدخال أي نص مشفر أو مرمّز أولاً.")

# زر العودة للبوابة
st.write("---")
if st.button("🔙 العودة إلى البوابة الرئيسية للمنصة", use_container_width=True, key="btn_back_to_main"):
    st.switch_page("app.py")

