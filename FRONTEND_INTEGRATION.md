# 🔗 دليل ربط Backend مع Frontend

## ✅ ما تم إضافته للربط مع Frontend

### 1. 🔓 CORS (Cross-Origin Resource Sharing)
**تم إضافته ✓**

- تم تفعيل `django-cors-headers` للسماح للـ Frontend بالاتصال بالـ Backend
- في Development: جميع الـ origins مسموحة
- في Production: يجب تحديد الـ origins المسموحة في `CORS_ALLOWED_ORIGINS`

**الاستخدام:**
```javascript
// Frontend يمكنه الآن الاتصال بدون مشاكل
fetch('http://127.0.0.1:8000/api/products/')
```

---

### 2. 🔍 Filtering & Searching
**تم إضافته ✓**

المنتجات الآن تدعم:
- **Filtering**: حسب الفئة (`?category=1` أو `?category__name=Electronics`)
- **Searching**: البحث في الاسم والوصف (`?search=laptop`)
- **Ordering**: الترتيب حسب السعر، التاريخ، الاسم (`?ordering=price` أو `?ordering=-price`)

**أمثلة:**
```
GET /api/products/?category=1
GET /api/products/?search=laptop
GET /api/products/?ordering=-price
GET /api/products/?category=1&search=laptop&ordering=price
```

---

### 3. 📚 Swagger/OpenAPI Documentation
**تم إضافته ✓**

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`
- **API Docs**: `http://127.0.0.1:8000/api-docs/`

يمكن للـ Frontend developers استخدام هذه الصفحات لرؤية جميع الـ APIs وتجربتها مباشرة!

---

### 4. 🛡️ Throttling (Rate Limiting)
**تم إضافته ✓**

- **Anonymous users**: 100 requests/hour
- **Authenticated users**: 1000 requests/hour

هذا يحمي الـ API من الإساءة.

---

### 5. 📦 المكتبات المضافة

تم إضافة المكتبات التالية إلى `requirements.txt`:
- `django-cors-headers` - للسماح للـ Frontend بالاتصال
- `django-filter` - للفلترة والبحث
- `drf-yasg` - لتوثيق Swagger/OpenAPI
- `python-decouple` - لإدارة Environment Variables (جاهز للاستخدام)

---

## 🚀 خطوات الربط مع Frontend

### 1. تثبيت المكتبات الجديدة

```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA"
.\venv\Scripts\Activate.ps1
cd backend
pip install -r requirements.txt
```

### 2. تشغيل السيرفر

```powershell
python manage.py runserver
```

### 3. في Frontend (مثال React)

```javascript
// api.js
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// Get products with filtering
export const getProducts = async (filters = {}) => {
  const params = new URLSearchParams(filters);
  const response = await fetch(`${API_BASE_URL}/products/?${params}`);
  return response.json();
};

// Login
export const login = async (username, password) => {
  const response = await fetch(`${API_BASE_URL}/auth/login/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });
  return response.json();
};

// Authenticated request
export const getCart = async (token) => {
  const response = await fetch(`${API_BASE_URL}/cart/`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  return response.json();
};
```

---

## 📋 Checklist للربط مع Frontend

### ✅ الأساسيات (مكتملة)
- [x] CORS configured
- [x] JWT Authentication
- [x] API Documentation (Swagger)
- [x] Filtering & Searching
- [x] Pagination
- [x] Error Handling

### ⚠️ يجب إضافتها قبل Production

- [ ] Environment Variables (`.env` file)
- [ ] Update `ALLOWED_HOSTS` for production
- [ ] Set `DEBUG = False` in production
- [ ] Configure specific CORS origins (remove `CORS_ALLOW_ALL_ORIGINS`)
- [ ] Add HTTPS/SSL
- [ ] Database migration to PostgreSQL/MySQL (بدلاً من SQLite)
- [ ] Static files serving (WhiteNoise أو CDN)
- [ ] Logging configuration

---

## 🔧 إعدادات CORS للـ Production

في `settings.py`، غيّر:

```python
# Development
CORS_ALLOW_ALL_ORIGINS = True

# Production (يجب تغييره)
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
]
```

---

## 📝 ملاحظات مهمة

1. **Base URL**: جميع الـ APIs تبدأ بـ `/api/`
2. **Authentication**: استخدم `Authorization: Bearer <token>` في الـ header
3. **Content-Type**: استخدم `application/json` للـ POST/PUT requests
4. **Pagination**: جميع الـ list endpoints تدعم pagination (20 items per page)
5. **Error Format**: جميع الأخطاء ترجع في format:
   ```json
   {
     "error": "Error message"
   }
   ```

---

## 🧪 اختبار الـ API

### استخدام Swagger UI:
1. افتح `http://127.0.0.1:8000/swagger/`
2. اضغط على "Authorize" وأدخل JWT token
3. جرب أي endpoint مباشرة من المتصفح

### استخدام Postman/Thunder Client:
- Base URL: `http://127.0.0.1:8000`
- Authentication: Bearer Token
- جميع الـ endpoints موجودة في `API_DOCUMENTATION.md`

---

## 🎯 الخطوات التالية المقترحة

1. **إضافة Environment Variables**:
   - إنشاء `.env` file
   - نقل `SECRET_KEY` و `DEBUG` إلى `.env`

2. **إضافة File Upload**:
   - رفع صور المنتجات
   - رفع صور المستخدمين

3. **إضافة WebSocket** (اختياري):
   - للإشعارات الفورية
   - للـ real-time updates

4. **إضافة Caching** (اختياري):
   - لتحسين الأداء
   - Redis أو Memcached

---

## 📞 الدعم

- راجع `API_DOCUMENTATION.md` للتوثيق الكامل
- راجع `START_SERVER.md` لتعليمات التشغيل
- استخدم Swagger UI لرؤية جميع الـ APIs وتجربتها

**المشروع الآن جاهز للربط مع Frontend! 🎉**
