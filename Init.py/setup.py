import sys
import os
from cx_Freeze import setup, Executable

# Reemplaza "nombre_script.py" con el nombre de tu archivo de script principal
script = 'run.py'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Reemplaza "NombreApp" con el nombre de tu aplicación
setup(
    name="IteraCopy",
    version="1.0",
    description="Descripción de la aplicación",
    options={
        'build_exe': {
            'include_files': [
                (os.path.dirname(sys.executable) + "/DLLs/tcl86t.dll", "tcl86t.dll"),
                (os.path.dirname(sys.executable) + "/DLLs/tk86t.dll", "tk86t.dll")
            ],
        },
    },
    executables=[
        Executable(script, base=base, icon="escarabajop.ico", target_name='IteraCopy')
    ]
)