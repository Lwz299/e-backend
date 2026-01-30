# 🔐 Environment Variables - دليل شامل

## ✅ ما تم إعداده

### 1. **python-decouple** ✓
- موجود في `requirements.txt`
- تم إضافته إلى `settings.py`

### 2. **ملف .env.example** ✓
- تم إنشاؤه كقالب
- يحتوي على جميع المتغيرات المطلوبة

### 3. **تحديث settings.py** ✓
- `SECRET_KEY` من environment variable
- `DEBUG` من environment variable
- `ALLOWED_HOSTS` من environment variable
- `DATABASE_URL` من environment variable

---

## 📋 Environment Variables المطلوبة

### للـ Development (محلي):

أنشئ ملف `.env` في مجلد `backend/`:

```env
SECRET_KEY=django-insecure-4-ni-p+y*w8$-p&_$aw-qkl)4ighflq33o+)4do090@v_9tdv2
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*
DATABASE_URL=
```

### للـ Production (Railway):

في Railway Dashboard → Settings → Variables، أضف:

```
SECRET_KEY=<أنشئ مفتاح جديد>
DEBUG=False
ALLOWED_HOSTS=e-backend-production-0a0c.up.railway.app,*.railway.app
DATABASE_URL=<سيتم إضافته تلقائياً من PostgreSQL>
```

---

## 🔑 إنشاء SECRET_KEY جديد

### في Python:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### أو في Terminal:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📝 خطوات الإعداد

### 1. للـ Development (محلي):

```powershell
# 1. انسخ ملف .env.example
cd "C:\Users\Windows 11\Downloads\MA\MA\backend"
copy .env.example .env

# 2. عدّل ملف .env بالقيم المناسبة
# (افتح .env في محرر النصوص)
```

### 2. للـ Production (Railway):

1. اذهب إلى Railway Dashboard
2. Settings → Variables
3. أضف المتغيرات التالية:

| Variable | Value | ملاحظات |
|----------|-------|----------|
| `SECRET_KEY` | `<مفتاح جديد>` | أنشئه من Python |
| `DEBUG` | `False` | مهم للـ production |
| `ALLOWED_HOSTS` | `e-backend-production-0a0c.up.railway.app,*.railway.app` | Railway URLs |
| `DATABASE_URL` | `<تلقائي>` | من PostgreSQL addon |

---

## 🔒 الأمان

### ⚠️ مهم جداً:

1. **لا ترفع ملف `.env` على GitHub!**
   - `.gitignore` يتجاهله تلقائياً
   - `.env.example` فقط للرفع (بدون قيم حقيقية)

2. **في Production:**
   - استخدم `DEBUG=False`
   - استخدم `SECRET_KEY` قوي
   - حدد `ALLOWED_HOSTS` بدقة

3. **لا تشارك `.env` مع أحد!**

---

## 🧪 اختبار Environment Variables

### محلياً:

```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA\backend"
python manage.py check
```

إذا كانت environment variables صحيحة، لن تظهر أخطاء.

### على Railway:

```bash
railway run python manage.py check
```

---

## 📋 Checklist

- [x] `python-decouple` في `requirements.txt`
- [x] `settings.py` يستخدم `config()`
- [x] `.env.example` موجود
- [x] `.gitignore` يتجاهل `.env`
- [ ] ملف `.env` محلي (أنشئه من `.env.example`)
- [ ] Environment variables في Railway

---

## 🐛 استكشاف الأخطاء

### المشكلة: "SECRET_KEY not found"
**الحل:** 
- تأكد من وجود `.env` محلياً
- أو أضف `SECRET_KEY` في Railway variables

### المشكلة: "DEBUG is not a boolean"
**الحل:** 
- استخدم `True` أو `False` (بدون quotes)
- أو `1` / `0`

### المشكلة: "ALLOWED_HOSTS error"
**الحل:**
- استخدم format: `host1,host2,host3`
- بدون spaces بعد الفواصل

---

## 📚 المراجع

- [python-decouple Documentation](https://github.com/henriquebastos/python-decouple)
- [Django Environment Variables](https://docs.djangoproject.com/en/stable/topics/settings/#using-environment-variables)

---

## ✅ الخلاصة

**الآن المشروع يستخدم Environment Variables بشكل صحيح!**

- ✅ آمن (لا توجد قيم حساسة في الكود)
- ✅ مرن (سهل التغيير بين Development و Production)
- ✅ جاهز للـ Production

**لا تنسَ:**
1. أنشئ `.env` من `.env.example` محلياً
2. أضف Environment Variables في Railway
