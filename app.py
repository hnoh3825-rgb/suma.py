import streamlit as st

# إعدادات الصفحة لتكون ملائمة للجوال
st.set_page_config(
    page_title="سوما برجر | Suma Burger",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات مخصصة لتصميم يشبه تطبيقات التوصيل الاحترافية
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .restaurant-header {
        text-align: center;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1a1a1a;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #ff4757;
        color: white;
    }
    .food-card {
        background: white;
        padding: 16px;
        border-radius: 14px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        margin-bottom: 12px;
        border: 1px solid #edf2f7;
    }
    .badge {
        background-color: #fff5f5;
        color: #e53e3e;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# رأس التطبيق
st.markdown(
    "<div class='restaurant-header'><h1>🍔 سوما برجر | Suma Burger</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #718096; font-size: 14px;'>ألذ وجبات البرجر الطازج في بريدة 🔥</p></div>",
    unsafe_allow_html=True,
)

# شريط معلومات سريعة
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("⭐ **4.7** (158)")
with col2:
    st.markdown("💵 **20–40 SAR**")
with col3:
    st.markdown("🟢 **متاح للطلب**")

st.markdown("---")

# القائمة الرسمية الكاملة المطابقة لموقعهم
menu_items = [
    # قسم البرجر
    {
        "name": "أوكلاهوما برجر",
        "price": 28.00,
        "calories": "1090 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس المشوية مع شرائح البصل وشريحتين من جبنة تشيدر الأمريكية.",
    },
    {
        "name": "تريبل سماش برجر",
        "price": 33.00,
        "calories": "1250 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع ثلاث شرائح من لحم البلاك أنجوس وثلاث شرائح من جبنة تشيدر الأمريكية وصوص سوما الخاص.",
    },
    {
        "name": "دبل سماش برجر",
        "price": 27.00,
        "calories": "1055 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر الأمريكية مع صوص سوما الخاص.",
    },
    {
        "name": "ترفل برجر",
        "price": 29.00,
        "calories": "1120 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر البيضاء وصوص الترفل والخس.",
    },
    # قسم المقبلات والبطاطس
    {
        "name": "بطاطس سوما",
        "price": 18.00,
        "calories": "735 سعرة حرارية",
        "category": "المقبلات والبطاطس",
        "desc": "بطاطس مقرمشة مع قطع لحم بلاك أنجوس ومزيج جبنة التشيدر الأمريكية مع صوص سوما والبصل المقرمش.",
    },
    {
        "name": "بطاطس عادية",
        "price": 10.00,
        "calories": "380 سعرة حرارية",
        "category": "المقبلات والبطاطس",
        "desc": "أصابع البطاطس المقرمشة والذهبية.",
    },
    # قسم الصوصات
    {
        "name": "صوص سوما الخاص",
        "price": 2.00,
        "calories": "88 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص سوما المميز والسر في طعم البرجر الفريد.",
    },
    {
        "name": "ترفل صوص",
        "price": 3.00,
        "calories": "95 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص الكمأة الغني بالنكهات العطرية الساحرة.",
    },
    # قسم المشروبات
    {
        "name": "مشروب غازي",
        "price": 5.00,
        "calories": "140 سعرة حرارية",
        "category": "المشروبات",
        "desc": "مشروبات باردة ومنعشة.",
    },
]

# اختيار القسم
categories = ["الكل", "البرجر", "المقبلات والبطاطس", "الصوصات", "المشروبات"]
selected_category = st.selectbox("📂 تصنيفات القائمة:", categories)

# تهيئة سلة الطلبات
if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("---")
st.subheader("📋 المنتجات المتوفرة")

# عرض المنتجات
for item in menu_items:
    if selected_category == "الكل" or item["category"] == selected_category:
        with st.container():
            st.markdown(
                f"""
                <div class='food-card'>
                    <h3 style='margin-bottom: 4px; color: #1a202c; font-size: 18px;'>{item['name']}</h3>
                    <span class='badge'>{item['calories']}</span>
                    <p style='color: #4a5568; margin-top: 8px; font-size: 13px; line-height: 1.4;'>{item['desc']}</p>
                    <p style='color: #e53e3e; font-weight: bold; font-size: 16px; margin-bottom: 0px;'>{item['price']:.2f} SAR</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(f"إضافة للسلة 🛒 ({item['name']})", key=item["name"]):
                st.session_state.cart.append(item)
                st.success(f"تمت إضافة {item['name']} إلى السلة!")

st.markdown("---")

# سلة الطلبات
st.subheader("🛒 سلة المشتريات والطلبات")

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

    # تجهيز رسالة الواتساب التلقائية
    whatsapp_text = (
        "مرحباً، أود إرسال طلب تجريبي من تطبيق سوما برجر:%0a"
    )
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
    st.info("السلة فارغة حالياً. تصفح القائمة وأضف طلباتك.")

st.markdown("---")

# معلومات التواصل والعنوان
st.subheader("📍 معلومات المطعم والتواصل")
st.markdown(
    "**العنوان:** طريق الأمير عبد الله بن عبد العزيز بن مسعيد بن جلوي، حي النهضة، بريدة"
)
st.markdown("**ساعات العمل:** يفتح يومياً الساعة 4:00 عصراً")

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
