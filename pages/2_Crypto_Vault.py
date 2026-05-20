import streamlit as st
import hashlib
from Crypto.Cipher import AES

st.set_page_config(page_title="Crypto Vault Pro", page_icon="🔒", layout="centered")

st.markdown("<h1>📥 خزنة التشفير العسكري (AES-256-GCM)</h1>", unsafe_allow_html=True)
st.write("---")

# استدعاء المفتاح المشترك أو وضع مفتاح افتراضي
if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-DEFAUL-KEY-GEN-9923-881A"

st.caption(f"🔑 المفتاح الموجي النشط: `{st.session_state['master_key']}`")

tab1, tab2 = st.tabs(["🔒 تشفير عسكري", "🔓 فك التشفير"])

# دالة التشفير الاحترافية AES-256-GCM
def aes_encrypt(data: bytes, key_str: str) -> bytes:
    # اشتقاق مفتاح 32 بايت (256 بت) باستخدام SHA-256
    secret_key = hashlib.sha256(key_str.encode()).digest()
    cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # ندمج الـ nonce والـ tag مع النص المشفر لنتمكن من فكه لاحقاً
    return cipher.nonce + tag + ciphertext

# دالة فك التشفير الاحترافية AES-256-GCM
def aes_decrypt(payload: bytes, key_str: str) -> bytes:
    secret_key = hashlib.sha256(key_str.encode()).digest()
    # استخراج الـ nonce والـ tag والنص المشفر الأصلي من الـ payload
    nonce = payload[:16]
    tag = payload[16:32]
    ciphertext = payload[32:]
    
    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

with tab1:
    st.subheader("🛡️ تشفير البيانات بنظام الحصانة المزدوجة")
    option = st.selectbox("اختر نوع البيانات:", ["نص سري", "ملف حقيقي (PDF, صور, مستندات)"])
    
    if option == "نص سري":
        user_text = st.text_area("اكتب النص السري هنا:", key="enc_text")
        if st.button("تشفير النص الآن بنظام AES-256"):
            if user_text:
                enc_data = aes_encrypt(user_text.encode('utf-8'), st.session_state['master_key'])
                st.info("🔒 النص المشفر عسكرياً (HEX):")
                st.code(enc_data.hex().upper(), language="text")
            else:
                st.warning("الرجاء كتابة نص أولاً.")
                
    else:
        uploaded_file = st.file_uploader("اختر ملفاً من جهازك لتشفيره بحماية مطلقة:")
        if st.button("تشفير وتجهيز تحميل الملف الآن"):
            if uploaded_file is not None:
                file_bytes = uploaded_file.read()
                enc_file_bytes = aes_encrypt(file_bytes, st.session_state['master_key'])
                st.session_state['aes_output'] = enc_file_bytes
                st.session_state['aes_filename'] = uploaded_file.name + ".zeta"
                st.success("✅ تم التشفير بمعيار AES-256-GCM العسكري! جاهز للتحميل.")
            else:
                st.error("الرجاء رفع ملف أولاً.")
                
        if 'aes_output' in st.session_state:
            st.download_button(
                label="📥 تحميل الملف المحمي عسكرياً (.zeta)",
                data=st.session_state['aes_output'],
                file_name=st.session_state['aes_filename'],
                mime="application/octet-stream"
            )

with tab2:
    st.subheader("🔓 استرجاع وفك التشفير العسكري")
    option_dec = st.selectbox("اختر نوع البيانات المراد فكها:", ["نص سري مشفر (HEX)", "ملف مشفر (.zeta)"])
    
    if option_dec == "نص سري مشفر (HEX)":
        hex_input = st.text_area("أدخل رمز الـ HEX المشفر عسكرياً:")
        if st.button("فك شفرة النص الآن"):
            if hex_input:
                try:
                    clean_hex = hex_input.strip().replace(" ", "")
                    dec_bytes = aes_decrypt(bytes.fromhex(clean_hex), st.session_state['master_key'])
                    st.success(f"🔓 النص الأصلي المسترجع: {dec_bytes.decode('utf-8')}")
                except Exception:
                    st.error("❌ فشل فك التشفير العسكري: تم رصد تلاعب في البيانات أو أن المفتاح الموجي غير متطابق!")
            else:
                st.warning("الرجاء إدخال الرمز أولاً.")
                
    else:
        uploaded_zeta = st.file_uploader("ارفع الملف المشفر عسكرياً (.zeta):")
        if st.button("فك تشفير الملف المستهدف"):
            if uploaded_zeta is not None:
                try:
                    zeta_bytes = uploaded_zeta.read()
                    dec_file_bytes = aes_decrypt(zeta_bytes, st.session_state['master_key'])
                    st.session_state['aes_dec_output'] = dec_file_bytes
                    st.session_state['aes_dec_filename'] = "SECURE_RECOVERED_" + uploaded_zeta.name.replace(".zeta", "")
                    st.success("✅ تم فك التشفير بنجاح والتحقق من سلامة الملف!")
                except Exception:
                    st.error("❌ خطأ حرج: لا يمكن فك الملف. المفتاح خاطئ أو الملف تالف ومعدل!")
            else:
                st.error("الرجاء رفع ملف .zeta أولاً.")
                
        if 'aes_dec_output' in st.session_state:
            st.download_button(
                label="📤 تحميل الملف الأصلي السليم",
                data=st.session_state['aes_dec_output'],
                file_name=st.session_state['aes_dec_filename'],
                mime="application/octet-stream"
            )
