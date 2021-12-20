"""
Fem illustration: 0.0.2

Your first GUI application - the adding submenu to menubar in main window

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
PROGRAM_NAME  = "Structural Analysis Matrix, fem" 
FILE_ICO_LOGO = "styde.ico"


class AppFem(tk.Tk): 
    WINSize=  '700x400+0+0'
    WINSizeX, WINSizeY= 300, 230
    WINBackgroundColor="#ccc"
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry(self.WINSize)
        self.minsize(self.WINSizeX,self.WINSizeY)
        self.config(bg=self.WINBackgroundColor)

        self.initUI()
        
    def initUI(self):

        self.checkedMenuBar = tk.BooleanVar()
        self.checkedMenuBar.trace("w", self.mark_checked)
        self.checkedToolBar = tk.BooleanVar()
        self.checkedToolBar.trace("w", self.mark_checked)
        self.checkedSideBar = tk.BooleanVar()
        self.checkedSideBar.trace("w", self.mark_checked)
        self.checkedStatusBar = tk.BooleanVar()
        self.checkedStatusBar.trace("w", self.mark_checked)
        self.checkedConsole = tk.BooleanVar()
        self.checkedConsole.trace("w", self.mark_checked)
        

        self.menuBar = tk.Menu(self)  # menu begins

        self.file_menu = tk.Menu(self.menuBar, tearoff=0)
        self.file_menu.add_command(label="New file")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save as...")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit - Exit", command=self.destroy)
        
        self.edit_menu = tk.Menu(self.menuBar, tearoff=0)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Paste")
        
        self.view_menu = tk.Menu(self.menuBar, tearoff=0)
        self.view_menu.add_checkbutton(label="Show Menu", onvalue=True,
                                offvalue=False, variable=self.checkedMenuBar)
        self.view_menu.add_checkbutton(label="Show toolbar", onvalue=True,
                                offvalue=False, variable=self.checkedToolBar)
        self.view_menu.add_checkbutton(label="Show Side bar", onvalue=True,
                                offvalue=False, variable=self.checkedSideBar)
        self.view_menu.add_checkbutton(label="Show Status bar", onvalue=True,
                                offvalue=False, variable=self.checkedStatusBar)
        self.view_menu.add_checkbutton(label="Show Console", onvalue=True,
                                offvalue=False, variable=self.checkedConsole)
        self.view_menu.add_checkbutton(label="Show Command UIConsole Only")
        self.view_menu.add_separator()
        
        self.tools_menu = tk.Menu(self.menuBar, tearoff=0)
        self.tools_menu.add_command(label="Command Palette...")
        self.tools_menu.add_command(label="Build")
        self.tools_menu.add_command(label="Cancel Build")
        self.tools_menu.add_command(label="Build Results")
        self.tools_menu.add_command(label="Save Build Results")
        self.tools_menu.add_separator()
        self.tools_menu.add_command(label="Macros")
        
        
        self.prefereces_menu = tk.Menu(self.menuBar, tearoff=0)
        self.prefereces_menu.add_command(label="Settings - Default")
        self.prefereces_menu.add_command(label="Settings - User")
        self.prefereces_menu.add_separator()
        self.prefereces_menu.add_command(label="Color Scheme...")
        self.prefereces_menu.add_command(label="Theme...")
        self.prefereces_menu.add_separator()
        self.prefereces_menu.add_command(label="Package Control")

        self.help_menu = tk.Menu(self.menuBar, tearoff=0)
        self.help_menu.add_command(label="Documentation")
        self.help_menu.add_command(label="Twitter")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Update Licence")
        self.help_menu.add_command(label="Remove Licence")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Changelog Calendar...")
        self.help_menu.add_command(label="About")

        self.menuBar.add_cascade(label='File', menu=self.file_menu)
        self.menuBar.add_cascade(label='Edit', menu=self.edit_menu)
        self.menuBar.add_cascade(label='View', menu=self.view_menu)
        self.menuBar.add_cascade(label='tools', menu=self.tools_menu)
        self.menuBar.add_cascade(label='prefereces', menu=self.prefereces_menu)
        self.menuBar.add_cascade(label='help', menu=self.help_menu)
        self.config(menu=self.menuBar)  # menu ends

    def mark_checked(self, *args):
        print('falta implementar checkeds...')


def main():
    ventana=AppFem()
    ventana.mainloop()

if __name__ == '__main__':
    main()