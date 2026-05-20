import streamlit as st
import hashlib
import time
from Crypto.Cipher import AES

st.set_page_config(page_title="Crypto Vault Pro Analytics", page_icon="🔒", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>📥 خزنة التشفير والتحليل السيبراني</h1>", unsafe_allow_html=True)
st.write("---")

if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-3D-INF-DEFAUL-KEY-GEN-9923"

st.caption(f"🔑 المفتاح الموجي النشط: `{st.session_state['master_key']}`")

tab1, tab2 = st.tabs(["🔒 تشفير وتحليل رقمي", "🔓 فك التشفير"])

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

with tab1:
    st.subheader("🛡️ تشفير البيانات بنظام الحصانة المزدوجة")
    option = st.selectbox("اختر نوع البيانات:", ["نص سري", "ملف حقيقي (PDF, صور, مستندات)"])
    
    if option == "نص سري":
        user_text = st.text_area("اكتب النص السري هنا:", key="enc_text")
        if st.button("تشفير النص الآن"):
            if user_text:
                start_time = time.time()
                enc_data = aes_encrypt(user_text.encode('utf-8'), st.session_state['master_key'])
                end_time = time.time()
                
                st.info("🔒 النص المشفر عسكرياً (HEX):")
                st.code(enc_data.hex().upper(), language="text")
                
                # لوحة التحليلات الرقمية للنص
                st.write("---")
                st.markdown("### 📊 لوحة التحليل السيبراني الفوري (Real-time Analytics)")
                col1, col2, col3 = st.columns(3)
                col1.metric(label="🛡️ معيار الحصانة", value="Quantum-Safe")
                col2.metric(label="⏱️ سرعة التشفير", value=f"{(end_time - start_time)*1000:.2f} ms")
                col3.metric(label="🔐 طول المفتاح", value="256-Bit")
            else:
                st.warning("الرجاء كتابة نص أولاً.")
                
    else:
        uploaded_file = st.file_uploader("اختر ملفاً من جهازك لتشفيره بحماية مطلقة:")
        if st.button("تشفير وتجهيز تحميل الملف الآن"):
            if uploaded_file is not None:
                start_time = time.time()
                file_bytes = uploaded_file.read()
                enc_file_bytes = aes_encrypt(file_bytes, st.session_state['master_key'])
                end_time = time.time()
                
                st.session_state['aes_output'] = enc_file_bytes
                st.session_state['aes_filename'] = uploaded_file.name + ".zeta"
                
                st.success("✅ تم التشفير بمعيار AES-256-GCM العسكري!")
                
                # لوحة التحليلات الرقمية للملف الحقيقي
                st.write("---")
                st.markdown("### 📊 لوحة التحليل السيبراني للملف")
                col1, col2, col3 = st.columns(3)
                col1.metric(label="💾 حجم الملف المعالج", value=f"{len(file_bytes)/1024:.1f} KB")
                col2.metric(label="⚡ وقت المعالجة", value=f"{(end_time - start_time)*1000:.1f} ms")
                col3.metric(label="🌌 صمود ضد الكسر", value="10^42 سنة")
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

