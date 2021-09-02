#!/usr/bin/env python
# coding: utf-8

# # Problem Set 1
# 
# 
# <span style="color:red">**Handed out:**</span> Monday August 23, 2021
# 
# **Due date:** Thursday September 09, 2021
# 
# 
# Problem set 1 will introduce you to the basic Python modules that you will see during the first two weeks of class. Remember that for your benefit, it will be better for you to start working on the assignments as early as possible. That way, you will have everything fresh in your mind and will be easier to finish with the assignment in due course. You will also avoid any late-submissions that carry grade reduction.
# 
# Finally, make sure you familiarize yourselves with how Anaconda and Jupyter notbooks work before proceeding with the actual assignments.
# 
# **New Python package! `NumPy`**
# 
# For the assignments in this set (and for all subsequent sets), you will need to use `NumPy`. `NumPy` is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
# 
# Of course, you won't need all of those!
# 
# First import `NumPy`
# ```python
# import numpy as np
# ```
# 
# Use the alias `np` to call any `NumPy` functions:
# ```python
# np.add(1,2) # add two values
# np.pow(2,2) # same as 2**2
# ```
# 
# You can always refer to the [Python Wikibook](https://en.wikibooks.org/wiki/Python_Programming) for more information on Python packages, functions, and more. And, don't forget: *Google is your friend!*

# ## Assignment 1: A Very Simple Program: Raising a number to a power and taking a logarithm (10 points)
# 
# Remember the standard program elements:
# - print out results (using the `print` operation)
# - read input from a user at the console (using the `input` function)
# - store values in variables, so that the program can access that value as needed.

# Write a program in Python that does the following:
# - Enter a number `x`
# - Enter a number `y`
# - Print $x^y$
# - Print $log_2(x)$
# 
# **Assist:** If `x = 2` and `y = 3`, your printed statements will be:
# 
# <span style="color:blue">Enter number x:</span> 2
#     
# <span style="color:blue">Enter number y:</span> 3
#     
# <span style="color:blue">x**y:</span> 8
#     
# <span style="color:blue">log(x):</span> 1
# 

# In[8]:


import math

x = int(input('Enter a number x:'))
y = int(input('Enter a number y:'))

alg1 = pow(x,y)
alg2 = math.log2(x) 

print('x**y:'+ str(alg1))
print('log(x):'+ str(alg2))


# ## Assignment 2: House hunting (20 points)
# 
# You have graduated from UM and now have a great job as a junior project manager! You move to the San Francisco Bay Area and decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area, you realize you are going to have to save for several years before you can afford to make the down payment on a house. In this assignment, you have to determine how long it will take you to save enough money to make the down payment given the following assumptions:
# 
# 1. Call the cost of your dream home `total_cost`. 
# 2. Call the portion of the cost needed for a down payment `portion_down_payment`. For simplicity, assume that `portion_down_payment = 0.25 (25%)`. 
# 3. Call the amount that you have saved thus far `current_savings`. You start with a current savings of 0 dollars. 
# 4. Assume that you invest your current savings wisely, with an annual return of `r` (in other words, at the end of each month, you receive an additional `current_savings*r/12` funds to put into your savings – the 12 is because `r` is an annual rate). Assume that your investments earn a return of `r = 0.04 (4%)`. 
# 5. Assume your annual salary is `annual_salary`. 
# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that `portion_saved`. This variable should be in decimal form (i.e. 0.1 for 10%). 
# 7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12).
# 8. Be careful about values that represent annual amounts and those that represent monthly amounts.
# 
# Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats.
# 
# Your program should ask the user to enter the following variables: 
# 1. The starting annual salary (`annual_salary`) 
# 2. The portion of salary to be saved (`portion_saved`)
# 3. The cost of your dream home (`total_cost`)
# 
# **Hints:** To help you get started, here is a rough outline of the stages you should probably follow in writing your code: 
# - Retrieve user input. Look at `input()` if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a `str` when you expect an `int`) 
# - Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts.
# 
# Printouts should be like:
# 
# <span style="color:blue">Enter your annual salary:</span> 120000
#     
# <span style="color:blue">Enter the percent of your salary to save, as a decimal:</span> .10
#     
# <span style="color:blue">Enter the cost of your dream home:</span> 1000000
#     
# <span style="color:blue">Number of months:</span> 183

# In[16]:


#set up input
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

#organize algorithm
current_savings = 0
annual_return_rate = 0.04
num_months = 0
portion_down_payment = 0.25

while True: 
    current_savings = (annual_salary/12)*portion_saved + current_savings*(1 + annual_return_rate/12)
    num_months += 1
    if current_savings >= total_cost*portion_down_payment:
        break

# set up output
print('Number of months: '+ str(num_months))


# ## Assignment 3: Saving with raise (15 points)
# 
# Modify the program from Assignment 2, to include the following:
# 1. Have the user input a semi-annual salary raise `semi_annual_raise` (as a decimal percentage) 
# 2. After the 6th month, increase your *annual salary* by that percentage. Do the same after the 12th month, the 18th month, and so on.
#     * **Hint:** Use the mod (\%) operator
# 
# Printouts should be like:
# 
# <span style="color:blue">Enter your annual salary:</span> 120000
#     
# <span style="color:blue">Enter the percent of your salary to save, as a decimal:</span> . 05
#     
# <span style="color:blue">Enter the cost of your dream home:</span> 500000
# 
# <span style="color:blue">Enter the semi-annual raise, as a decimal:</span> .03
#     
# <span style="color:blue">Number of months:</span> 142

# In[ ]:


## set up input
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual = float(input('Enter the semi-annual raise, as a decimal: '))

#organize algorithm
current_savings = 0
annual_return_rate = 0.04
num_months = 0
portion_down_payment = 0.25

while True: 
    current_savings = (annual_salary/12)*portion_saved + current_savings*(1 + annual_return_rate/12)
    num_months += 1
    if num_months%6 == 0:
        annual_salary = annual_salary * ( 1 + semi_annual)
    if current_savings >= total_cost*portion_down_payment:
        break

# set up output
print('Number of months: '+ str(num_months))


#  ## Assignment 4: Convert Celsius to Farenheit (15 points)
# 
# Usually, for those of us not originally from the US, one of the things that give us headaches is the difference between the Standard and Imperical metric systems. We are usually buffled when we need to calculate distances in feet, yards, and miles, rather than meters and kilometers, or when we need to calculate the weight in ounces and pounds, rather than grams and kilograms.
# 
# Another mind-boggling conversion is regarding measuring temperature in Farenheit rather than Celsius. The conversion formula is shown below:
# 
# $F = (9/5) * C + 32$
# 
# The purpose of this assignment is to write a program in Python converting the temperature in Celsius to Fahrenheit. Have the program output the values side-by-side. On the left, it prints out the temperature in Celsius, and on the right in Fahrenheit. Have the data print out all integer values of Celsius from 0 to 100 in 3 degree increments. Have the data print out the Fahrenheit to two decimal points.
# 
# **Hint:** Format the `print` as: 
# ```python
# print('%s %d  %s %.2f' % ('Celsius: ', celsius, 'Farenheit: ', farenheit))
# ```
# That way, you will see only two decimal points when printing the Farenheit values.

# In[16]:


celsius = 0

for each in range(0, 100, 3):
    celsius = each
    farenheit = celsius * (9/5) + 32
    print('Celsius: ', celsius, 'Farenheit: ', "{:.2f}".format(farenheit))
    


# ## Assignment 5: Functions (15 points)
# 
# The program you wrote for Assignment 3 does the right thing (hopefully!!), but the problem is that there are many lines within the `while` loop that makes the thread cumbersome to read. 
# 
# For this assignment, you will have to convert these lines into separate functions which you will call within the main program body. See the following example and consider it as a template for your program:
# 
# *Example:* Write a Python code that takes two numbers as inputs and prints out their sum
# 
# $1^{st}$ approach - Put everything to a single thread:
# ```python
# x = int(input("Enter value for x: ", ))
# y = int(input("Enter value for y: ", ))
# 
# res = x + y
# print(res)
# ```
# $2^{nd}$ approach - Use a function for the addition part:
# ```python
# def sum_func(x, y):
#     return x + y
# 
# x = int(input("Enter value for x: ", ))
# y = int(input("Enter value for y: ", ))
# 
# res = sum_func(x, y)
# print(res)
# ```
# 
# You are free to use any argument format for calling the function, based on what we saw in class.

# In[5]:


#set up input
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual = float(input('Enter the semi-annual raise, as a decimal: '))

#organize algorithm

# define a function
def months_of_saving(annual_salary, portion_saved, total_cost, semi_annual):
    current_savings = 0
    annual_return_rate = 0.04
    num_months = 0
    portion_down_payment = 0.25

    while True: 
        current_savings = (annual_salary/12)*portion_saved + current_savings*(1 + annual_return_rate/12)
        num_months += 1
        if num_months%6 == 0:
            annual_salary = annual_salary * ( 1 + semi_annual)
        if current_savings >= total_cost*portion_down_payment:
            break
    
    print('Number of months: ', num_months)

# set up output
months_of_saving(annual_salary, portion_saved, total_cost, semi_annual)


# ## Assignment 6: Calculate the volume of a sphere (15 points)
# 
# Compute the volume of a sphere with a radius of 5. The formula for a sphere is: $$\frac{4}{3}*\pi*r^3$$
# 
# Write a function `sphere_volume` that returns the volume of a sphere when given radius `r` as a parameter. Then in the main program call `sphere_volume` to print the volume of a sphere with a `radius = 5`. 
# 
# **Hint:** For **π** you can either directly assign `3.14` to a parameter, or (and I suggest you do that) import package `math` that contains all the known mathematical parameters:
# ```python
# import math
# 
# print(math.pi) # prints parameter π
# ```

# In[6]:


import math

def sphere_volumn(r):
    return 4/3*math.pi*(r^3)

print(sphere_volumn(5))


# ## Assignment 7: Check if a number is within a range (10 points)
# 
# Write a function that checks whether a number is in a given range.
# 
# This assignment is rather simple, you will need to include a conditional within the function body to see if the given number does belong to the given range.
# 
# You have to approach the solution to this assignment in two ways. In the first approach, your function will print out the result, whereas in the second, you have to use boolean return values.
# 
# **Example:** name your function `range_check` and build it to get three arguments: a) the number in question, b) the low end of the range, and c) the high end of the range.

# In[4]:


# First way
num = int(input('Please input the number to check: '))
start = int(input('Please input the start of the range: '))
end = int(input('Please input the end of the range: '))

def range_check(num, start, end):
    if num < start or num > end:
        print(str(num) + ' is not included in [', str(start), ', ' + str(end) + ']')
    else:
        print(str(num) + ' is included in [', str(start), ', ' + str(end) + ']')
        
range_check(num, start, end)


# In[29]:


# Second way
num = int(input('Please input the number to check: '))
start = int(input('Please input the start of the range: '))
end = int(input('Please input the end of the range: '))

def range_check(num, start, end):
     if num < start or num > end:
        return False
     else:
        return True
    
if range_check(num, start, end):
    print(str(num) + ' is included in [', str(start), ', ' + str(end) + ']')
else:
    print(str(num) + ' is not included in [', str(start), ', ' + str(end) + ']')

