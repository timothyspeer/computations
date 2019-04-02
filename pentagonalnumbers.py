import tkinter as tk

class PentagonalNumbersFrame(tk.Frame):
    def __init__(self, master):
        super(PentagonalNumbersFrame, self).__init__(master=master)
        self.master = master
        self.num = tk.StringVar()
        self.num.set('')
        self.calculation = tk.StringVar()
        self.calculation.set('')
    def drawFrame(self):
        self.description = tk.Label(master=self, padx=20, pady=20, text='The nth pentagonal number can be calculated using the formula n(3n-1)/2. This program'
                                                                      + ' allows the user to input an integer n in the range [1, 1000] and calculates the nth pentagonal number using'
                                                                      + ' the given formula.')
        self.description.grid(row=0, columnspan=2)
        
        self.numLabel = tk.Label(master=self, text='n = ')
        self.numLabel.grid(row=1, column=0, sticky='E')
        
        self.numEntry = tk.Entry(master=self, width=4, textvariable=self.num)
        self.numEntry.bind('<Key>', self.pressEnter)
        self.numEntry.grid(row=1, column=1, sticky='W')
        
        self.approximationLabel = tk.Label(master=self, text='Nth Pentagonal Number = ')
        self.approximationLabel.grid(row=2, column=0, sticky='E')

        self.approximation = tk.Label(master=self, width=20, textvariable=self.calculation)
        self.approximation.grid(row=2, column=1, sticky='W')
        
        self.calcButton = tk.Button(master=self, text='Calculate', command=lambda: self.calculation.set(str(self.calcApprox())))
        self.calcButton.grid(row=3, columnspan=2, pady=(10, 20))
        
        self.grid()
    def calcApprox(self):
        try:
            value = int(self.num.get())
            if value >= 1 and value <= 1000:
                return self.pentagonalNumber(value)
        except ValueError:
            pass
        return 'Enter an integer in [1, 1000]'
    def pressEnter(self, event):
        if event.keycode == 13:
            self.calculation.set(str(self.calcApprox()))
    def pentagonalNumber(self, n):
        return int(n * (3*n-1) / 2)