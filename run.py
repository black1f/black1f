
import sys
import importlib.util
import os
from pathlib import Path

# تحديد مسار pyc
pyc_path = Path(__file__).parent / "__pycache__" / "snsnsnd.cpython-312.pyc"

if not pyc_path.exists():
    print("❌ ملف pyc غير موجود")
    exit()

# تحميل الملف كـ module
spec = importlib.util.spec_from_file_location("snsnsnd", pyc_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# تشغيل الدالة main() داخل ملفك
if hasattr(module, "main"):
    module.main()
else:
    print("⚠ ملفك لا يحتوي على دالة main()")
