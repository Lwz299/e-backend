# 🚂 دليل النشر على Railway

## ✅ ما تم إعداده

### 1. **Procfile** ✓
تم إنشاء `Procfile` في جذر المشروع (نفس مكان `manage.py`):
```
web: gunicorn backend.wsgi --log-file -
```

### 2. **Gunicorn** ✓
تم تثبيت `gunicorn` وإضافته إلى `requirements.txt`:
```
gunicorn==24.1.1
```

### 3. **Database Configuration** ✓
تم إعداد `settings.py` لدعم `dj-database-url`:
```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', f'sqlite:///{str(BASE_DIR / "db.sqlite3")}')
    )
}
```

### 4. **ALLOWED_HOSTS** ✓
```python
ALLOWED_HOSTS = ['*']  # مؤقت للاختبار
```

---

## 🚀 خطوات النشر على Railway

### 1️⃣ رفع المشروع على GitHub

```bash
git init
git add .
git commit -m "Initial commit - Ready for Railway deployment"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

**ملاحظة مهمة:** تأكد من إضافة `.gitignore` لتجاهل:
- `venv/`
- `__pycache__/`
- `*.pyc`
- `db.sqlite3` (اختياري - يمكنك رفعه أو استخدام PostgreSQL)
- `.env`

### 2️⃣ إنشاء مشروع جديد على Railway

1. اذهب إلى [railway.app](https://railway.app)
2. سجل دخول بحساب GitHub
3. اضغط على **"New Project"**
4. اختر **"Deploy from GitHub repo"**
5. اختر المستودع الخاص بك

### 3️⃣ إعداد قاعدة البيانات (PostgreSQL)

1. في Railway dashboard، اضغط على **"+ New"**
2. اختر **"Database"** → **"Add PostgreSQL"**
3. Railway سيقوم تلقائياً بإنشاء `DATABASE_URL` environment variable

### 4️⃣ إعداد Environment Variables

في Railway dashboard → Settings → Variables، أضف:

```
DATABASE_URL=<سيتم تعيينه تلقائياً من PostgreSQL>
SECRET_KEY=<أنشئ مفتاح سري جديد>
DEBUG=False
```

**لإنشاء SECRET_KEY جديد:**
```python
# في Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5️⃣ إعداد Root Directory (مهم!)

إذا كان المشروع في مجلد `backend` داخل المستودع:

1. في Railway dashboard → Settings → Service
2. اضغط على **"Settings"** → **"Root Directory"**
3. أدخل: `backend`

### 6️⃣ تشغيل Migrations

في Railway dashboard → Deployments → View Logs، سترى أن Railway يشغل:
- `pip install -r requirements.txt`
- `gunicorn backend.wsgi`

**لإضافة migrations تلقائياً:**

أضف ملف `railway.json` في جذر المشروع:
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && gunicorn backend.wsgi --log-file -",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

أو يمكنك إضافة migrations في `Procfile`:
```
release: python manage.py migrate
web: gunicorn backend.wsgi --log-file -
```

### 7️⃣ إنشاء Superuser

بعد النشر، يمكنك إنشاء superuser من Railway CLI:

```bash
# تثبيت Railway CLI
npm i -g @railway/cli

# تسجيل الدخول
railway login

# ربط المشروع
railway link

# إنشاء superuser
railway run python manage.py createsuperuser
```

أو من Railway dashboard → Deployments → يمكنك فتح shell وتشغيل الأوامر.

---

## 🔧 إعدادات إضافية للـ Production

### تحديث ALLOWED_HOSTS

بعد الحصول على URL من Railway، حدّث `settings.py`:

```python
ALLOWED_HOSTS = [
    'your-app-name.railway.app',
    '*.railway.app',  # للسماح بجميع subdomains
]
```

### تحديث CORS

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
    "https://www.your-frontend-domain.com",
]

CORS_ALLOW_ALL_ORIGINS = False  # مهم للـ production!
```

### Static Files

Railway سيقوم تلقائياً بجمع static files عند الـ build. إذا احتجت:

```bash
python manage.py collectstatic --noinput
```

---

## 📋 Checklist قبل النشر

- [x] `Procfile` موجود في جذر المشروع
- [x] `gunicorn` في `requirements.txt`
- [x] `dj-database-url` في `requirements.txt`
- [x] `DATABASES` config في `settings.py`
- [x] `ALLOWED_HOSTS` محددة
- [ ] `SECRET_KEY` في environment variables
- [ ] `DEBUG=False` في production
- [ ] قاعدة بيانات PostgreSQL مضافة
- [ ] Migrations تم تشغيلها
- [ ] Superuser تم إنشاؤه

---

## 🐛 استكشاف الأخطاء

### المشكلة: "No start command found"
**الحل:** تأكد من وجود `Procfile` في جذر المشروع (نفس مكان `manage.py`)

### المشكلة: "ModuleNotFoundError: No module named 'backend'"
**الحل:** 
- تأكد من Root Directory في Railway Settings
- أو تأكد من أن `Procfile` يستخدم المسار الصحيح: `backend.wsgi`

### المشكلة: Database connection error
**الحل:**
- تأكد من إضافة PostgreSQL addon
- تأكد من وجود `DATABASE_URL` في environment variables

### المشكلة: Static files not found
**الحل:**
- أضف `python manage.py collectstatic --noinput` في build command
- أو استخدم WhiteNoise middleware

---

## 🔗 روابط مفيدة

- [Railway Documentation](https://docs.railway.app)
- [Django on Railway](https://docs.railway.app/guides/django)
- [Gunicorn Documentation](https://docs.gunicorn.org)

---

## ✅ بعد النشر

بعد النشر الناجح، ستحصل على URL مثل:
```
https://your-app-name.railway.app
```

يمكنك الوصول إلى:
- API Root: `https://your-app-name.railway.app/api/`
- Admin Panel: `https://your-app-name.railway.app/admin/`
- Swagger: `https://your-app-name.railway.app/swagger/`

**مبروك! مشروعك الآن على Railway! 🎉**
