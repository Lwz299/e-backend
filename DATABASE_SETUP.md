# 🗄️ إعداد قاعدة البيانات PostgreSQL

## ✅ رابط قاعدة البيانات من Railway

```
postgres://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway
```

---

## 🔧 كيفية الاستخدام

### 1️⃣ في Railway (Production)

Railway سيقوم تلقائياً بإضافة هذا الرابط كـ `DATABASE_URL` environment variable.

**لا حاجة لفعل شيء!** الإعدادات الحالية ستعمل تلقائياً.

---

### 2️⃣ للاختبار المحلي (اختياري)

إذا أردت اختبار الاتصال محلياً:

#### Windows PowerShell:
```powershell
$env:DATABASE_URL="postgres://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway"
python manage.py migrate
python manage.py runserver
```

#### أو إنشاء ملف `.env`:
```env
DATABASE_URL=postgres://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway
```

ثم في `settings.py` (إذا كنت تستخدم python-decouple):
```python
from decouple import config

DATABASE_URL = config('DATABASE_URL', default=None)
```

---

## 📋 خطوات النشر على Railway

### 1. إضافة Environment Variable في Railway:

1. اذهب إلى Railway Dashboard
2. اختر مشروعك
3. Settings → Variables
4. أضف:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgres://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway`

**ملاحظة:** إذا أضفت PostgreSQL addon في Railway، سيتم إضافة `DATABASE_URL` تلقائياً!

### 2. تشغيل Migrations:

بعد النشر، migrations ستعمل تلقائياً بفضل `Procfile`:
```
release: python manage.py migrate --noinput
```

أو يدوياً من Railway CLI:
```bash
railway run python manage.py migrate
```

### 3. إنشاء Superuser:

```bash
railway run python manage.py createsuperuser
```

---

## ✅ التحقق من الاتصال

### اختبار الاتصال من Python:

```python
python manage.py dbshell
```

أو:

```python
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())
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

## 📝 ملاحظات

1. **الإعدادات الحالية:** المشروع جاهز للعمل مع PostgreSQL تلقائياً
2. **Migrations:** ستعمل تلقائياً عند النشر بفضل `Procfile`
3. **Backup:** Railway يقوم بعمل backup تلقائي، لكن يمكنك إضافة backup يدوي
4. **Performance:** PostgreSQL أفضل بكثير من SQLite للـ production

---

## ✅ Checklist

- [x] رابط قاعدة البيانات جاهز
- [x] `DATABASE_URL` في Railway environment variables
- [x] `Procfile` يحتوي على migrations
- [x] `dj-database-url` في `requirements.txt`
- [ ] Migrations تم تشغيلها
- [ ] Superuser تم إنشاؤه
- [ ] تم اختبار الاتصال

**قاعدة البيانات جاهزة للاستخدام! 🎉**
