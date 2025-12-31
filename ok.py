#!/usr/bin/env python3
import sys
import os

# تشغيل مباشر
try:
    import ss
    if hasattr(ss, 'main'):
        ss.main()
    elif hasattr(ss, '__main__'):
        ss.__main__()
except Exception as e:
    print(f"خطأ: {e}")
