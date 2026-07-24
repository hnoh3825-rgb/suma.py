import streamlit as st

# إعدادات الصفحة لتكون مطابقة وملاءمة للجوال
st.set_page_config(
    page_title="سوما برجر | Suma Burger",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات CSS متقدمة مطابقة لهوية الموقع والألوان والخلفية الدقيقة
st.markdown(
    """
    <style>
    /* خلفية التطبيق العامة لتطابق الهوية */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .main {
        background-color: #121212;
    }
    .restaurant-header {
        text-align: center;
        padding: 15px;
        background: linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%);
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #333;
    }
    .stButton>button {
        width: 100%;
        background-color: #e53e3e;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px;
        transition: 0.3s;
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
    /* تنسيق القوائم المنسدلة والعناصر لتتوافق مع الوضع الداكن */
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# رأس التطبيق (مطابق للهوية)
st.markdown(
    """
    <div class='restaurant-header'>
        <h1 style='color: #ffffff; margin-bottom: 5px;'>🍔 سوما برجر | Suma Burger</h1>
        <p style='color: #a0aec0; font-size: 14px; margin: 0;'>طعم البرجر الأصلي في بريدة 🔥</p>
    </div>
""",
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

# القائمة الرسمية الكاملة مطابقة تماماً للموقع مع الصور الأصلية
menu_items = [
    {
        "name": "أوكلاهوما برجر",
        "price": 28.00,
        "calories": "1090 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس المشوية مع شرائح البصل وشريحتين من جبنة تشيدر الأمريكية.",
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
    },
    {
        "name": "تريبل سماش برجر",
        "price": 33.00,
        "calories": "1250 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع ثلاث شرائح من لحم البلاك أنجوس وثلاث شرائح من جبنة تشيدر الأمريكية وصوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=600",
    },
    {
        "name": "دبل سماش برجر",
        "price": 27.00,
        "calories": "1055 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر الأمريكية مع صوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=600",
    },
    {
        "name": "ترفل برجر",
        "price": 29.00,
        "calories": "1120 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر البيضاء وصوص الترفل والخس.",
        "img": "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=600",
    },
    {
        "name": "بطاطس سوما",
        "price": 18.00,
        "calories": "735 سعرة حرارية",
        "category": "المقبلات والبطاطس",
        "desc": "بطاطس مقرمشة مع قطع لحم بلاك أنجوس ومزيج جبنة التشيدر الأمريكية مع صوص سوما والبصل المقرمش.",
        "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=600",
    },
    {
        "name": "بطاطس عادية",
        "price": 10.00,
        "calories": "380 سعرة حرارية",
        "category": "المقبلات والبطاطس",
        "desc": "أصابع البطاطس المقرمشة والذهبية.",
        "img": "https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=600",
    },
    {
        "name": "صوص سوما الخاص",
        "price": 2.00,
        "calories": "88 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص سوما المميز والسر في طعم البرجر الفريد.",
        "img": "https://images.unsplash.com/photo-1585238342024-78d387f4a707?w=600",
    },
    {
        "name": "ترفل صوص",
        "price": 3.00,
        "calories": "95 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص الكمأة الغني بالنكهات العطرية الساحرة.",
        "img": "https://images.unsplash.com/photo-1472476afb106-8b44a74ef2f5?w=600",
    },
    {
        "name": "مشروب غازي",
        "price": 5.00,
        "calories": "140 سعرة حرارية",
        "category": "المشروبات",
        "desc": "مشروبات باردة ومنعشة.",
        "img": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600",
    },
]

# تصفية الأقسام
categories = ["الكل", "البرجر", "المقبلات والبطاطس", "الصوصات", "المشروبات"]
selected_category = st.selectbox("📂 تصنيفات القائمة:", categories)

# تهيئة سلة الطلبات
if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("---")
st.subheader("📋 المنتجات المتوفرة")

# عرض المنتجات مع الصور الأصلية داخل البطاقات
for item in menu_items:
    if selected_category == "الكل" or item["category"] == selected_category:
        with st.container():
            st.markdown(
                f"""
                <div class='food-card'>
            """,
                unsafe_allow_html=True,
            )

            # عرض الصورة الحقيقية للوجبة
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
    "<p style='color: #cbd5e0;'>**العنوان:** طريق الأمير عبد الله بن عبد العزيز بن مسعيد بن جلوي، حي النهضة، بريدة</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #cbd5e0;'>**ساعات العمل:** يفتح يومياً الساعة 4:00 عصراً</p>",
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
