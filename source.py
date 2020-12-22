# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# Here is a test class, replace the code below with your own
import math
class Aquifer:
    def __init__(self, type, Q, r_1, r_2, h_1, h_2, b=0):
        '''
              type -> type of aquifer
              Q -> rate at which water is pumped out of well

              - Cofined -
                 r_1 -> distance between first well to pumping well
                 r_2 -> distance between second well to pumping well
                 h_1 -> height of closer observational well water table
                 h_2 -> height of farther observational well water table
                 b -> thickness of the aquifer

             - Unconfined -
                 r_1 -> radius of influence
                 r_2 -> radius of pumping well
                 h_1 -> original thickness of aquifer
                 h_2 -> height of water table at the pumping well
             '''

    ---------------
    '''
      type -> type of aquifer
      Q -> rate at which water is pumped out of well
      d -> distance from ground level to the bottom of aquifer

      - Cofined -
         r_1 -> distance between first well to pumping well
         r_2 -> distance between second well to pumping well
         h_1 -> height of closer observational well water table
         h_2 -> height of farther observational well water table
         b -> thickness of the aquifer

     - Unconfined -
         r_1 -> radius of influence
         r_2 -> radius of pumping well
         h_1 -> depth after pumping
         h_2 -> original depth of water
     '''

    self.type = type
        self.Q = Q
        self.r_1 = r_1
        self.r_2 = r_2
        self.h_1 = h_1
        self.h_2 = h_2
        self.b = b
        self.d = d
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


    def thickness(self):
        if self.b:  # for confined well
            return self.b
        else:
            return self.d - self.h_2  # for uncofined well
