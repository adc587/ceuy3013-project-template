# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.

'''
This is the test section of the code,
the following shows two aquifers: an unconfined (aquifer 1) and confined (aquifer 2) aquifer.
feel free to input the values that you wish and the code will automatically return valuable data.

Program will return:

for both unconfined and confined
k (m/s) / (ft/s)
Possible sediments and deposits

for unconfined
thickness before and after pumping (m) / (ft)

for confined
drawdown (m) / (ft)

The following data has to be input in SI units (m^3/s and m) or US units (ft^3/s, and ft):

        type -> type of aquifer
        Q -> rate at which water is pumped out of well (m^3/s) / (ft^3/s)
        d -> distance from ground level to the bottom of aquifer (m) / (ft)

        - Cofined -
           r_1 -> distance between first well to pumping well (m) / (ft)
           r_2 -> distance between second well to pumping well (m) / (ft)
           d_1 -> height of closer observational well water table (m) / (ft)
           d_2 -> height of further observational well water table (m) / (ft)
           b -> thickness of the aquifer (m) / (ft)

       - Unconfined -
           r_1 -> radius of influence (m) / (ft)
           r_2 -> radius of pumping well (m) / (ft)
           d_1 -> drawdown at pumping well (m) / (ft)
           d_2 -> original depth of water (m) / (ft)

the test has been conducted using the homework examples question 1 (aquifer 1) and 2 (aquifer 2)
'''


from source import Aquifer

if __name__ == '__main__':
    aqua_2 = Aquifer(type="confined", Q=0.401, r_1=27, r_2=79, d_1=54.34, d_2=57.56, b=15, d=70)
    print()
    print('-------------------------- Aquifer 1 ---------------------------')
    print(aqua_2)
    print('k =', aqua_2.solve_for_k())
    print('possible sediments and deposits:', aqua_2.possible_sediments_deposits())
    # in the following print please assign the distance from the ground level to the original water level,
    # this will be necessary to calculate the drawdown at the wells
    # print(aqua_2.drawdown(wl)) <-- replace wl for the value in the print below.
    print('drawdown at observational wells 1 and 2 (s_1,s_2):', aqua_2.drawdown(10))

    print('-------------------------- Aquifer 2 ---------------------------')
    aqua_1 = Aquifer(type="unconfined", Q=0.10833333, r_1=1100, r_2=0.15, d_1=9.14, d_2=20.4, d = 50)
    print(aqua_1)
    print('k =', aqua_1.solve_for_k())
    print('possible sediments and deposits:', aqua_1.possible_sediments_deposits())
    print('thickness of aquifer before pumping =', aqua_1.h_1)
    print('thickness of aquifer after pumping =', aqua_1.h_2)
