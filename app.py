import streamlit as st

st.title("🌤️ Weather Advisor Expert System")
st.write("مرحباً بكِ في نظام النصائح الجوية الذكي.")

st.divider()

temperature = st.number_input("أدخل درجة الحرارة الحالية (مئوية):", value=25.0)
condition = st.selectbox("حالة الجو العامة:", ["مشمس", "ممطر", "غائم", "عاصف"])

if st.button("الحصول على الاستشارة الذكية"):
    if temperature > 35 and condition == "مشمس":
        st.error("⚠️ تحذير: الجو حار جداً ومشمس! يُنصح بارتداء نظارات شمسية وعدم التعرض المباشر لأشعة الشمس.")
    elif condition == "ممطر":
        st.info("☔ الجو ممطر، لا تنسَ إحضار مظلتك وارتداء ملابس دافئة.")
    elif temperature < 15:
        st.info("🧥 الطقس بارد جداً، يُفضل ارتداء معطف ثقيل.")
    else:
        st.success("✅ الطقس معتدل ومناسب جداً للأنشطة اليومية!")