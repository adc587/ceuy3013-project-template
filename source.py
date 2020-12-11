# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# Here is a test class, replace the code below with your own
import math
class TestClass:
    def __init__(self, type, Q, r_1, r_2, h_1, h_2, b=0):
        self.type = type
        self.Q = Q
        self.r_1 = r_1
        self.r_2 = r_2
        self.h_1 = h_1
        self.h_2 = h_2
        self.b = b


    def __str__(self):
        return 'number: {}'.format(self.number)

    def solve_for_k(self):
        '''
        Assume user always uses SI units. Returns K in (m^3)/s
        '''
        if self.b != 0: # for confined aquifers, b != 0
            return self.Q * math.log(self.r_2 / self.r_1)/(2 * math.pi * self.b*(self.h_2 - self.h_1))
        else: # b = 0 for unconfined aquifers
            return self.Q * math.log(self.r_2 / self.r_1) / (2 * math.pi * (self.h_2 - self.h_1))

aqua_1 = TestClass("cofined", 180, 27,79,54.34,57.56, 15)
print(aqua_1.solve_for_k())
