import streamlit as st
import hashlib

st.set_page_config(page_title="Crypto Vault", page_icon="🔒", layout="centered")

st.markdown("<h1>📥 خزنة التشفير وحماية البيانات</h1>", unsafe_allow_html=True)
st.write("---")

# استدعاء المفتاح المشترك أو وضع مفتاح افتراضي
if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-DEFAUL-KEY-GEN-9923-881A"

st.caption(f"🔑 المفتاح الموجي المستخدم حالياً في العمليات: `{st.session_state['master_key']}`")

tab1, tab2 = st.tabs(["🔒 تشفير وحماية", "🔓 فك التشفير"])

# دالة التشفير التنفيذية
def xor_block_cipher(data: bytes, key_str: str) -> bytes:
    key_bytes = hashlib.sha256(key_str.encode()).digest()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

with tab1:
    st.subheader("⚙️ قسم التشفير الآمن")
    option = st.selectbox("اختر نوع البيانات المراد حمايتها:", ["نص سري", "ملف حقيقي (PDF, صور, مستندات)"])
    
    if option == "نص سري":
        user_text = st.text_area("اكتب أو الصق النص السري هنا:", key="enc_text_area")
        if st.button("تشفير النص الآن", key="btn_enc_text"):
            if user_text:
                encrypted_bytes = xor_block_cipher(user_text.encode('utf-8'), st.session_state['master_key'])
                st.markdown("<div class='success-box'><b>🔒 النص المشفر بنجاح:</b></div>", unsafe_allow_html=True)
                st.code(encrypted_bytes.hex().upper(), language="text")
            else:
                st.warning("⚠️ الرجاء كتابة نص أولاً لتشفيره.")
            
    else:
        uploaded_file = st.file_uploader("اختر ملفاً من جهازك لتشفييره بالكامل:", key="file_enc_uploader")
        
        # الزر أصبح ظاهراً دائماً هنا خارج الشرط لحل مشكلة الموبايل
        if st.button("تشفير وتجهيز تحميل الملف الآن", key="btn_enc_file"):
            if uploaded_file is not None:
                file_bytes = uploaded_file.read()
                encrypted_file = xor_block_cipher(file_bytes, st.session_state['master_key'])
                st.session_state['encrypted_output'] = encrypted_file
                st.session_state['file_name_out'] = uploaded_file.name + ".zeta"
                st.success("✅ تم تشفير الملف بنجاح! اضغط على زر التحميل في الأسفل لحفظه.")
            else:
                st.error("❌ خطأ: الرجاء اختيار ورفع ملف من زر Upload أولاً قبل الضغط على التشفير.")
        
        # إظهار زر التحميل الأخضر إذا تمت العملية بنجاح
        if 'encrypted_output' in st.session_state:
            st.download_button(
                label="📥 تحميل الملف المشفر الآمن (.zeta)",
                data=st.session_state['encrypted_output'],
                file_name=st.session_state['file_name_out'],
                mime="application/octet-stream"
            )

with tab2:
    st.subheader("⚙️ قسم فك التشفير واسترجاع البيانات")
    option_dec = st.selectbox("اختر نوع البيانات المراد فك شفرتها:", ["نص سري مشفر (HEX)", "ملف مشفر (.zeta)"])
    
    if option_dec == "نص سري مشفر (HEX)":
        hex_input = st.text_area("أدخل رمز الـ HEX المشفر هنا:", key="dec_text_area")
        if st.button("فك شفرة النص الآن", key="btn_dec_text"):
            if hex_input:
                try:
                    # تنظيف النص من الفراغات
                    clean_hex = hex_input.strip().replace(" ", "")
                    decrypted_bytes = xor_block_cipher(bytes.fromhex(clean_hex), st.session_state['master_key'])
                    st.success(f"🔓 النص المسترجع بنجاح: {decrypted_bytes.decode('utf-8', errors='ignore')}")
                except Exception:
                    st.error("❌ فشل فك التشفير: تأكد من أن الرمز صحيح ومن تطابق المفتاح الموجي.")
            else:
                st.warning("⚠️ الرجاء إدخال رمز الـ HEX أولاً.")
            
    else:
        uploaded_zeta = st.file_uploader("ارفع الملف المشفر بصيغة (.zeta):", key="file_dec_uploader")
        
        # الزر ظاهر دائماً
        if st.button("فك تشفير الملف الأصلي الآن", key="btn_dec_file"):
            if uploaded_zeta is not None:
                zeta_bytes = uploaded_zeta.read()
                original_bytes = xor_block_cipher(zeta_bytes, st.session_state['master_key'])
                st.session_state['decrypted_output'] = original_bytes
                st.session_state['file_name_dec_out'] = "RECOVERED_" + uploaded_zeta.name.replace(".zeta", "")
                st.success("✅ تم فك تشفير الملف بنجاح! اضغط على زر التحميل في الأسفل للحصول عليه.")
            else:
                st.error("❌ خطأ: الرجاء رفع ملف الـ .zeta أولاً قبل الضغط على زر فك التشفير.")
        
        # إظهار زر تحميل الملف المسترجع
        if 'decrypted_output' in st.session_state:
            st.download_button(
                label="📤 تحميل الملف الأصلي المسترجع",
                data=st.session_state['decrypted_output'],
                file_name=st.session_state['file_name_dec_out'],
                mime="application/octet-stream"
            )
