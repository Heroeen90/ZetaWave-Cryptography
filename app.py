import streamlit as st
import time

# إعدادات الصفحة الرئيسية للموقع
st.set_page_config(
    page_title="ZetaWave Quantum Platform",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# حقن ثيم الـ SaaS الاحترافي في الصفحة الرئيسية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Space+Grotesk:wght@500;700&family=Cairo:wght@400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .main-hero {
        text-align: center;
        padding: 60px 20px;
        margin-top: 40px;
    }
    .brand-glow {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 56px;
        font-weight: 700;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 20px;
    }
    .hero-desc {
        color: #9ca3af;
        font-size: 17px;
        max-width: 600px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }
    .pricing-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-top: 30px;
    }
    @media (max-width: 600px) {
        .pricing-grid { grid-template-columns: 1fr; }
    }
    .price-card {
        background: rgba(17, 24, 39, 0.45);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 30px;
        text-align: center;
        position: relative;
    }
    .pro-card {
        border-color: #00d2ff;
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.1);
    }
    .badge {
        position: absolute;
        top: 15px;
        right: 15px;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        color: #fff;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 20px;
        font-weight: bold;
    }
    .price-val {
        font-size: 36px;
        font-weight: bold;
        color: #fff;
        margin: 15px 0;
    }
    .price-val span { font-size: 16px; color: #888; }
    
    [data-testid="stSidebar"] {
        background-color: #05070f !important;
        border-right: 1px solid rgba(255, 255, 255, 0.03);
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة الحساب المشترك في السايدبار الجانبي لجميع الصفحات
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = False

with st.sidebar:
    st.markdown("<h3 style='font-family: Cairo; text-align: center;'>💼 بوابة حسابك الرقمي</h3>", unsafe_allow_html=True)
    st.write("---")
    
    if st.session_state['is_pro']:
        st.markdown("<div style='background: rgba(0, 210, 255, 0.1); border: 1px solid #00d2ff; padding: 15px; border-radius: 12px; text-align: center;'><span style='color: #00d2ff; font-weight: bold; font-family: Cairo;'>👑 الحساب: الباقة الاحترافية (نشط)</span></div>", unsafe_allow_html=True)
        if st.button("تسجيل الخروج من الباقة", key="main_logout"):
            st.session_state['is_pro'] = False
            st.rerun()
    else:
        st.markdown("<div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px;'><span style='color: #888; font-family: Cairo;'>👤 الحساب الحالي: الباقة المجانية</span></div>", unsafe_allow_html=True)
        
        license_key = st.text_input("أدخل كود تفعيل اشتراكك (License Key):", type="password", key="main_lic_input")
        if st.button("🚀 تفعيل الحساب والترقية", use_container_width=True, key="main_lic_btn"):
            if license_key == "ZETA-PRO-2026":
                st.session_state['is_pro'] = True
                st.toast("تمت الترقية إلى الباقة الاحترافية بنجاح! 🎉")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("❌ كود التفعيل غير صحيح.")

# عرض الـ Hero Section والأسعار
st.markdown("""
<div class="main-hero">
    <div class="brand-glow">ZETAWAVE SUITE</div>
    <div class="hero-desc">المنصة السحابية الأولى عالمياً لتأمين وتشفير البيانات الفوق-أمنية باستخدام خوارزميات ريمان الرياضية المتقدمة وحصانة AES-256 العسكرية.</div>
</div>

<h2 style='text-align: center; font-family: Cairo; margin-bottom: 30px;'>🏷️ خطط الاشتراك السحابية مرنة التكلفة</h2>
<div class="pricing-grid">
    <div class="price-card">
        <h3 style='color: #fff; font-family: Cairo;'>الباقة الأساسية (Free)</h3>
        <div class="price-val">$0 <span>/ شهرياً</span></div>
        <p style='color: #888; font-size: 14px;'>تناسب الأفراد لتجربة التشفير البسيط</p>
        <hr style='border-color: rgba(255,255,255,0.05)'>
        <ul style='text-align: right; color: #bbb; font-size: 13px; font-family: Cairo;'>
            <li>✓ تشفير وفك تشفير النصوص السريّة</li>
            <li>✓ مفتاح موجي افتراضي متغير</li>
            <li>✗ تشفير الملفات الحقيقية مقفل</li>
            <li>✗ محلل الشفرات الذكي مقفل</li>
        </ul>
    </div>
    <div class="price-card pro-card">
        <div class="badge">الأكثر طلباً</div>
        <h3 style='color: #00d2ff; font-family: Cairo;'>الباقة الاحترافية (Pro)</h3>
        <div class="price-val">$29 <span>/ شهرياً</span></div>
        <p style='color: #888; font-size: 14px;'>للشركات ومحترفي الأمن السيبراني</p>
        <hr style='border-color: rgba(0, 210, 255, 0.2)'>
        <ul style='text-align: right; color: #bbb; font-size: 13px; font-family: Cairo;'>
            <li>✓ كل ميزات الباقة المجانية بالكامل</li>
            <li>✓ تشفير مفتوح للملفات بجميع الأحجام</li>
            <li>✓ الوصول الكامل لمحلل الشفرات الذكي الجنائي</li>
            <li>✓ وضع اللانهاية الكمي الفوق-أمن دائم</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

