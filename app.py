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

        .logo-container h1 {
            color: #0044cc;
            font-weight: 900;
            letter-spacing: 2px;
            font-size: 24px;
            margin: 0;
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
            order: 3;
        }

        @media (min-width: 1025px) {
            .categories-sidebar {
                order: 1;
            }
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

        /* قسم المنتجات وسط الصفحة */
        .products-section {
            display: flex;
            flex-direction: column;
            gap: 20px;
            order: 2;
        }

        .section-title {
            font-size: 18px;
            font-weight: 700;
            color: #0044cc;
            margin-bottom: 10px;
            border-bottom: 2px solid #ccff00;
            padding-bottom: 5px;
            text-align: right;
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
            text-align: right;
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
            order: 3;
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
    </style>
</head>
<body>

    <!-- رأس الصفحة -->
    <header class="header-top">
        <div class="header-left">
            <i class="fa-solid fa-cart-shopping" style="color: #0044cc; font-size: 18px;"></i>
        </div>
        <div class="logo-container">
            <h1>SUMA</h1>
        </div>
        <div class="header-right">
            <div class="order-type-selector">
                <span>نوع الطلب</span>
                <strong>حدد نوع الطلب</strong>
            </div>
            <i class="fa-solid fa-bars" style="color: #0044cc; font-size: 18px;"></i>
        </div>
    </header>

    <!-- البانر الرئيسي باستخدام صورة الخلفية back.jpg -->
    <section class="banner-section">
        <div class="banner-card">
            <img src="back.jpg" alt="SUMA Banner">
        </div>
    </section>

    <!-- المحتوى الرئيسي للقائمة -->
    <main class="main-container">
        
        <!-- سلة الطلبات (يسار) -->
        <aside class="cart-sidebar">
            <div class="cart-icon-box">
                <i class="fa-solid fa-bag-shopping"></i>
            </div>
            <p class="cart-text">أضف أصناف من القائمة</p>
        </aside>

        <!-- قائمة المنتجات (المنتصف) -->
        <section class="products-section">
            <h2 class="section-title">برجر</h2>
            
            <div class="product-card">
                <div class="product-info">
                    <h3 class="product-name">الوكانهوما برجر</h3>
                    <p class="product-desc">جرب اللذيذة مع شريحتين من لحم الأنجاس المخبوزة مع صوص الجمل وشرائح من جبنة تشيدر الأمريكية...</p>
                    <div class="product-meta">
                        <span>1090 سعرة حرارية</span>
                        <span class="product-price">28.00 ر.س</span>
                    </div>
                </div>
                <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500" alt="برجر" class="product-img">
            </div>

            <div class="product-card">
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
            <div class="category-item active">
                <span>برجر</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item">
                <span>أطباق جانبية</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item">
                <span>صوصات</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
            <div class="category-item">
                <span>مشروبات</span>
                <i class="fa-solid fa-chevron-left"></i>
            </div>
        </aside>

    </main>

</body>
</html>
