# 🚀 كيفية تشغيل المشروع وعرض الـ API

## ✅ تم إصلاح البيئة الافتراضية!

تم حذف الـ venv القديمة وإنشاء واحدة جديدة بنجاح.

## 📋 خطوات التشغيل

### 1️⃣ تفعيل البيئة الافتراضية

في PowerShell:
```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

أو إذا واجهت مشكلة في PowerShell:
```powershell
.\venv\Scripts\activate.bat
```

### 2️⃣ الانتقال إلى مجلد Backend

```powershell
cd backend
```

### 3️⃣ تشغيل الخادم

```powershell
python manage.py runserver
```

أو بدون تفعيل البيئة:
```powershell
..\venv\Scripts\python.exe manage.py runserver
```

---

## 🌐 الوصول إلى الـ API

بعد تشغيل الخادم، سيكون متاحاً على:

### 🔗 الروابط الأساسية:

1. **API Root (قائمة جميع الـ APIs):**
   ```
   http://127.0.0.1:8000/api/
   ```
   أو
   ```
   http://localhost:8000/api/
   ```

2. **Admin Panel:**
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## 📡 عرض الـ API في المتصفح

### الطريقة 1: فتح API Root مباشرة
1. افتح المتصفح (Chrome, Firefox, Edge)
2. اذهب إلى: `http://127.0.0.1:8000/api/`
3. سترى قائمة بجميع الـ endpoints المتاحة

### الطريقة 2: استخدام Postman أو Thunder Client
- استورد الـ endpoints من ملف `API_DOCUMENTATION.md`
- استخدم Base URL: `http://127.0.0.1:8000`

### الطريقة 3: استخدام curl في Terminal
```powershell
# عرض API Root
Invoke-WebRequest -Uri http://127.0.0.1:8000/api/ | Select-Object -ExpandProperty Content

# أو
curl http://127.0.0.1:8000/api/
```

---

## 🧪 اختبار الـ API

### مثال: عرض جميع المنتجات
```
GET http://127.0.0.1:8000/api/products/
```

### مثال: عرض جميع الفئات
```
GET http://127.0.0.1:8000/api/categories/
```

### مثال: تسجيل مستخدم جديد
```
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "test123456",
  "password2": "test123456"
}
```

---

## 📚 التوثيق الكامل

راجع ملف `API_DOCUMENTATION.md` للحصول على:
- جميع الـ endpoints (43 API)
- أمثلة على الـ requests
- معلومات المصادقة (JWT)
- تفاصيل كل endpoint

---

## ⚠️ ملاحظات مهمة

1. **الخادم يعمل على المنفذ 8000** (افتراضي)
2. **لإيقاف الخادم:** اضغط `Ctrl + C` في Terminal
3. **للتأكد من أن الخادم يعمل:** افتح `http://127.0.0.1:8000/api/` في المتصفح
4. **إذا كان المنفذ 8000 مستخدم:** استخدم منفذ آخر:
   ```powershell
   python manage.py runserver 8001
   ```

---

## 🔧 استكشاف الأخطاء

### المشكلة: الخادم لا يعمل
```powershell
# تأكد من تفعيل البيئة الافتراضية
.\venv\Scripts\Activate.ps1

# تأكد من وجود جميع المكتبات
pip install -r requirements.txt

# قم بتشغيل migrations
python manage.py migrate
```

### المشكلة: خطأ في PowerShell Execution Policy
```powershell
# قم بتشغيل PowerShell كمسؤول ثم:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## ✅ التحقق من أن كل شيء يعمل

1. ✅ الخادم يعمل (لا توجد أخطاء في Terminal)
2. ✅ يمكنك فتح `http://127.0.0.1:8000/api/` في المتصفح
3. ✅ ترى JSON response مع قائمة الـ endpoints

**الآن المشروع جاهز للاستخدام! 🎉**
