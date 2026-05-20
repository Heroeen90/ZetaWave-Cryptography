import streamlit as st
import stripe
import time

# إعدادات الصفحة الرئيسية
st.set_page_config(
    page_title="ZetaWave Quantum Platform",
    page_icon="🛡️",
    layout="centered"
)

# 🔑 المفاتيح العلنية ومعرف السعر (مدمجة داخل الكود لأنها آمنة للعلن)
STRIPE_PUBLIC_KEY = "pk_test_51TZEozGVNwmCi5l2MezBS5P14YRe8Dc6uUIx8qW9mlxTrVpkOme9RbhQHnpzDymQ9ZMQZTN8oylDyJDyQoKPijIV00oT2DyBkC"
PRICE_ID = "price_1O23XyYourActualPriceIDHere"  # ⚠️ تأكد من استبدال هذا بمعرف السعر الذي يبدأ بـ price_ من حسابك

# 🔒 استدعاء المفتاح السري بأمان من خزنة Streamlit Secrets الحامية
try:
    STRIPE_SECRET_KEY = st.secrets["STRIPE_SECRET_KEY"]
    stripe.api_key = STRIPE_SECRET_KEY
except KeyError:
    st.warning("⚠️ تحذير سيبراني: لم يتم ضبط المفتاح السري 'STRIPE_SECRET_KEY' في إعدادات المنصة بعد.")

# حقن ثيم الـ SaaS الاحترافي المتوافق تماماً مع الموبايل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600&family=Space+Grotesk:wght=500;700&family=Cairo:wght=400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    [data-testid="stToolbar"] {visibility: hidden;}
    
    .main-hero {
        text-align: center;
        padding: 20px 10px;
        margin-top: 10px;
    }
    .brand-glow {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 42px;
        font-weight: 700;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }
    .hero-desc {
        color: #9ca3af;
        font-size: 15px;
        max-width: 600px;
        margin: 0 auto 25px auto;
        line-height: 1.6;
    }
    
    .price-card {
        background: rgba(17, 24, 39, 0.45);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        position: relative;
        margin-bottom: 15px;
    }
    .pro-card {
        border-color: rgba(0, 210, 255, 0.4);
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.05);
    }
    .badge {
        position: absolute;
        top: 12px;
        right: 12px;
        background: linear-gradient(90deg, #00d2ff, #7928ca);
        color: #fff;
        font-size: 10px;
        padding: 3px 8px;
        border-radius: 20px;
        font-weight: bold;
    }
    .price-val {
        font-size: 30px;
        font-weight: bold;
        color: #fff;
        margin: 8px 0;
    }
    .price-val span { font-size: 14px; color: #888; }
    
    .owner-box {
        background: linear-gradient(90deg, rgba(0,210,255,0.07), rgba(121,40,202,0.07));
        border: 1px dashed rgba(0, 210, 255, 0.3);
        padding: 15px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة تهيئة الجلسة للمالك والمحاكاة
if 'is_pro' not in st.session_state:
    st.session_state['is_pro'] = True 

# التقاط ما إذا كان العميل عائداً بعد الدفع الناجح عبر الروابط (Success URL)
query_params = st.query_params
if "session_id" in query_params:
    st.session_state['is_pro'] = True
    st.balloons()
    st.success("🎉 شكراً لك! تم تأكيد عملية الدفع بنجاح وتفعيل الباقة الاحترافية.")

# عرض لوحة التحكم الفورية بالحساب
st.markdown("<h3 style='font-family: Cairo; text-align: center; font-size: 20px;'>💼 بوابة التحكم بالحساب الرقمي</h3>", unsafe_allow_html=True)

if st.session_state['is_pro']:
    st.markdown("""
    <div class="owner-box">
        <span style="color: #00d2ff; font-weight: bold; font-family: Cairo; font-size: 15px;">👑 وضع المالك النشط: حساب الـ Pro مفتوح بالكامل تلقائياً</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔥 الدخول المباشر إلى لوحة أدوات التشفير والمعاملات 💻", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Crypto_Vault.py")
        
    if st.button("🔄 محاكاة حساب عميل مجاني (لاختبار الدفع الحقيقي)", use_container_width=True):
        st.session_state['is_pro'] = False
        st.rerun()
else:
    st.markdown("""
    <div style="background: rgba(255,150,0,0.07); border: 1px solid rgba(255,150,0,0.3); padding: 15px; border-radius: 16px; text-align: center; margin-bottom: 20px;">
        <span style="color: #ff9600; font-family: Cairo; font-weight: bold; font-size: 14px;">👤 وضع المحاكاة نشط: أنت تتصفح الآن كـ (عميل مجاني محدود)</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚡ إلغاء المحاكاة والعودة لوضع المالك الاحترافي (Pro)", use_container_width=True):
        st.session_state['is_pro'] = True
        st.rerun()

st.write("---")

# عرض الـ Hero Section والأسعار
st.markdown("""
<div class="main-hero">
    <div class="brand-glow">ZETAWAVE SUITE</div>
    <div class="hero-desc">المنصة السحابية الأولى لتأمين وتشفير البيانات الفوق-أمنية باستخدام خوارزميات ريمان الرياضية المتطورة وحصانة AES-256 العسكرية.</div>
</div>
<h2 style='text-align: center; font-family: Cairo; margin-bottom: 20px; font-size: 22px;'>🏷️ خطط الاشتراك السحابية الحالية</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="price-card">
        <h3 style='color: #fff; font-family: Cairo; font-size: 16px;'>الباقة الأساسية (Free)</h3>
        <div class="price-val">$0 <span>/ شهرياً</span></div>
        <p style='color: #888; font-size: 13px; margin-bottom: 10px;'>تناسب الأفراد لتجربة التشفير البسيط</p>
        <hr style='border-color: rgba(255,255,255,0.05); margin-bottom: 10px;'>
        <ul style='text-align: right; color: #bbb; font-size: 12px; font-family: Cairo; direction: rtl; padding-right: 15px; min-height: 110px;'>
            <li>✓ تشفير وفك تشفير النصوص السريّة</li>
            <li>✓ مفتاح موجي افتراضي متغير</li>
            <li>✗ تشفير الملفات الحقيقية مقفل</li>
            <li>✗ محلل الشفرات الذكي مقفل</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎯 أنت على هذه الباقة حالياً" if not st.session_state['is_pro'] else "🔄 تحويل الحساب للمجاني", use_container_width=True, key="btn_free_plan"):
        if st.session_state['is_pro']:
            st.session_state['is_pro'] = False
            st.rerun()

with col2:
    st.markdown("""
    <div class="price-card pro-card">
        <div class="badge">الأكثر طلباً</div>
        <h3 style='color: #00d2ff; font-family: Cairo; font-size: 16px;'>الباقة الاحترافية (Pro)</h3>
        <div class="price-val">$29 <span>/ شهرياً</span></div>
        <p style='color: #888; font-size: 13px; margin-bottom: 10px;'>للشركات ومحترفي الأمن السيبراني</p>
        <hr style='border-color: rgba(0, 210, 255, 0.2); margin-bottom: 10px;'>
        <ul style='text-align: right; color: #bbb; font-size: 12px; font-family: Cairo; direction: rtl; padding-right: 15px; min-height: 110px;'>
            <li>✓ كل ميزات الباقة المجانية بالكامل</li>
            <li>✓ تشفير مفتوح للمللفات بجميع الأحجام</li>
            <li>✓ الوصول الكامل لمحلل الشفرات الجنائي</li>
            <li>✓ وضع اللانهاية الكمي الفوق-أمن</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("💳 اشتراك الآن عبر Stripe الآمن ⚡" if not st.session_state['is_pro'] else "✅ باقة الـ Pro مفعّلة لك بالكامل", use_container_width=True, type="primary", key="btn_pro_plan"):
        if not st.session_state['is_pro']:
            try:
                with st.spinner("🔄 جاري إنشاء جلسة الدفع الآمنة..."):
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=[{
                            'price': PRICE_ID,
                            'quantity': 1,
                        }],
                        mode='subscription',
                        success_url="https://ccu.streamlit.app/?session_id={CHECKOUT_SESSION_ID}",
                        cancel_url="https://ccu.streamlit.app/",
                    )
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_session.url}">', unsafe_allow_html=True)
                    st.write(f"🔗 إذا لم يتم تحويلك تلقائياً، [اضغط هنا للدفع]({checkout_session.url})")
            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء الاتصال ببوابة Stripe: {e}")
        else:
            st.success("🌟 باقتك نشطة بالفعل! يمكنك الذهاب مباشرة لصفحة الأدوات والمعاملات.")

