import tkinter as tk

class WallisProductFrame(tk.Frame):
    def __init__(self, master):
        super(WallisProductFrame, self).__init__(master=master)
        self.master = master
        self.num = tk.StringVar()
        self.num.set('')
        self.calculation = tk.StringVar()
        self.calculation.set('')
    def drawFrame(self):
        self.description = tk.Label(master=self, padx=20, pady=20, text='The Wallis product has a value of pi/2. The Wallis product is the infinite product formed by taking the limit as n goes to infinity' 
                                                      + ' of the sequence whose nth term is given by \n\n [2*1/(2*1-1)]*[2*1/(2*1+1)]x' 
                                                      + '[2*2/(2*2-1)]*[2*2/(2*2+1)]x ...x[2*n/(2*n-1)]*[2*n/(2*n+1)] \n\n'
                                                      + ' This program allows the user to input an'
                                                      + ' integer n in the range [1, 990] and will calculate an approximation to the Wallis product by using the nth term from the above sequence.')  
        self.description.grid(row=0, columnspan=2)
        
        self.numLabel = tk.Label(master=self, text='n = ')
        self.numLabel.grid(row=1, column=0, sticky='E')
        
        self.numEntry = tk.Entry(master=self, width=4, textvariable=self.num)
        self.numEntry.grid(row=1, column=1, sticky='W')

        self.approximationLabel = tk.Label(master=self, text='Approximation = ')
        self.approximationLabel.grid(row=2, column=0, sticky='E')

        self.approximation = tk.Label(master=self, width=20, textvariable=self.calculation)
        self.approximation.grid(row=2, column=1, sticky='W')
        
        self.calcButton = tk.Button(master=self, text='Calculate', command=lambda: self.calculation.set(str(self.calcApprox())))
        self.calcButton.grid(row=3, columnspan=2, pady=(10, 20))
        
        self.grid()
    def calcApprox(self):
        try:
            value = int(self.num.get())
            if value >= 1 and value <= 990:
                return self.wallisProduct(value)
        except ValueError:
            pass
        return 'Enter an integer in [1, 990]'
    def wallisProduct(self, n):
        if n == 1:
            return 4 / 3
        return self.wallisProduct(n-1) * 2*n/(2*n-1) * 2*n/(2*n+1)