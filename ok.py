#!/usr/bin/env python3
import os, sys, shutil, zipfile
MODULE_NAME = "ss"
ZIP_NAME = "ss.zip"
def main():
    try:
        curr = os.path.dirname(os.path.abspath(__file__))
        home = os.environ.get("HOME", "/data/data/com.termux/files/home")
        run_dir = os.path.join(home, f".{MODULE_NAME}_safe")
        if not os.path.exists(run_dir): os.makedirs(run_dir)
        zip_path = os.path.join(curr, ZIP_NAME)
        if not os.path.exists(zip_path): return
        with zipfile.ZipFile(zip_path, 'r') as z: z.extractall(run_dir)
        sys.path.insert(0, run_dir)
        os.chdir(run_dir)
        import ss
        if hasattr(ss, "main"): ss.main()
        elif hasattr(ss, "__main__"): ss.__main__()
    except Exception as e: print(f"Error: {e}")
if __name__ == "__main__": main()
