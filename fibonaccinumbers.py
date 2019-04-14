import frame1

class FibonacciNumbersFrame(frame1.Frame1):
    def __init__(self, master):
        description = 'The nth Fibonacci number f(n) is defined to be f(n-1) + f(n-2) for n > 1. For n = 0 and n = 1 the Fibonacci numbers are defined to be f(0) = f(1) = 1. This program allows the user to calculate the nth Fibonacci number for n in the range [0, 25].'  
        parameterText = 'n = '
        calcText = 'Nth Fibonacci Number = '
        submitButtonText = 'Calculate'
        super(FibonacciNumbersFrame, self).__init__(master, description, parameterText, calcText, submitButtonText)
    def calc(self):
        try:
            value = int(self.parameter.get())
            if value >= 0 and value <= 25:
                return str(self.fibonacciNumber(value))
        except ValueError:
            pass
        return 'Enter an integer in [0, 25]'
    def fibonacciNumber(self, n):
        if n == 0 or n == 1:
            return 1
        return self.fibonacciNumber(n-1) + self.fibonacciNumber(n-2)

