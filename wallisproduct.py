import frame1

class WallisProductFrame(frame1.Frame1):
    def __init__(self, master):
        description = 'The Wallis product has a value of pi/2. The Wallis product is the infinite product formed by taking the limit as n goes to infinity of the sequence whose nth term is given by \n\n [2*1/(2*1-1)]*[2*1/(2*1+1)]x[2*2/(2*2-1)]*[2*2/(2*2+1)]x ...x[2*n/(2*n-1)]*[2*n/(2*n+1)] \n\n This program allows the user to input an integer n in the range [1, 989] and will calculate an approximation to the Wallis product by using the nth term from the above sequence.' 
        parameterText = 'n = '
        calcText = 'Approximation = '
        submitButtonText = 'Calculate'
        super(WallisProductFrame, self).__init__(master, description, parameterText, calcText, submitButtonText)
    def calc(self):
        try:
            value = int(self.parameter.get())
            if value >= 1 and value <= 989:
                return str(self.wallisProduct(value))
        except ValueError:
            pass
        return 'Enter an integer in [1, 989]'
    def wallisProduct(self, n):
        if n == 1:
            return 4 / 3
        return self.wallisProduct(n-1) * 2*n/(2*n-1) * 2*n/(2*n+1)