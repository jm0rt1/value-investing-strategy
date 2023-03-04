import sys
from setuptools import setup

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="value-investing-strategy",
    version="0.1",
    description="",
    author="James Mortensen",
    autho_email="jmortens@syr.edu",
    url="https://github.com/jm0rt1/CSE682-Project"
)
