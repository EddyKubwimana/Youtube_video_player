import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "youtube",
        version = "0.1",
        description = "Personal",
        options = {"build_exe": {"packages":["os"], "include_files":["youtube.py"]}},
        executables = [Executable("youtube.py", base=base)])
