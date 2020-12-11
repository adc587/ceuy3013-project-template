# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.

from source import Aquifer


if __name__ == '__main__':
    print('-------------------------- Aquifer 1 ---------------------------')
    aqua_1 = Aquifer("uncofined", 0.10833333, 1100, 0.15, 29.6, 20.46)
    print(aqua_1)
    print(aqua_1.solve_for_k())
    print(aqua_1.possible_sediments_deposits())

    aqua_2 = Aquifer("cofined", 0.002, 27, 79, 54.34, 57.56, 15)
    print()
    print('-------------------------- Aquifer 2 ---------------------------')
    print(aqua_2)
    print(aqua_2.solve_for_k())
    print(aqua_2.possible_sediments_deposits())
