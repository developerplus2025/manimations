from cx_Freeze import setup, Executable

setup(
    name="ToolForMath",
    version="1.0",
    description="CMATH",
    executables=[Executable("script.py")]
)
