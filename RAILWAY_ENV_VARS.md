# 🔐 Environment Variables المطلوبة في Railway

## ⚠️ مشكلة CSRF - الحل النهائي

إذا كنت تواجه مشكلة:
```
Origin checking failed - https://e-backend-production-0a0c.up.railway.app does not match any trusted origins.
```

## ✅ Environment Variables المطلوبة

في Railway Dashboard → Settings → Variables، أضف:

### 1. CSRF_TRUSTED_ORIGINS (مهم جداً!)
```
Name: CSRF_TRUSTED_ORIGINS
Value: https://e-backend-production-0a0c.up.railway.app
```

### 2. DEBUG (يجب أن يكون False في Production)
```
Name: DEBUG
Value: False
```

### 3. SECRET_KEY
```
Name: SECRET_KEY
Value: <أنشئ مفتاح جديد>
```

لإنشاء SECRET_KEY جديد:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. ALLOWED_HOSTS
```
Name: ALLOWED_HOSTS
Value: e-backend-production-0a0c.up.railway.app,*.railway.app
```

### 5. DATABASE_URL (تلقائي من PostgreSQL)
```
Name: DATABASE_URL
Value: postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@ballast.proxy.rlwy.net:10091/railway
```

---

## 📋 Checklist كامل

- [ ] `CSRF_TRUSTED_ORIGINS` = `https://e-backend-production-0a0c.up.railway.app`
- [ ] `DEBUG` = `False`
- [ ] `SECRET_KEY` = `<مفتاح جديد>`
- [ ] `ALLOWED_HOSTS` = `e-backend-production-0a0c.up.railway.app,*.railway.app`
- [ ] `DATABASE_URL` = `<رابط PostgreSQL>`

---

## 🚀 بعد إضافة Environment Variables

1. **احفظ** Environment Variables
2. **انتظر** إعادة النشر التلقائي (أو اضغط Redeploy)
3. **اختبر** Admin Panel: https://e-backend-production-0a0c.up.railway.app/admin/

---

## 🔍 التحقق من الإعدادات

بعد إضافة Environment Variables، يمكنك التحقق:

```bash
railway run python manage.py shell
```

ثم في Python shell:
```python
from django.conf import settings
print("CSRF_TRUSTED_ORIGINS:", settings.CSRF_TRUSTED_ORIGINS)
print("DEBUG:", settings.DEBUG)
print("ALLOWED_HOSTS:", settings.ALLOWED_HOSTS)
```

---

## ⚠️ ملاحظات مهمة

1. **DEBUG = True في Production:**
   - الرسالة تقول أن `DEBUG = True`
   - يجب تغييره إلى `False` في Railway Environment Variables
   - هذا مهم جداً للأمان!

2. **Format CSRF_TRUSTED_ORIGINS:**
   - استخدم format: `https://e-backend-production-0a0c.up.railway.app`
   - بدون spaces
   - يجب أن يبدأ بـ `https://`

3. **بعد التحديث:**
   - Railway يحتاج إعادة نشر
   - انتظر حتى يعيد النشر تلقائياً (عادة 1-2 دقيقة)

---

## 🐛 إذا استمرت المشكلة

### 1. تحقق من Environment Variables:
- تأكد من أن جميع المتغيرات موجودة
- تأكد من القيم صحيحة (بدون spaces إضافية)

### 2. إعادة نشر يدوي:
- في Railway Dashboard → Deployments
- اضغط "Redeploy"

### 3. تحقق من Logs:
- في Railway Dashboard → Deployments → View Logs
- ابحث عن أخطاء

---

## ✅ بعد الإصلاح

- ✅ CSRF errors ستختفي
- ✅ Admin Panel سيعمل
- ✅ جميع POST requests ستعمل
- ✅ المشروع آمن (DEBUG=False)

**المشروع جاهز! 🎉**
