'''
Program Name: ComplexNum.py 
Programmer Name: Ashwin Mayurathan
Date: 5-09-2022
Description: This code creates the class ComplexNum for the code ashwin_fractals.py
'''
#Creates Class
class ComplexNum():

    #init: Initializes the class
    def __init__(self):
        #The value associated with the real number
        self.num = 0
        #The value associated with the imaginary number
        self.imaginary = 0

    #assign_val: Lets the user assign values for the complex number. Takes 2 parameters
    #            The first parameter num is the real number part of the complex number
    #            The second parameter imaginary is the imaginary part of the complex number
    def assign_val(self, num, imaginary):
        self.num = num
        self.imaginary = imaginary

    #get_num_val: Returns the real number value of the complex number
    def get_num_val(self):
        return self.num

    #get_imaginary_val: Returns the imaginary value of the complex number
    def get_imaginary_val(self):
        return self.imaginary

    #get_complex_string: Returns a string to where the first number is the 
    #                    real number, and the second is the imaginary number
    def get_complex_string(self):
        return f"{self.num}, {self.imaginary}"

    #run_sequence: Runs the sequence Z(n) = Z(n-1)**2 + C to determine Z(n).
    #              Z(n-1) is the current value of the complex number before the sequence is run
    #              C is the constant that is added in the sequence
    def run_sequence(self, constant):
        #Finds the value of Z(n)
        #(x + yi)**2 = x**2 - y**2 + 2xyi
        #real number value: x**2 - y**2 (assign that as the real number)
        #imaginary number value (i not included): 2xy (assign that as the imaginary number)
        num = self.num**2 - self.imaginary**2 + constant.get_num_val()
        imaginary = self.num*self.imaginary*2 + constant.get_imaginary_val()

        #Reassigns the complex number
        self.assign_val(num, imaginary)
