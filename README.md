# CE-UY 3013 Project Template

*This file presents a description of the final project. For your submission,*
*this file must serve as the documentation of your project, how your program*
*should be used along with examples.*


#documentation

The aquifer class allows an aquifer obejct to be created. With all the different
variables for an aquifer. The comment in the code explains what each variable means,
and how it should be input in the test. The test section of the code has detailed instructions.

Code will return:

for both unconfined and confined
k (m/s) / (ft/s)
Possible sediments and deposits

for unconfined
thickness before and after pumping (m) / (ft)

for confined
drawdown (m) / (ft)

This code is able to do this because of a series of functions that were designed.
These are:

The function **solve_for_k** will solve for the hydraulic conductivity of the aquifer.
Given all the variables are valid.

The function **possible_sediments_deposits** will pick all possible sediments and 
deposits for each aquifer, be it confined or unconfined. the variable **self.data**
stores the k values for each possible sediment and deposit.

The function **thickness** returns the thickness of the aquifer before and
after pumping.

The funtion **drawdown** returns the drawdowns for a confined aquifer given a
water level.

The test file has examples using the numbers from the homework to make sure all
the calculations work. The homework examples are attached in the repository and can be found as:

Questions:
Hw5 - ground water

Solutions
Hw5 solutions



