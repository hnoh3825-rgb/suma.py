<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SUMA - طلبات الطعام</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Cairo', sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
        }

        /* رأس الصفحة الأصفر */
        .header-top {
            background-color: #ccff00;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
        }

        .header-left, .header-right {
            display: flex;
            align-items: center;
            gap: 15px;
            cursor: pointer;
        }

        .order-type-selector {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            font-size: 13px;
            font-weight: 700;
            color: #0044cc;
        }

        .order-type-selector span:first-child {
            color: #666;
            font-size: 11px;
        }

        .logo-container {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
        }

        .logo-container img {
            height: 35px;
            object-fit: contain;
        }

        /* البانر الإعلاني الرئيسي */
        .banner-section {
            background-color: #ccff00;
            padding: 0 30px 30px 30px;
            display: flex;
            justify-content: center;
        }

        .banner-card {
            width: 100%;
            max-width: 1100px;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            position: relative;
        }

        .banner-card img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }

        /* تخطيط المحتوى الرئيسي */
        .main-container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 300px 1fr 320px;
            gap: 20px;
        }

        @media (max-width: 1024px) {
            .main-container {
                grid-template-columns: 1fr;
            }
        }

        /* القائمة الجانبية للتصنيفات (يمين) */
        .categories-sidebar {
            background: #fff;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            height: fit-content;
        }

        .category-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 15px;
            margin-bottom: 5px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            color: #0044cc;
            transition: background 0.2s;
        }

        .category-item:hover, .category-item.active {
            background-color: #f0f4ff;
        }

        .category-item i {
            font-size: 12px;
        }

        /* قسم المنتجات وسط الصفحة */
        .products-section {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .section-title {
            font-size: 18px;
            font-weight: 700;
            color: #0044cc;
            margin-bottom: 10px;
            border-bottom: 2px solid #ccff00;
            padding-bottom: 5px;
        }

        .product-card {
            background: #fff;
            border-radius: 12px;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .product-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        .product-info {
            flex: 1;
            padding-left: 15px;
        }

        .product-name {
            font-size: 16px;
            font-weight: 700;
            color: #0044cc;
            margin-bottom: 5px;
        }

        .product-desc {
            font-size: 13px;
            color: #666;
            margin-bottom: 10px;
            line-height: 1.4;
        }

        .product-meta {
            display: flex;
            gap: 15px;
            font-size: 12px;
            color: #888;
        }

        .product-price {
            font-weight: 700;
            color: #0044cc;
        }

        .product-img {
            width: 100px;
            height: 100px;
            border-radius: 10px;
            object-fit: cover;
        }

        /* سلة الطلبات (يسار) */
        .cart-sidebar {
            background: #fff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            height: fit-content;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            min-height: 200px;
            justify-content: center;
            border: 1px dashed #ddd;
        }

        .cart-icon-box {
            font-size: 32px;
            color: #888;
            margin-bottom: 10px;
        }

        .cart-text {
            color: #888;
            font-size: 14px;
        }

        /* النافذة المنسدلة لتفاصيل المنتج / الخيارات */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            padding: 20px;
        }

        .modal-content {
            background: #fff;
            width: 100%;
            max-width: 600px;
            border-radius: 16px;
            overflow: hidden;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            animation: modalFadeIn 0.3s ease;
        }

        @keyframes modalFadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .modal-header-img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            position: relative;
        }

        .modal-close-btn {
            position: absolute;
            top: 15px;
            left: 15px;
            background: rgba(0,0,0,0.6);
            color: #fff;
            border: none;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }

        .modal-body {
            padding: 20px;
            overflow-y: auto;
        }

        .modal-title {
            font-size: 20px;
            font-weight: 700;
            color: #0044cc;
            margin-bottom: 8px;
        }

        .modal-desc {
            font-size: 14px;
            color: #666;
            margin-bottom: 20px;
        }

        .option-group {
            margin-bottom: 20px;
            border-top: 1px solid #eee;
            padding-top: 15px;
        }

        .option-group-title {
            font-weight: 700;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            font-size: 15px;
        }

        .option-label {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            cursor: pointer;
            font-size: 14px;
        }

        .modal-footer {
            padding: 15px 20px;
            background: #f8f9fa;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .add-to-cart-btn {
            background-color: #ccff00;
            color: #000;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            font-size: 15px;
            width: 100%;
            transition: background 0.2s;
        }

        .add-to-cart-btn:hover {
            background-color: #b3e600;
        }
    </style>
</head>
<body>

    <!-- رأس الصفحة -->
    <header class="header-top">
        <div class="header-left">
            <i class="fa-solid fa-cart-shopping" style="color: #0044cc; font-size: 18px;"></i>
        </div>
        <div class="logo-container">
            <!-- استخدام اسم متطابق مع الشعار الموجود في تصميمك الخلفي -->
            <h1 style="color: #0044cc; font-weight: 900; letter-spacing: 2px; font-size: 24px;">SUMA</h1>
        </div>
        <div class="header-right">
            <div class="order-type-selector">
                <span>نوع الطلب</span>
                <strong>حدد نوع الطلب</strong>
            </div>
            <i class="fa-solid fa-bars" style="color: #0044cc; font-size: 18px;"></i>
        </div>
    </header>

    <!-- البانر الرئيسي المطابق لصورة الباكجراوند -->
    <section class="banner-section">
        <div class="banner-card">
            <!-- استبدل الرابط أدناه بصورة الباكجراوند الفعليّة back.jpg المرفوعة -->
            <img src="back.jpg" alt="SUMA Banner">
        </div>
    </section>

    <!-- المحتوى الرئيسي للقائمة -->
    <main class="main-container">
        
        <!-- سلة الطلبات (تظهر يسار في الشاشات الكبيرة) -->
        <aside class="cart-sidebar">
            <div class="cart-icon-box">
                <i class="fa-solid fa-bag-shopping"></i>
            </div>
            <p class="cart-text">أضف أصناف من القائمة</p>
        </aside>

        <!-- قائمة المنتجات (المنتصف) -->
        <section class="products-section" id="products-container">
            <h2 class="section-title">برجر</h2>
            
            <!-- منتج 1: الوكانهوما برجر -->
            <div class="product-card" onclick="openProductModal('الوكانهوما برجر', 'جرب اللذيذة مع شريحتين من لحم الأنجاس المخبوزة مع صوص الجمل وشرائح من جبنة تشيدر الأمريكية و...', '28.00', '1090 سعرة حرارية', 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500')">
                <div class="product-info">
                    <h3 class="product-name">الوكانهوما برجر</h3>
                    <p class="product-desc">جرب اللذيذة مع شريحتين من لحم الأنجاس المخبوزة مع صوص الجمل وشرائح من جبنة تشيدر الأمريكية و...</p>
                    <div class="product-meta">
                        <span>1090 سعرة حرارية</span>
                        <span class="product-price">28.00 ر.س</span>
                    </div>
                </div>
                <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500" alt="برجر" class="product-img">
            </div>

            <!-- منتج إضافي تجريبي للبرجر -->
            <div class="product-card" onclick="openProductModal('كلاسيك برجر', 'شريحة لحم بقر غني مع الخس الطازج والطماطم وصوص سوما الخاص والجبن.', '24.00', '850 سعرة حرارية', 'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500')">
                <div class="product-info">
                    <h3 class="product-name">كلاسيك برجر</h3>
                    <p class="product-desc">شريحة لحم بقر غني مع الخس الطازج والطماطم وصوص سوما الخاص والجبن.</p>
                    <div class="product-meta">
                        <span>850 سعرة حرارية</span>
                        <span class="product-price">24.00 ر.س</span>
                    </div>
                </div>
                <img src="https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500" alt="برجر" class="product-img">
            </div>
        </section>

        <!-- التصنيفات الجانبية (يمين) -->
        <aside class="categories-sidebar">
            <div class="category-item active" onclick="filterCategory('برجر', this)">
                <span>برجر</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item" onclick="filterCategory('أطباق جانبية', this)">
                <span>أطباق جانبية</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item" onclick="filterCategory('صوصات', this)">
                <span>صوصات</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item" onclick="filterCategory('مشروبات', this)">
                <span>مشروبات</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
        </aside>

    </main>

    <!-- نافذة تخصيص الطلب المنبثقة -->
    <div class="modal-overlay" id="productModal">
        <div class="modal-content">
            <div style="position: relative;">
                <img id="modalImg" src="" alt="" class="modal-header-img">
                <button class="modal-close-btn" onclick="closeProductModal()"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="modal-body">
                <h3 class="modal-title" id="modalTitle">عنوان المنتج</h3>
                <p class="modal-desc" id="modalDesc">وصف تفصيلي للمنتج يظهر هنا...</p>
                
                <div class="option-group">
                    <div class="option-group-title">
                        <span>اختر الإضافات المفضلة</span>
                        <span style="font-size: 12px; color: #888;">اختياري</span>
                    </div>
                    <label class="option-label">
                        <span>جبن إضافي</span>
                        <input type="checkbox">
                    </label>
                    <label class="option-label">
                        <span>صوص سوما إضافي</span>
                        <input type="checkbox">
                    </label>
                </div>
            </div>
            <div class="modal-footer">
                <button class="add-to-cart-btn" onclick="closeProductModal()">إضافة إلى السلة</button>
            </div>
        </div>
    </div>

    <script>
        // دالة فتح نافذة المنتج
        function openProductModal(title, desc, price, calories, imgUrl) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalDesc').innerText = desc + " (" + calories + ")";
            document.getElementById('modalImg').src = imgUrl;
            document.getElementById('productModal').style.display = 'flex';
        }

        // دالة إغلاق النافذة
        function closeProductModal() {
            document.getElementById('productModal').style.display = 'none';
        }

        // محاكاة التنقل بين التصنيفات
        function filterCategory(categoryName, element) {
            document.querySelectorAll('.categories-sidebar .category-item').forEach(item => {
                item.classList.remove('active');
            });
            element.classList.add('active');
            document.querySelector('.products-section .section-title').innerText = categoryName;
            
            // يمكن تحديث المنتجات هنا حسب التصنيف المختار
        }

        // إغلاق النافذة عند النقر خارج المحتوى
        window.onclick = function(event) {
            let modal = document.getElementById('productModal');
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    </script>
</body>
</html>
