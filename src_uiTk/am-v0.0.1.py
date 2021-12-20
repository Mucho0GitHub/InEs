"""
Fem illustration: 0.0.1

Your first GUI application - refactoring main window

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
__date__ = '06/12/2018'
PROGRAM_NAME  = "Análisis matricial - InEs" 
FILE_ICO_LOGO = "styde.ico"


class AppFem(tk.Tk):   
    __winSize =  '700x400+3+3'
    
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry(self.__winSize)
        
        self.minsize(300,230)
        self.config(bg="#ccc")

def vmain():
    ventana=AppFem()
    ventana.mainloop()

if __name__ == '__main__':
    vmain()