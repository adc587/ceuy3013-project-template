# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.

from source import Aquifer


if __name__ == '__main__':
    print('-------------------------- Aquifer 1 ---------------------------')
    aqua_1 = Aquifer("unconfined", 0.10833333, 1100, 0.15, 29.6, 20.46, d = 50)
    print(aqua_1)
    print('k =', aqua_1.solve_for_k())
    print('possible sediments and deposits:', aqua_1.possible_sediments_deposits())
    print('thickness before pumping =', aqua_1.h_1)
    print('thickness after pumping =', aqua_1.h_2)

    aqua_2 = Aquifer("confined", 0.002, 27, 79, 54.34, 57.56, 15, d = 70)
    print()
    print('-------------------------- Aquifer 2 ---------------------------')
    print(aqua_2)
    print('k =', aqua_2.solve_for_k())
    print('possible sediments and deposits:', aqua_2.possible_sediments_deposits())
    print(aqua_2.drawdown(10))