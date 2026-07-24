-=import streamlit as st

# إعدادات الصفحة لتكون ملائمة للجوال
st.set_page_config(
    page_title="سوما برجر | Suma Burger",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# تنسيقات CSS مخصصة لإعطاء طابع تطبيق حقيقي للمطعم
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4757;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff6b81;
        color: white;
    }
    .card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# رأس التطبيق
st.markdown(
    "<h1 style='text-align: center; color: #2d3436;'>🍔 سوما برجر</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #636e72;'>طعم البرجر الأصلي في بريدة  🔥</p>",
    unsafe_allow_html=True,
)

# شريط الحالة ومعلومات سريعة
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("⭐ **4.7** (158)")
with col2:
    st.markdown("💵 **20–40 SAR**")
with col3:
    st.markdown("🔴 **مغلق الآن**")

st.markdown("---")

# القائمة (Menu)
st.subheader("📋 قائمة الوجبات")

# أقسام القائمة
menu_category = st.selectbox(
    "اختر القسم:", ["الكل", "البرجر", "المقبلات", "المشروبات"]
)

# منتجات تجريبية مستوحاة من مطاعم البرجر
products = [
    {
        "name": "سوما كلاسيك برجر",
        "price": 32,
        "category": "البرجر",
        "desc": "لحم أنجوس طازج، جبن أمريكي، صوص سوما الخاص",
        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500",
    },
    {
        "name": "دبل سموك برجر",
        "price": 38,
        "category": "البرجر",
        "desc": "قطعتين لحم، بصل مقرمش، صوص المدخن",
        "img": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500",
    },
    {
        "name": "بطاطس بالجبن والبيكن",
        "price": 20,
        "category": "المقبلات",
        "desc": "بطاطس مقرمشة مع جبن ساخن وقطع بيوكن",
        "img": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500",
    },
    {
        "name": "مشروب غازي",
        "price": 6,
        "category": "المشروبات",
        "desc": "مشروب بارد ومنعش",
        "img": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500",
    },
]

# تهيئة سلة المشتريات
if "cart" not in st.session_state:
    st.session_state.cart = []

# عرض المنتجات
for p in products:
    if menu_category == "الكل" or p["category"] == menu_category:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <h3>{p['name']}</h3>
                    <p style='color: #636e72;'>{p['desc']}</p>
                    <p style='color: #e84118; font-weight: bold;'>السعر: {p['price']} SAR</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button(f"إضافة للسلة - {p['name']}", key=p["name"]):
                st.session_state.cart.append(p)
                st.success(f"تمت إضافة {p['name']} إلى السلة!")

st.markdown("---")

# سلة المشتريات والطلبات
st.subheader("🛒 سلة المشتريات")
if len(st.session_state.cart) > 0:
    total = 0
    for idx, item in enumerate(st.session_state.cart):
        st.write(f"- {item['name']} | **{item['price']} SAR**")
        total += item["price"]

    st.markdown(f"### المجموع الكلي: **{total} SAR**")

    if st.button("إرسال الطلب (عبر الواتساب)"):
        st.success(
            "تم تحويلك إلى خدمة العملاء لإتمام الطلب! (رقم المطعم: 0556344884)"
        )
        st.session_state.cart = []
else:
    st.info("السلة فارغة حالياً.")

st.markdown("---")

# معلومات التواصل والعنوان
st.subheader("📍 معلومات المطعم والتواصل")
st.markdown("**العنوان:** طريق الأمير عبد الله بن عبد العزيز بن مسعيد بن جلوي، حي النهضة، بريدة")
st.markdown("**ساعات العمل:** يفتح الساعة 4:00 عصراً")

col_call, col_wa = st.columns(2)
with col_call:
    st.markdown(
        "[📞 الاتصال بالمطعم](tel:0556344884)",
        unsafe_allow_html=True,
    )
with col_wa:
    st.markdown(
        "[💬 مراسلة واتساب](https://wa.me/966556344884)",
        unsafe_allow_html=True,
    )