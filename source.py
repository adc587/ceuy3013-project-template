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
        self.data = {  # Range of Values of Hydraulic Conductiviy and Permeability
            "Karl Limestone": [.1, .000001],
            "Permeable Limestone": [10 ** (-2), 10 ** (-7)],
            "Fractured Igneous and Metamorphic Rocks": [10 ** (-3), 10 ** (-8)],
            "Limestone and Dolomite": [10 ** (-3), 10 ** (-10)],
            "Sandstone": [10 ** (-6), 10 ** (-11)],
            "Unfractured Metamorphic and Igneous Rocks": [10 ** (-8), 10 ** (-13)],
            "Shale": [10 ** (-13), 10 ** (-10)],
            "Unweathered Marine Clay": [10 ** (-11), 10 ** (-6)],
            "Glacial Till": [10 ** (-10), 10 ** (-6)],
            "Silt, Loess": [10 ** (-9), 10 ** (-5)],
            "Silty Sand": [10 ** (-7), 10 ** (-4)],
            "Clean Sand": [10 ** (-6), 10 ** (-2)],
            "Gravel": [10 ** (-5), 10 ** (-1)]
        }

    def __str__(self):
        res = "Q = " + str(self.Q) + ", r_1 = " + str(self.r_1) + ", r_2 = " + str(self.r_2) + ", h_1 = " + str(
            self.h_1) + ", h_2 = " + str(self.h_2)
        res += ", b = " + str(self.b)
        return res


    def solve_for_k(self):
        '''
        Assume user always uses SI units. Returns K in (m^3)/s
        '''
        if self.b != 0: # for confined aquifers, b != 0
            return self.Q * math.log(self.r_2 / self.r_1)/(2 * math.pi * self.b*(self.h_2 - self.h_1))
        else: # b = 0 for unconfined aquifers
            return self.Q * math.log(self.r_2 / self.r_1) / (math.pi * ((self.h_2**2) - (self.h_1**2)))

    def possible_sediments_deposits(self):
        res = []
        for key,v in self.data.items():
            k = self.solve_for_k()
            #print(k)
            if v[0] < k < v[1]:
                res.append(key)
        return res

aqua_1 = TestClass("unconfined", 0.1083333, 1100, 0.15, 29.6, 20.46)
print(aqua_1)
print(aqua_1.solve_for_k())
print(aqua_1.possible_sediments_deposits())


