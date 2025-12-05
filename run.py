
import snsnsnd

try:
    snsnsnd.main()
except AttributeError:
    print("⚠ ملف .so لا يحتوي دالة main()… شغّل الدالة المناسبة بنفسك.")
