# 🗄️ إعداد DATABASE_URL - PostgreSQL

## ✅ رابط قاعدة البيانات

```
postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway
```

---

## 🔧 كيفية الاستخدام

### 1️⃣ في Railway (Production) - تلقائي

Railway سيقوم تلقائياً بإضافة هذا الرابط كـ `DATABASE_URL` environment variable.

**لا حاجة لفعل شيء!** الإعدادات الحالية ستعمل تلقائياً.

---

### 2️⃣ للاختبار المحلي (اختياري)

إذا أردت اختبار الاتصال محلياً:

#### Windows PowerShell:
```powershell
# تعيين DATABASE_URL مؤقتاً
$env:DATABASE_URL="postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway"

# تشغيل migrations
cd "C:\Users\Windows 11\Downloads\MA\MA\backend"
.\..\venv\Scripts\Activate.ps1
python manage.py migrate

# تشغيل السيرفر
python manage.py runserver
```

#### أو إنشاء ملف `.env` محلي:
```env
DATABASE_URL=postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway
```

---

## 📋 إضافة DATABASE_URL في Railway

### الطريقة 1: تلقائي (مُوصى به)
إذا أضفت PostgreSQL addon في Railway:
- Railway ينشئ `DATABASE_URL` تلقائياً
- لا حاجة لإضافة شيء يدوياً

### الطريقة 2: يدوي
1. Railway Dashboard → Settings → Variables
2. أضف Environment Variable:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway`

---

## ✅ التحقق من الإعدادات

الإعدادات الحالية في `settings.py`:

```python
DATABASE_URL = config('DATABASE_URL', default=None)

if DATABASE_URL:
    # Production: استخدام PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Development: استخدام SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

**هذا يعني:**
- ✅ إذا كان `DATABASE_URL` موجود → يستخدم PostgreSQL
- ✅ إذا لم يكن موجود → يستخدم SQLite (Development)

---

## 🧪 اختبار الاتصال

### محلياً (إذا أضفت .env):
```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA\backend"
.\..\venv\Scripts\Activate.ps1
python manage.py dbshell
```

### على Railway:
```bash
railway run python manage.py dbshell
```

---

## 🔒 أمان

**⚠️ مهم:** هذا الرابط يحتوي على:
- **Username:** `postgres`
- **Password:** `zATuXsUdBavsPssZUZliHhXgftXsQljH`
- **Host:** `ballast.proxy.rlwy.net`
- **Port:** `10091`
- **Database:** `railway`

**لا تشارك هذا الرابط علناً!** احتفظ به في:
- Environment Variables في Railway
- ملف `.env` محلي (وأضفه إلى `.gitignore`)

---

## 📝 خطوات النشر على Railway

### 1. إضافة Environment Variable في Railway:

1. اذهب إلى Railway Dashboard
2. Settings → Variables
3. أضف:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway`

**ملاحظة:** إذا أضفت PostgreSQL addon، سيتم إضافة `DATABASE_URL` تلقائياً!

### 2. تشغيل Migrations:

بعد النشر، migrations ستعمل تلقائياً بفضل `Procfile`:
```
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
```

أو يدوياً:
```bash
railway run python manage.py migrate
```

### 3. إنشاء Superuser:

```bash
railway run python manage.py createsuperuser
```

---

## 🐛 استكشاف الأخطاء

### المشكلة: "could not connect to server"
**الحل:**
- تأكد من أن Railway PostgreSQL service يعمل
- تأكد من أن `DATABASE_URL` موجود في environment variables
- تحقق من firewall settings في Railway

### المشكلة: "database does not exist"
**الحل:**
- Railway ينشئ قاعدة البيانات تلقائياً
- إذا لم تكن موجودة، أنشئها يدوياً أو أعد إنشاء PostgreSQL service

### المشكلة: "password authentication failed"
**الحل:**
- تأكد من أن الرابط صحيح
- تحقق من أن كلمة المرور لم تتغير في Railway

---

## ✅ Checklist

- [x] رابط قاعدة البيانات جاهز
- [x] `DATABASE_URL` في Railway environment variables
- [x] `dj-database-url` في `requirements.txt`
- [x] `settings.py` مضبوط لاستخدام `DATABASE_URL`
- [ ] Migrations تم تشغيلها
- [ ] Superuser تم إنشاؤه
- [ ] تم اختبار الاتصال

---

## 🎉 الخلاصة

**قاعدة البيانات جاهزة للاستخدام!**

- ✅ الإعدادات صحيحة
- ✅ ستعمل تلقائياً مع `DATABASE_URL`
- ✅ في Railway: أضف `DATABASE_URL` في Environment Variables
- ✅ في Development: يمكنك استخدام SQLite أو PostgreSQL

**المشروع جاهز! 🚀**
