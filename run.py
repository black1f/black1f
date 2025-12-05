#!/usr/bin/env python3
import marshal, types, os, sys

def find_pyc():
    # البحث عن أول ملف ينتهي بـ pyc
    for f in os.listdir("."):
        if f.endswith(".pyc"):
            return f
    return None

def run_pyc():
    filename = find_pyc()
    if not filename:
        print("❌ ملف pyc غير موجود")
        sys.exit(1)

    with open(filename, "rb") as f:
        data = f.read()

    # تخطي 16 بايت الأولى (Header)
    code = marshal.loads(data[16:])

    module = types.ModuleType("__main__")
    exec(code, module.__dict__)

run_pyc()
