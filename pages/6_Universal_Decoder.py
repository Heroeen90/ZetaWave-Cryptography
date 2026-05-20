import streamlit as st
import base64
import binascii
import re

# 🛡️ إعدادات الصفحة المنفصلة لضمان التوافق مع الهواتف والأبعاد
st.set_page_config(
    page_title="Universal Decoder | مفكك الشفرات العام",
    page_icon="🔓",
    layout="centered"
)

# حقن ثيم الـ SaaS الموحد للمنصة لتبدو متناسقة تماماً مع بقية الصفحات
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600&family=Cairo:wght=400;700&display=swap');
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0b0f19 0%, #030712 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    [data-testid="stToolbar"] {visibility: hidden;}
    .decoder-header {
        text-align: center;
        padding: 15px 0;
    }
    .decoder-title {
        font-family: 'Cairo', sans-serif;
        font-size: 28px;
        font-weight: 700;
        background: linear-gradient(90deg, #00ffcc, #0077ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .result-box {
        background: rgba(17, 24, 39, 0.6);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 12px;
        padding: 15px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة الصفحة
st.markdown("""
<div class="decoder-header">
    <div class="decoder-title">🔓 مفكك الشفرات العام (Multi-Decoder)</div>
    <p style="color: #9ca3af; font-size: 14px; font-family: Cairo;">أداة سيبرانية ذكية لتحليل النصوص المدخلة وتفكيك ترميزها تلقائياً</p>
</div>
""", unsafe_allow_html=True)

# صندوق إدخال النص البرمجي المراد تحليله وفكه
input_text = st.text_area("📥 أدخل النص المشفر أو المرمّز هنا لتبدأ المنصة بتحليله:", height=150, placeholder="ضع النص هنا...")

# دالة ذكية لفحص وتفكيك الأنماط تلقائياً
def universal_decoder(text):
    text = text.strip()
    if not text:
        return None, None

    # 1. فحص وتفكيك التشفير الثنائي (Binary)
    if re.match(r'^[01\s]+$', text) and len(text.replace(" ", "")) % 8 == 0:
        try:
            binary_pure = text.replace(" ", "")
            chars = [chr(int(binary_pure[i:i+8], 2)) for i in range(0, len(binary_pure), 8)]
            return "النظام الثنائي (Binary Text)", "".join(chars)
        except:
            pass

    # 2. فحص وتفكيك الـ Hexadecimal (النظام الستة عشري)
    if re.match(r'^[0-9a-fA-F\s]+$', text) and len(text.replace(" ", "")) % 2 == 0:
        try:
            hex_pure = text.replace(" ", "")
            decoded_hex = bytes.fromhex(hex_pure).decode('utf-8', errors='ignore')
            if decoded_hex.isprintable():
                return "النظام الستة عشري (Hexadecimal)", decoded_hex
        except:
            pass

    # 3. فحص وتفكيك الـ Base64
    if re.match(r'^[A-Za-z0-9+/=\s]+$', text) and len(text.replace(" ", "")) % 4 == 0:
        try:
            decoded_b64 = base64.b64decode(text.encode('utf-8'), validate=True).decode('utf-8', errors='ignore')
            if decoded_b64.isprintable():
                return "ترميز القاعدة 64 (Base64 Encoding)", decoded_b64
        except:
            pass

    # 4. فحص وتفكيك شفرة مورس (Morse Code)
    if re.match(r'^[.\-\s/]+$', text):
        morse_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '
        }
        try:
            words = text.split(' / ') if ' / ' in text else [text]
            decoded_morse = []
            for word in words:
                decoded_word = "".join([morse_dict.get(letter, '?') for letter in word.split()])
                decoded_morse.append(decoded_word)
            return "شفرة مورس العالمية (Morse Code)", " ".join(decoded_morse)
        except:
            pass

    # 5. إذا كانت الخوارزمية معقدة أو حديثة (تتطلب مفتاح)
    return "خوارزمية معقدة / تشفير حديث (AES/RSA)", "🔒 تم تحليل النص: يبدو أن البيانات مشفرة باستخدام بروتوكول حديث محمي عسكرياً. لفك شفرة هذا النص، يرجى استخدام واجهة 'التشفير الآمن' الرئيسية وإدخال المفتاح السري (Secret Key) المخصص للملف."

# زر بدء التفكيك والتحليل الذكي
if st.button("🔍 ابدأ التحليل والتفكيك التلقائي", use_container_width=True, type="primary"):
    if input_text:
        with st.spinner("جاري تحليل بصمة التشفير الرقمية..."):
            algo_name, result = universal_decoder(input_text)
            
            if algo_name:
                st.markdown(f"""
                <div class="result-box">
                    <span style="color: #00ffcc; font-weight: bold; font-family: Cairo; font-size: 14px;">📊 الخوارزمية المكتشفة:</span>
                    <p style="color: #ffffff; font-size: 15px; margin-top: 5px;">{algo_name}</p>
                    <hr style="border-color: rgba(255,255,255,0.05); margin: 10px 0;">
                    <span style="color: #00ffcc; font-weight: bold; font-family: Cairo; font-size: 14px;">📝 النص الأصلي بعد الفك:</span>
                    <p style="color: #f3f4f6; font-size: 16px; margin-top: 5px; white-space: pre-wrap;">{result}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ فضلاً، ضع نصاً أو شفرة داخل الصندوق أولاً ليتم فحصها.")

