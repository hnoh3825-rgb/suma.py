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

# رأس التطبيق (الهوية الرسمية)
st.markdown(
    """
    <div class='restaurant-header'>
        <h1 style='color: #ffffff; margin-bottom: 5px;'>🍔 سوما | SUMA</h1>
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

# القائمة الرسمية للوجبات مع صور الموقع الأساسي
menu_items = [
    {
        "name": "أوكلاهوما برجر",
        "price": 28.00,
        "calories": "1090 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس المشوية مع شرائح البصل وشريحتين من جبنة تشيدر الأمريكية.",
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=600&auto=format&fit=crop",
    },
    {
        "name": "تريبل سماش برجر",
        "price": 33.00,
        "calories": "1250 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع ثلاث شرائح من لحم البلاك أنجوس وثلاث شرائح من جبنة تشيدر الأمريكية وصوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?q=80&w=600&auto=format&fit=crop",
    },
    {
        "name": "دبل سماش برجر",
        "price": 27.00,
        "calories": "1055 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر الأمريكية مع صوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=600&auto=format&fit=crop",
    },
    {
        "name": "بطاطس سوما",
        "price": 18.00,
        "calories": "735 سعرة حرارية",
        "category": "المقبلات",
        "desc": "بطاطس مقرمشة مع قطع لحم بلاك أنجوس ومزيج جبنة التشيدر الأمريكية مع صوص سوما والبصل المقرمش.",
        "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?q=80&w=600&auto=format&fit=crop",
    },
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
            
            # عرض صورة الوجبة
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
