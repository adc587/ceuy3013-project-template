# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.

from source import Aquifer


if __name__ == '__main__':

    aqua_1 = Aquifer("unconfined", 0.1083333, 1100, 0.15, 29.6, 20.46)
    print(aqua_1)
    print(aqua_1.solve_for_k())
    print(aqua_1.possible_sediments_deposits())
