"""
Fem illustration: 0.0.4

Your first GUI application - the top level window
Adding some widgets

@Tkinter GUI Application Development
"""
__author__ = 'F. Jimenez Mucho'
__title__= 'Structural Analysis Matrix, InEs-v0.0.4'
__date__ = '06/12/2018'
__version__ = '0.0.4'
__license__ = 'GNU GPLv3'


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
        import tkinter.messagebox as msg
    except ImportError:
        raise ImportError("Se requiere el modulo ...")

# Constante
PROGRAM_NAME  = "Structural Analysis Matrix, InEs" 
FILE_ICO_LOGO = "styde.ico"


class AppFem(tk.Tk): 
    __winSize=  '700x400+0+0'
    __winSizeX, __winSizeY= 300, 230
    __winBackgroundColor="#ccc"
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry(self.__winSize)
        self.minsize(self.__winSizeX,self.__winSizeY)
        self.config(bg=self.__winBackgroundColor)

        self.initUI()

    def initUI(self):

        self.checkedMenuBar = tk.BooleanVar()
        self.checkedMenuBar.trace("w", self.onDeverlopment)
        self.checkedToolBar = tk.BooleanVar()
        self.checkedToolBar.trace("w", self.onDeverlopment)
        self.checkedSideBar = tk.BooleanVar()
        self.checkedSideBar.trace("w", self.onDeverlopment)
        self.checkedStatusBar = tk.BooleanVar()
        self.checkedStatusBar.trace("w", self.onDeverlopment)
        self.checkedConsole = tk.BooleanVar()
        self.checkedConsole.trace("w", self.onDeverlopment)



        self.menuBar = tk.Menu(self)  # menu begins

        self.file_menu = tk.Menu(self.menuBar, tearoff=0)
        self.file_menu.add_command(label="New file", accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save as...", accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit - Exit", accelerator="Ctrl-Q", command=self.destroy)
        
        self.edit_menu = tk.Menu(self.menuBar, tearoff=0)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V")
        
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
        self.tools_menu.add_command(label="Build", accelerator="Ctrl+B")
        self.tools_menu.add_command(label="Cancel Build", accelerator="Ctrl+Break")
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
        self.help_menu.add_command(label="About", command=self.onDeverlopment)

        self.menuBar.add_cascade(label='File', menu=self.file_menu)
        self.menuBar.add_cascade(label='Edit', menu=self.edit_menu)
        self.menuBar.add_cascade(label='View', menu=self.view_menu)
        self.menuBar.add_cascade(label='tools', menu=self.tools_menu)
        self.menuBar.add_cascade(label='prefereces', menu=self.prefereces_menu)
        self.menuBar.add_cascade(label='help', menu=self.help_menu)
        self.config(menu=self.menuBar)  # menu ends

        # ------------command:comandos - key:teclado----------------
        ## File
        self.bind("<Control-n>", lambda event: self.onDeverlopment())
        self.bind("<Control-N>", lambda event: self.onDeverlopment())
        self.bind("<Control-o>", lambda event: self.onDeverlopment())
        self.bind("<Control-O>", lambda event: self.onDeverlopment())
        self.bind("<Control-s>", lambda event: self.onDeverlopment())
        self.bind("<Control-S>", lambda event: self.onDeverlopment())
        self.bind("<Control-q>", lambda event: self.onDeverlopment())
        self.bind("<Control-Q>", lambda event: self.onDeverlopment())
        ## Edit
        self.bind("<Control-c>", lambda event: self.onDeverlopment())
        self.bind("<Control-C>", lambda event: self.onDeverlopment())
        
        self.bind("<Control-b>", lambda event: self.onDeverlopment())
        self.bind("<Control-B>", lambda event: self.onDeverlopment())

    def onDeverlopment(self, *args):
        print('falta implementar checkeds...')
        msg.showinfo('Información',message='No esta implementado por completo ....')


def main():
    ventana=AppFem()
    ventana.mainloop()

if __name__ == '__main__':
    main()