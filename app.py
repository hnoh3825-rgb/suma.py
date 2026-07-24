import streamlit as st

# إعدادات الصفحة لتكون ملائمة للجوال وبشكل أنيق
st.set_page_config(
    page_title="سوما | SUMA",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات CSS متقدمة لتصميم يشبه تطبيقات التوصيل الاحترافية
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fb;
    }
    .restaurant-header {
        text-align: center;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1e1e1e;
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
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border: 1px solid #edf2f7;
    }
    .badge {
        background-color: #edf2f7;
        color: #2d3436;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# رأس التطبيق
st.markdown(
    "<div class='restaurant-header'><h1>🍔 سوما | SUMA</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #718096;'>ألذ وجبات البرجر الطازج وبلاك أنجوس 🔥</p></div>",
    unsafe_allow_html=True,
)

# شريط معلومات سريعة
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("⭐ **4.7** (158 تقييم)")
with col2:
    st.markdown("💵 **20 - 40 SAR**")
with col3:
    st.markdown("🟢 **مفتوح للطلبات**")

st.markdown("---")

# القائمة الحقيقية المستخرجة من موقعهم
menu_items = [
    {
        "name": "أوكلاهوما برجر",
        "price": 28.00,
        "calories": "1090 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس المشوية مع شرائح البصل وشريحتين من جبنة تشيدر الأمريكية.",
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500",
    },
    {
        "name": "تريبل سماش برجر",
        "price": 33.00,
        "calories": "1250 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع ثلاث شرائح من لحم البلاك أنجوس وثلاث شرائح من جبنة تشيدر الأمريكية وصوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500",
    },
    {
        "name": "دبل سماش برجر",
        "price": 27.00,
        "calories": "1055 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر الأمريكية مع صوص سوما الخاص.",
        "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500",
    },
    {
        "name": "ترفل برجر",
        "price": 29.00,
        "calories": "1120 سعرة حرارية",
        "category": "البرجر",
        "desc": "خبز البريوش مع شريحتين من لحم البلاك أنجوس وشريحتين من جبنة تشيدر البيضاء وصوص الترفل والخس.",
        "img": "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500",
    },
    {
        "name": "بطاطس سوما",
        "price": 18.00,
        "calories": "735 سعرة حرارية",
        "category": "المقبلات والبطاطس",
        "desc": "بطاطس مع قطع لحم بلاك أنجوس ومزيج جبنة التشيدر الأمريكية مع صوص سوما والبصل المقرمش.",
        "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500",
    },
    {
        "name": "صوص سوما الخاص",
        "price": 2.00,
        "calories": "88 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص سوما المميز والسر في طعم البرجر.",
        "img": "https://images.unsplash.com/photo-1585238342024-78d387f4a707?w=500",
    },
    {
        "name": "ترفل صوص",
        "price": 3.00,
        "calories": "95 سعرة حرارية",
        "category": "الصوصات",
        "desc": "صوص كمأة ممزوج بنكهات متوازنة ومنسجمة.",
        "img": "https://images.unsplash.com/photo-1472476afb106-8b44a74ef2f5?w=500",
    },
]

# تصفية الأقسام
categories = ["الكل", "البرجر", "المقبلات والبطاطس", "الصوصات"]
selected_category = st.selectbox("📂 تصفح القائمة حسب القسم:", categories)

# تهيئة السلة
if "cart" not in st.session_state:
    st.session_state.cart = []

st.markdown("---")
st.subheader("📋 المنتجات المتوفرة")

# عرض المنتجات بتصميم بطاقات أنيق
for item in menu_items:
    if selected_category == "الكل" or item["category"] == selected_category:
        with st.container():
            st.markdown(
                f"""
                <div class='food-card'>
                    <h3 style='margin-bottom: 5px; color: #1a202c;'>{item['name']}</h3>
                    <span class='badge'>{item['calories']}</span>
                    <p style='color: #4a5568; margin-top: 8px; font-size: 14px;'>{item['desc']}</p>
                    <p style='color: #e53e3e; font-weight: bold; font-size: 16px;'>{item['price']} SAR</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(f"إضافة للسلة 🛒 ({item['name']})", key=item["name"]):
                st.session_state.cart.append(item)
                st.success(f"تمت إضافة {item['name']} بنجاح!")

st.markdown("---")

# عرض سلة المشتريات المتقدمة
st.subheader("🛒 سلة الطلبات المبدئية")

if len(st.session_state.cart) > 0:
    total_price = 0
    for i, cart_item in enumerate(st.session_state.cart):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.write(f"• {cart_item['name']}")
        with c2:
            st.write(f"**{cart_item['price']} SAR**")
        total_price += cart_item["price"]

    st.markdown(f"### المجموع الكلي: **{total_price:.2f} SAR**")

    # زر إتمام الطلب عبر الواتساب مع تنسيق الرسالة تلقائياً
    whatsapp_text = (
        "مرحباً، أود طلب الأغذية التالية من تطبيق سوما التجريبي:%0a"
    )
    for ci in st.session_state.cart:
        whatsapp_text += f"- {ci['name']} ({ci['price']} SAR)%0a"
    whatsapp_text += f"المجموع الكلي: {total_price:.2f} SAR"

    wa_url = f"https://wa.me/966556344884?text={whatsapp_text}"

    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("🗑️ تفريغ السلة"):
            st.session_state.cart = []
            st.rerun()
    with col_w2:
        st.markdown(
            f"<a href='{wa_url}' target='_blank'><button style='width:100%; background-color:#25d366; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold; text-align:center; cursor:pointer;'>إرسال الطلب للواتساب 📱</button></a>",
            unsafe_allow_html=True,
        )
else:
    st.info("سلة الطلبات فارغة حالياً. اختر وجبتك المفضلة وأضفها للسلة!")

st.markdown("---")

# قسم معلومات المطعم التواصلية
st.subheader("📍 معلومات المطعم والتواصل")
st.markdown(
    "**العنوان:** طريق الأمير عبد الله بن عبد العزيز بن مسعيد بن جلوي، حي النهضة، بريدة"
)

c_call, c_wa = st.columns(2)
with c_call:
    st.markdown(
        "<a href='tel:0556344884'><button style='width:100%; background-color:#3182ce; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold;'>📞 اتصال مباشر</button></a>",
        unsafe_allow_html=True,
    )
with c_wa:
    st.markdown(
        "<a href='https://wa.me/966556344884' target='_blank'><button style='width:100%; background-color:#38a169; color:white; border:none; padding:10px; border-radius:12px; font-weight:bold;'>💬 واتساب</button></a>",
        unsafe_allow_html=True,
    )
