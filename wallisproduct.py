import tkinter as tk

def wallisProduct(n):
    if n == 1:
        return 4 / 3
    return wallisProduct(n-1) * 2*n/(2*n-1) * 2*n/(2*n+1)

class WallisProductFrame(tk.Frame):
    def __init__(self, master):
        super(WallisProductFrame, self).__init__(master=master)
        self.master = master
        self.drawFrame()
    def drawFrame(self):
        self.title = tk.Label(master=self, text='About the Wallis Product')
        self.title.grid()
