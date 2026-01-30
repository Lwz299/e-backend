# 🚀 كيفية تشغيل Scripts إنشاء Superuser

## ⚠️ المشكلة: Windows يطلب اختيار برنامج

هذا يحدث لأن Windows لا يعرف كيفية تشغيل ملفات `.py` مباشرة.

---

## ✅ الحل: استخدام Terminal/PowerShell

### الطريقة 1: تشغيل محلي (للاختبار)

#### في PowerShell:

```powershell
# 1. الانتقال إلى مجلد المشروع
cd "C:\Users\Windows 11\Downloads\MA\MA"

# 2. تفعيل البيئة الافتراضية
.\venv\Scripts\Activate.ps1

# 3. الانتقال إلى مجلد backend
cd backend

# 4. تشغيل السكربت
python create_superuser.py
```

أو للـ interactive:

```powershell
python create_superuser_interactive.py
```

---

### الطريقة 2: استخدام Django Management Command (الأسهل)

```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA"
.\venv\Scripts\Activate.ps1
cd backend
python manage.py createsuperuser
```

---

### الطريقة 3: تشغيل على Railway مباشرة (للـ Production)

#### بدون SSH:

```bash
railway run --project=1c4c4c30-692e-419b-927d-70c34fb39a4d python manage.py createsuperuser
```

#### مع SSH:

```bash
railway ssh --project=1c4c4c30-692e-419b-927d-70c34fb39a4d --environment=be115a9a-553a-4b38-af76-e4aeb5329b07 --service=5cc8883c-56d0-47ee-a8d1-79c32a7cc367
python manage.py createsuperuser
```

---

## 📝 خطوات مفصلة للـ PowerShell

### الخطوة 1: فتح PowerShell
- اضغط `Win + X`
- اختر "Windows PowerShell" أو "Terminal"

### الخطوة 2: الانتقال إلى المشروع
```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA\backend"
```

### الخطوة 3: تفعيل البيئة الافتراضية
```powershell
..\venv\Scripts\Activate.ps1
```

إذا واجهت مشكلة Execution Policy:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
..\venv\Scripts\Activate.ps1
```

### الخطوة 4: تشغيل الأمر
```powershell
python manage.py createsuperuser
```

---

## 🎯 الأوامر السريعة (Copy & Paste)

### للاختبار المحلي:
```powershell
cd "C:\Users\Windows 11\Downloads\MA\MA"; .\venv\Scripts\Activate.ps1; cd backend; python manage.py createsuperuser
```

### للـ Production على Railway:
```bash
railway run --project=1c4c4c30-692e-419b-927d-70c34fb39a4d python manage.py createsuperuser
```

---

## ⚙️ إصلاح مشكلة "اختيار البرنامج" في Windows

### الحل الدائم:

1. افتح "Settings" → "Apps" → "Default apps"
2. ابحث عن "Python" أو "Python Launcher"
3. أو قم بتثبيت Python من [python.org](https://www.python.org)

### الحل المؤقت:

استخدم PowerShell/Terminal دائماً بدلاً من النقر المزدوج على الملف.

---

## 🔍 التحقق من أن Python يعمل

```powershell
python --version
```

يجب أن يظهر:
```
Python 3.14.2
```

---

## ✅ الخلاصة

**لا تنقر على ملف `.py` مباشرة!**

استخدم PowerShell/Terminal:
```powershell
python manage.py createsuperuser
```

أو على Railway:
```bash
railway run --project=1c4c4c30-692e-419b-927d-70c34fb39a4d python manage.py createsuperuser
```
