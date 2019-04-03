import frame1

class PentagonalNumbersFrame(frame1.Frame1):
    def __init__(self, master):
        description = 'The nth pentagonal number can be calculated using the formula n(3n-1)/2. This program allows the user to input an integer n in the range [1, 1000] and calculates the nth pentagonal number using the given formula.'
        parameterText = 'n = '
        calcText = 'Nth Pentagonal Number = '
        submitButtonText = 'Calculate'
        super(PentagonalNumbersFrame, self).__init__(master, description, parameterText, calcText, submitButtonText)
    def calc(self):
        try:
            value = int(self.parameter.get())
            if value >= 1 and value <= 1000:
                return str(self.pentagonalNumber(value))
        except ValueError:
            pass
        return 'Enter an integer in [1, 1000]'
    def pentagonalNumber(self, n):
        return int(n * (3*n-1) / 2)