import streamlit as st

# إعدادات الصفحة لتكون متجاوبة وبتصميم فاخر
st.set_page_config(
    page_title="سوما | SUMA",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات الهوية والألوان الداكنة المستوحاة من الموقع الأصلي
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .restaurant-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%);
        border-radius: 20px;
        margin-bottom: 25px;
        border: 1px solid #333;
    }
    .logo-img {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #e53e3e;
        margin-bottom: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #e53e3e;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #c53030;
        color: white;
    }
    .food-card {
        background: #1e1e1e;
        padding: 15px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 15px;
        border: 1px solid #2d2d2d;
    }
    .badge {
        background-color: #2d1515;
        color: #ff6b6b;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 5px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# رأس التطبيق مع الشعار الحقيقي المأخوذ من سيرفر النظام
logo_url = "https://media-files.tryordersystem.com/tenant/suma/settings/6a0e148871355.jpg"
st.markdown(
    f"""
    <div class='restaurant-header'>
        <img src='{logo_url}' class='logo-img'>
        <h1 style='color: #ffffff; margin-bottom: 5px; font-size: 24px;'>سوما | SUMA</h1>
        <p style='color: #a0aec0; font-size: 14px; margin: 0;'>طعم البرجر الأصلي في بريدة 🔥</p>
    </div>
""",
    unsafe_allow_html=True,
)

# شريط معلومات سريعة
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("⭐ **4.7** (158 تقييم)")
with col2:
    st.markdown("💵 **20–40 SAR**")
with col3:
    st.markdown("🟢 **متاح للطلب**")

st.markdown("---")

# القائمة الرسمية مع تصحيح صورة دبل سماش برجر لتكون الصورة الأخيرة التي أرسلتها، وإدراج جميع الصور التي أرسلتها
menu_items = [
    {
        "name": "أوكلاهوما برجر",
        "price": 28.00,
        "calories": "1090 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس المشوية مع شرائح البصل وشريحتين من جبنة تشيدر الأمريكية.",
        "img": "https://resizer.deliverect.com/nUhMkGHSDtAt4yfmX7g5CPIkFDmYmbXvb0N1Cv6AaCw/rt:fill/g:ce/el:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2lrb25hLWJ1Y2tldC1wcm9kdWN0aW9uL2ltYWdlcy82ODVjZTFlZTk2OGEzZWI5ODE0MDdkNjkvR2VtaW5pX0dlbmVyYXRlZF9JbWFnZV8xdWNiNnQxdWNiNnQxdWNiLTZhMGUwYmY3OWQ1NmJjMWFmODA0NTc5MS5wbmc=.jpg"
    },
    {
        "name": "تريبل سماش برجر",
        "price": 33.00,
        "calories": "1250 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع ثلاث شرائح من لحم البلاك أنجوس وثلاث شرائح من جبنة تشيدر الأمريكية وصوص سوما الخاص.",
        "img": "https://resizer.deliverect.com/TXvqNQCQWx7phCBRxWXi4yBtBdT3czIXah5cfLfaPmM/rt:fill/g:ce/el:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2lrb25hLWJ1Y2tldC1wcm9kdWN0aW9uL2ltYWdlcy82ODVjZTFlZTk2OGEzZWI5ODE0MDdkNjkvRFNDMDgwNTUtNmEwZTBjMWE1YmM0M2FjY2RhYjk2ZTJhLmpwZWc=.jpg"
    },
    {
        "name": "دبل سماش برجر",
        "price": 27.00,
        "calories": "1055 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر الأمريكية مع صوص سوما الخاص.",
        "img": "https://resizer.deliverect.com/8vro1kOj2bqOtSsQR-nVsCQ7xNpQ0f28U7Yb7DqxiIM/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NTE1NzIzOTZfOWY0ZGY5MGMtY2ZmZC00NDUxLTk3ZGQtODBjMDZhMGUwMWY2LmpwZWc=.jpg"
    },
    {
        "name": "بطاطس سوما",
        "price": 18.00,
        "calories": "735 سعرة حرارية",
        "category": "المقبلات",
        "desc": "بطاطس مقرمشة مع قطع لحم بلاك أنجوس ومزيج جبنة التشيدر الأمريكية مع صوص سوما والبصل المقرمش.",
        "img": "https://resizer.deliverect.com/W9WJ8vnk1qqALXyLNrttO3DRMpLpwYG-xH94Q2LSdIw/rt:fill/g:ce/el:0/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2lrb25hLWJ1Y2tldC1wcm9kdWN0aW9uL2ltYWdlcy82ODVjZTFlZTk2OGEzZWI5ODE0MDdkNjkvJUQ4JUE4JUQ4JUI3JUQ4JUE3JUQ4JUI3JUQ4JUIzJTIwJUQ4JUI5JUQ4JUE3JUQ4JUFGJUQ5JThBLTZhMGRmYjhiNDYyNDJhMDA0NDBhZTM1NC5qcGc=.jpg"
    },
    {
        "name": "وجبة سوما الخاصة (1)",
        "price": 30.00,
        "calories": "950 سعرة حرارية",
        "category": "البرجر",
        "desc": "أحدث وأشهى إضافات القائمة لدينا من صوصات ووجبات سوما المميزة.",
        "img": "https://resizer.deliverect.com/lvGJ205eA2RGsSqjPt_YmmFt7k3F7d3gzPY2yAjs5S4/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NTE5OTA3NThfOWY1N2I2YWUtMjVjOC00ZGFjLThlMGUtODViMzVkMDA5MWNiLmpwZw==.jpg"
    },
    {
        "name": "وجبة سوما الخاصة (2)",
        "price": 32.00,
        "calories": "980 سعرة حرارية",
        "category": "البرجر",
        "desc": "صنف إضافي مميز من قائمة طعام مطعم سوما الأصلية.",
        "img": "https://resizer.deliverect.com/un8_t-OWsMYyka23y36N0my6JXlgOadJO2wHHq8Hbwg/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NTE5OTA2NTFfOWY1N2I2MGItNGE3MC00NjNkLTljN2MtZjRiNjdkZWM0NDBmLmpwZw==.jpg"
    },
    {
        "name": "وجبة سوما الخاصة (3)",
        "price": 34.00,
        "calories": "1020 سعرة حرارية",
        "category": "البرجر",
        "desc": "صنف إضافي فاخر من قائمة طعام مطعم سوما.",
        "img": "https://resizer.deliverect.com/06_ZVDOorMBA2tkDpH3dDpHjIEvdgLgGP3SAr3tPW0s/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NTE5OTA3NDRfOWY1N2I2OTgtZWIwMi00YTFlLTg5YjAtNTQ4MWRjZWFmYzcyLmpwZw==.jpg"
    },
    {
        "name": "وجبة سوما الخاصة (4)",
        "price": 35.00,
        "calories": "1050 سعرة حرارية",
        "category": "البرجر",
        "desc": "إضافة جديدة مميزة من قائمة مطعم سوما الأصلية.",
        "img": "https://resizer.deliverect.com/ghRZyTtvE1Dl4BIsm8ZCWimlukz_0juZIhqeI-Kg1cg/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NTE5OTA0NDlfOWY1N2I0ZDYtMjhmNi00NGVlLThlYTctNGQzYjBhYzFlMjYxLmpwZw==.jpg"
    },
    {
        "name": "وجبة سوما الخاصة (5)",
        "price": 36.00,
        "calories": "1100 سعرة حرارية",
        "category": "البرجر",
        "desc": "صنف إضافي أصلي من قائمة مطعم سوما.",
        "img": "https://resizer.deliverect.com/8mZ_THjQkRSpoAwSKAxQkAaZa6f7ogokI_ChQ8Yoiqo/rt:fill/g:ce/el:0/cb:ededc03f2f7a45d9b29970a490a648e5/aHR0cHM6Ly9mb29kaWNzLWNvbnNvbGUtcHJvZHVjdGlvbi5zMy5ldS13ZXN0LTEuYW1hem9uYXdzLmNvbS9pbWFnZXMvMTE2OTAzXzE3NDg5NDMwOTNfOWYxMGMxMmUtMzE5ZC00NTY1LTkxODUtZmEwYTI1ODhlNDBlLmpwZw==.jpg"
    }
]

# تصفية المنتجات حسب القسم
categories = ["الكل", "البرجر", "المقبلات"]
selected_category = st.selectbox("📂 تصنيفات القائمة:", categories)

# تهيئة سلة المشتريات
if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("---")
st.subheader("📋 قائمة الوجبات")

# عرض الوجبات
for item in menu_items:
    if selected_category == "الكل" or item["category"] == selected_category:
        with st.container():
            st.markdown("<div class='food-card'>", unsafe_allow_html=True)
            
            # عرض صورة الوجبة من السيرفر الأصلي
            st.image(item["img"], use_container_width=True)
            
            st.markdown(
                f"""
                    <h3 style='margin-top: 10px; margin-bottom: 4px; color: #ffffff; font-size: 18px;'>{item['name']}</h3>
                    <span class='badge'>{item['calories']}</span>
                    <p style='color: #a0aec0; margin-top: 6px; font-size: 13px; line-height: 1.4;'>{item['desc']}</p>
                    <p style='color: #ff6b6b; font-weight: bold; font-size: 16px; margin-bottom: 10px;'>{item['price']:.2f} SAR</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(f"إضافة للسلة 🛒 ({item['name']})", key=item["name"]):
                st.session_state.cart.append(item)
                st.success(f"تمت إضافة {item['name']} للسلة بنجاح!")

st.markdown("---")

# قسم سلة الطلبات وإرسالها للواتساب
st.subheader("🛒 سلة المشتريات")

if len(st.session_state.cart) > 0:
    total_price = 0
    for cart_item in st.session_state.cart:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"• {cart_item['name']}")
        with c2:
            st.write(f"**{cart_item['price']:.2f} SAR**")
        total_price += cart_item["price"]

    st.markdown(f"### المجموع الكلي: **{total_price:.2f} SAR**")

    whatsapp_text = "مرحباً، أود إرسال طلب من تطبيق سوما:%0a"
    for ci in st.session_state.cart:
        whatsapp_text += f"- {ci['name']} ({ci['price']:.2f} SAR)%0a"
    whatsapp_text += f"المجموع الكلي: {total_price:.2f} SAR"

    wa_url = f"https://wa.me/966556344884?text={whatsapp_text}"

    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("🗑️ تفريغ السلة"):
            st.session_state.cart = []
            st.rerun()
    with col_w2:
        st.markdown(
            f"<a href='{wa_url}' target='_blank'><button style='width:100%; background-color:#25d366; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold; text-align:center; cursor:pointer;'>إرسال للواتساب 📱</button></a>",
            unsafe_allow_html=True,
        )
else:
    st.info("السلة فارغة حالياً. اختر وجبتك المفضلة وأضفها للسلة.")

st.markdown("---")

# معلومات التواصل والعنوان
st.subheader("📍 معلومات المطعم")
st.markdown(
    "<p style='color: #cbd5e0;'>**العنوان:** طريق الأمير عبد الله بن عبد العزيز بن مسعيد بن جلوي، حي النهضة، بريدة</p>",
    unsafe_allow_html=True,
)

col_call, col_wa = st.columns(2)
with col_call:
    st.markdown(
        "<a href='tel:0556344884'><button style='width:100%; background-color:#3182ce; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold;'>📞 اتصال مباشر</button></a>",
        unsafe_allow_html=True,
    )
with col_wa:
    st.markdown(
        "<a href='https://wa.me/966556344884' target='_blank'><button style='width:100%; background-color:#38a169; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold;'>💬 واتساب</button></a>",
        unsafe_allow_html=True,
    )
