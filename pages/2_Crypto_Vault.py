import streamlit as st
import hashlib

st.set_page_config(page_title="Crypto Vault", page_icon="🔒", layout="centered")

st.markdown("<h1>📥 خزنة التشفير وحماية البيانات</h1>", unsafe_allow_html=True)
st.write("---")

# استدعاء المفتاح المشترك من الصفحة الأولى، أو وضع مفتاح افتراضي إذا لم يمر بالمختبر أولاً
if 'master_key' not in st.session_state:
    st.session_state['master_key'] = "ZETA-DEFAUL-KEY-GEN-9923-881A"

st.caption(f"🔑 المفتاح الموجي المستخدم حالياً في العمليات: `{st.session_state['master_key']}`")

tab1, tab2 = st.tabs(["🔒 تشفير وحماية", "🔓 فك التشفير"])

# دالة التشفير التنفيذية للمصفوفات والملفات
def xor_block_cipher(data: bytes, key_str: str) -> bytes:
    key_bytes = hashlib.sha256(key_str.encode()).digest()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

with tab1:
    st.subheader("⚙️ قسم التشفير الآمن")
    option = st.selectbox("اختر نوع البيانات المراد حمايتها:", ["نص سري", "ملف حقيقي (PDF, صور, مستندات)"])
    
    if option == "نص سري":
        user_text = st.text_area("اكتب أو الصق النص السري هنا:")
        if st.button("تشفير النص"):
            if user_text:
                encrypted_bytes = xor_block_cipher(user_text.encode('utf-8'), st.session_state['master_key'])
                st.code(encrypted_bytes.hex().upper(), language="text")
                st.success("🔒 انسخ الرمز المشفر أعلاه بأمان.")
            else: st.warning("الرجاء كتابة نص.")
            
    else:
        uploaded_file = st.file_uploader("اختر ملفاً من جهازك لتشفييره بالكامل:")
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            if st.button("تشفير وتجهيز تحميل الملف"):
                encrypted_file = xor_block_cipher(file_bytes, st.session_state['master_key'])
                st.download_button(
                    label="📥 تحميل الملف المشفر الآمن (.zeta)",
                    data=encrypted_file,
                    file_name=uploaded_file.name + ".zeta",
                    mime="application/octet-stream"
                )

with tab2:
    st.subheader("⚙️ قسم فك التشفير واسترجاع البيانات")
    option_dec = st.selectbox("اختر نوع البيانات المراد فك شفرتها:", ["نص سري مشفر (HEX)", "ملف مشفر (.zeta)"])
    
    if option_dec == "نص سري مشفر (HEX)":
        hex_input = st.text_area("أدخل رمز الـ HEX المشفر هنا:")
        if st.button("فك شفرة النص"):
            if hex_input:
                try:
                    decrypted_bytes = xor_block_cipher(bytes.fromhex(hex_input), st.session_state['master_key'])
                    st.success(f"🔓 النص المسترجع بنجاح: {decrypted_bytes.decode('utf-8', errors='ignore')}")
                except Exception: st.error("فشل التشفير: تأكد من صحة الرمز ومن تطابق المفتاح الموجي.")
            else: st.warning("الرجاء إدخال الرمز أولاً.")
            
    else:
        uploaded_zeta = st.file_uploader("ارفع الملف المشفر بصيغة (.zeta):")
        if uploaded_zeta is not None:
            zeta_bytes = uploaded_zeta.read()
            if st.button("فك تشفير الملف الأصلي"):
                original_bytes = xor_block_cipher(zeta_bytes, st.session_state['master_key'])
                original_name = uploaded_zeta.name.replace(".zeta", "")
                st.download_button(
                    label="📤 تحميل الملف الأصلي المسترجع",
                    data=original_bytes,
                    file_name="RECOVERED_" + original_name,
                    mime="application/octet-stream"
                )
