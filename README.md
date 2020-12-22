# CE-UY 3013 Project Confined and Unconfined Aquifers by Arturo Carvajales

*This file presents a description of the final project.*

The aquifer class allows an aquifer obejct to be created with all the different
variables for an aquifer. The comments in the code explains what each variable means,
and how it should be input in the test. The test section of the code also has detailed instructions.
The following is the basic instructions as to give an idea of what this code can do.

The inputs required (input has to be in SI units (m^3/s and m) or US units (ft^3/s, and ft):

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


Code will return:

	- for both unconfined and confined -
	   k -> (m/s) / (ft/s)
	   Possible sediments and deposits

	- for confined -
	   drawdown at each observational well (m) / (ft)

	- for unconfined -
	   thickness before and after pumping -> (m) / (ft)


This code is able to do this because of a series of functions that were designed,
these are:

	- The function **solve_for_k** will solve for the hydraulic conductivity of the aquifer.
	Given all the variables are valid.

	- The function **possible_sediments_deposits** will pick all possible sediments and 
	deposits for each aquifer, be it confined or unconfined. the variable **self.data**
	stores the k values for each possible sediment and deposit.

	- The function **thickness** returns the thickness of the aquifer before and
	after pumping.

	- The funtion **drawdown** returns the drawdowns for a confined aquifer given a
	water level.

The test file has examples using the numbers from the homework to make sure all
the calculations work. The homework examples are attached in the repository and can be found as:

	- Questions:
	Hw5 - ground water

	- Solutions
	Hw5 solutions



