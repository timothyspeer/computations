import tkinter as tk

def wallisProduct(n):
    if n == 1:
        return 4 / 3
    return wallisProduct(n-1) * 2*n/(2*n-1) * 2*n/(2*n+1)

class WallisProductFrame(tk.Frame):
    def __init__(self, master):
        super(WallisProductFrame, self).__init__(master=master)
        self.master = master
    def drawFrame(self):
        self.description = tk.Label(master=self, padx=20, pady=20, text='The Wallis product has a value of pi/2. The Wallis product is the infinite product formed by taking the limit as n goes to infinity' 
                                                      + ' of the sequence whose nth term is given by \n\n [2*1/(2*1-1)]*[2*1/(2*1+1)]x' 
                                                      + '[2*2/(2*2-1)]*[2*2/(2*2+1)]x ...x[2*n/(2*n-1)]*[2*n/(2*n+1)] \n\n'
                                                      + ' This program allows the user to input an'
                                                      + ' integer n in the range [1, 2968] and will calculate an approximation to the Wallis product by using the nth term from the above sequence.')  
        self.description.grid(row=0, columnspan=2)
        self.numLabel = tk.Label(master=self, text='n = ')
        self.numLabel.grid(row=1, column=0, sticky='E')
        self.num = tk.Entry(master=self, width=4)
        self.num.grid(row=1, column=1, sticky='W')
        self.grid()
