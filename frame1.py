import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, master, description, parameterText, calcText, submitButtonText):
        super(Frame1, self).__init__(master=master)
        self.master = master
        self.description = description
        
        self.parameterText = parameterText
        self.parameter = tk.StringVar()
        self.parameter.set('')
        
        self.calcText = calcText
        self.calcValue = tk.StringVar()
        self.calcValue.set('')
        
        self.submitButtonText = submitButtonText
    def drawFrame(self):
        self.descriptionLabel = tk.Label(master=self, padx=20, pady=20, text=self.description)  
        self.descriptionLabel.grid(row=0, columnspan=2)
        
        self.parameterLabel = tk.Label(master=self, text=self.parameterText)
        self.parameterLabel.grid(row=1, column=0, sticky='E')
        
        self.parameterEntry = tk.Entry(master=self, width=4, textvariable=self.parameter)
        self.parameterEntry.bind('<Key>', self.pressEnter)
        self.parameterEntry.grid(row=1, column=1, sticky='W')

        self.calcLabel = tk.Label(master=self, text=self.calcText)
        self.calcLabel.grid(row=2, column=0, sticky='E')

        self.calcValueLabel = tk.Label(master=self, width=20, textvariable=self.calcValue)
        self.calcValueLabel.grid(row=2, column=1, sticky='W')
        
        self.submitButton = tk.Button(master=self, text=self.submitButtonText, command=lambda: self.setCalcValue(self.calc()))
        self.submitButton.grid(row=3, columnspan=2, pady=(10, 20))
        
        self.grid()
    def setCalcValue(self, value):
        self.calcValue.set(value)
    def calc(self):
        return ''
    def pressEnter(self, event):
        if event.keycode == 13:
            self.setCalcValue(self.calc())
    
