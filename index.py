import tkinter as tk
from idlelib.percolator import Percolator
import idlelib.colorizer as ic

main = tk.Tk()
text = tk.Text(main)
main.title("Syntax Highlighting")
text.pack()
Percolator(text).insertfilter(ic.ColorDelegator())
main.mainloop()