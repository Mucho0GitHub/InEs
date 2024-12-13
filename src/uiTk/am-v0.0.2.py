"""
Fem illustration: 0.0.2

Your first GUI application - the menubar adding main window

@Tkinter GUI Application Development
"""

import sys
PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter
    except ImportError:
        raise ImportError("Se requiere el modulo ...")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo ...")

# Constante
PROGRAM_NAME  = "Structural Analysis Matrix, fem" 
FILE_ICO_LOGO = "styde.ico"


class AppFem(tk.Tk): 
    __WINSize=  '700x400+0+0'
    __WINSizeX, __WINSizeY= 300, 230
    __WINBackgroundColor="#ccc"
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry(self.__WINSize)
        self.minsize(self.__WINSizeX,self.__WINSizeY)
        self.config(bg=self.__WINBackgroundColor)

        self.initUI()

    def initUI(self):
        self.menuBar = tk.Menu(self)  # menu begins

        self.file_menu = tk.Menu(self.menuBar, tearoff=0)
        # all file menu-items will be added here next
        self.menuBar.add_cascade(label='File', menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menuBar, tearoff=0)
        # all edit menu-items will be added here next
        self.menuBar.add_cascade(label='Edit', menu=self.edit_menu)

        self.view_menu = tk.Menu(self.menuBar, tearoff=0)
        # all view menu-items will be added here next
        self.menuBar.add_cascade(label='View', menu=self.view_menu)

        self.tools_menu = tk.Menu(self.menuBar, tearoff=0)
        # all tools menu-items will be added here next
        self.menuBar.add_cascade(label='tools', menu=self.tools_menu)

        self.prefereces_menu = tk.Menu(self.menuBar, tearoff=0)
        # all prefereces menu-items will be added here next
        self.menuBar.add_cascade(label='prefereces', menu=self.prefereces_menu)

        self.help_menu = tk.Menu(self.menuBar, tearoff=0)
        # all help menu-items will be added here next
        self.menuBar.add_cascade(label='help',  menu=self.help_menu)

        self.config(menu=self.menuBar)  # menu ends    

def main():
    ventana=AppFem()
    ventana.mainloop()

if __name__ == '__main__':
    main()