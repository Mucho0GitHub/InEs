# ***********************************
#  Author: F. Jimenez Mucho.
#  E-mail: fjmucho@gmail.com 
#  License: MIT License
#  Date: '06/12/2018'
# ***********************************
"""
Fem illustration: 0.0.0

Your first GUI application - create window ui

@Tkinter GUI Application Development
"""
import sys

PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo ...")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo ...")

# Constante
PROGRAM_NAME  = "Análisis matricial - InEs"
FILE_ICO_LOGO = "styde.ico"

class AppFem(tk.Tk):   
    def __init__(self):
        super(AppFem, self).__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry('700x400+3+3')

if __name__ == '__main__':
    ventana=AppFem()
    ventana.mainloop()