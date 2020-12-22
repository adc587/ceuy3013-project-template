# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# Here is a test class, replace the code below with your own
import math
class Aquifer:
    def __init__(self, type, Q, r_1, r_2, d_1, d_2, b=0, d=0):
        '''
         type -> type of aquifer
         Q -> rate at which water is pumped out of well
         d -> distance from ground level to the bottom of aquifer

         - Cofined -
            r_1 -> distance between first well to pumping well
            r_2 -> distance between second well to pumping well
            d_1 -> height of closer observational well water table
            d_2 -> height of farther observational well water table
            b -> thickness of the aquifer

        - Unconfined -
            r_1 -> radius of influence
            r_2 -> radius of pumping well
            d_1 -> drawdown at well
            d_2 -> original depth of water
        '''

        self.type = type
        self.Q = Q
        self.r_1 = r_1
        self.r_2 = r_2
        self.d_1 = d_1
        self.d_2 = d_2
        self.b = b
        self.d = d
        self.h_1 = 0
        self.h_2 = 0
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
        self.thickness()

    def __str__(self):
        res = "Q = " + str(self.Q) + ", r_1 = " + str(self.r_1) + ", r_2 = " + str(self.r_2) + ", d_1 = " + str(
            self.d_1) + ", d_2 = " + str(self.d_2)
        res += ", b = " + str(self.b) + ', d = ' + str(self.d)
        return res


    def solve_for_k(self):
        '''
        Assume user always uses proper units. Returns K in (m/s) / (ft/s)
        '''
        if self.b != 0: # for confined aquifers, b != 0
            return self.Q * math.log(self.r_2 / self.r_1)/(2 * math.pi * self.b*(self.h_2 - self.h_1))
        else: # b = 0 for unconfined aquifers
            return self.Q * math.log(self.r_2 / self.r_1) / (math.pi * ((self.h_2**2) - (self.h_1**2)))

    def possible_sediments_deposits(self):
        '''
        picks appropriate sediments and deposits for each aquifer
        '''
        res = []
        for key,v in self.data.items():
            k = self.solve_for_k()
            #print(k)
            if v[0] < k < v[1]:
                res.append(key)
        return res

    def thickness(self):
        '''
        returns thickness of aquifer before pumping, h_1, and after pumping, h_2, in m / ft
        '''
        if self.b: # for confined aquifer
            self.h_1 = self.d_1
            self.h_2 = self.d_2
        else: # for unconfined aquifer
            self.h_1 = self.d - self.d_2
            self.h_2 = self.h_1 - self.d_1

    def drawdown(self, wl):
        '''
        wl* -> water level
        calculates drawdown, s_1 and s_2, of observational wells, in m / ft.
        '''
        if self.type == 'confined':
            wl1 = self.d - self.d_1
            wl2 = self.d - self.d_2
            s_1 = wl1 - wl
            s_2 = wl2 - wl
            return s_1, s_2


