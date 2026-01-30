# 🔐 Railway Environment Variables - Final

## 📋 جميع Environment Variables المطلوبة

انسخ هذه القيم وأضفها في Railway Dashboard → Settings → Variables:

---

### 1. SECRET_KEY (مطلوب - أنشئ مفتاح جديد)
```
SECRET_KEY=<أنشئ مفتاح جديد>
```

**لإنشاء SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### 2. DEBUG (مطلوب)
```
DEBUG=False
```

---

### 3. ALLOWED_HOSTS (مطلوب)
```
ALLOWED_HOSTS=e-backend-production-0a2d.up.railway.app,*.railway.app
```

---

### 4. DATABASE_URL (تلقائي من Railway - أو يدوياً)
```
DATABASE_URL=postgresql://postgres:zATuXsUdBavsPssZUZliHhXgftXsQljH@yamanote.proxy.rlwy.net:34363/railway
```

**ملاحظة:** Railway يضيف هذا تلقائياً من PostgreSQL service، لكن يمكنك إضافته يدوياً.

---

### 5. CSRF_TRUSTED_ORIGINS (مطلوب)
```
CSRF_TRUSTED_ORIGINS=https://e-backend-production-0a2d.up.railway.app
```

---

### 6. CORS_ALLOWED_ORIGINS (اختياري - للـ Frontend)
```
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

---

### 7. CORS_ALLOW_ALL_ORIGINS (اختياري)
```
CORS_ALLOW_ALL_ORIGINS=False
```

---

## 🚀 خطوات سريعة

1. **افتح Railway Dashboard**
2. **Settings → Variables**
3. **أضف جميع المتغيرات أعلاه**
4. **احفظ**
5. **انتظر إعادة النشر**

---

## ✅ Checklist

- [ ] `SECRET_KEY` (أنشئ مفتاح جديد)
- [ ] `DEBUG=False`
- [ ] `ALLOWED_HOSTS=e-backend-production-0a2d.up.railway.app,*.railway.app`
- [ ] `DATABASE_URL` (تلقائي أو يدوياً)
- [ ] `CSRF_TRUSTED_ORIGINS=https://e-backend-production-0a2d.up.railway.app`
- [ ] تم إعادة النشر

---

## 🎯 بعد إضافة Environment Variables

المشروع سيعمل تلقائياً:
- ✅ PostgreSQL connection
- ✅ Static files
- ✅ Admin Panel
- ✅ API endpoints
- ✅ CSRF protection

**كل شيء جاهز! 🎉**
