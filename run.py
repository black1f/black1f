#!/usr/bin/env python3
import sys
import os

# طريقة تشغيل A.so من home (حيث يعمل)
os.chdir(os.path.expanduser('~'))
sys.path.insert(0, '.')

try:
    # استورد الملف المشفر
    import A
    
    # اطبع تأكيد
    print("✅ تم تحميل A.so بنجاح")
    
    # شغّل السكربت الحقيقي
    if hasattr(A, 'main'):
        A.main()
    elif hasattr(A, 'run'):
        A.run()
    else:
        print("⚠️ لا توجد دالة main أو run")
        print("🔍 الدوال المتاحة:", [x for x in dir(A) if not x.startswith('__')])
        
except Exception as e:
    print(f"❌ خطأ: {e}")
    print("🔄 تشغيل A.py مباشرة كبديل...")
    
    # كبديل، شغّل A.py
    if os.path.exists('/storage/emulated/0/CP/A.py'):
        with open('/storage/emulated/0/CP/A.py', 'r') as f:
            exec(f.read())
