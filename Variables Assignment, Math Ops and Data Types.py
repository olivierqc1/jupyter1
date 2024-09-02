#!/usr/bin/env python
# coding: utf-8

# ![image-2.png](attachment:image-2.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[ ]:


# Let's define a variable named "company_name" and assign a value to it
# A string in Python is a sequence of characters that are surrounded by single or double quotations
# You can run the cell by clicking "shift + enter" or by clicking the "Run" button

# Note that you might be wondering - I can do this in Excel, why am I using Python for this?! 
# This is an introductory lecture to Python, we will build on what we learn to develop powerful applications 
# Python offers greater scalability and efficiency compared to Excel
# It offers faster execution and allows for automating complex tasks 
# It also comes with several open-source libraries so we do not have to develop code from scratch

company_name = 'Apple'


# In[ ]:


# Let's display the content of "company_name"
company_name


# In[ ]:


# Let's confirm the datatype for our variable
# Note that the output is "str" which stands for string 
type(company_name)


# In[ ]:


# Let's define and display the second entry in the table and assign a decimal number to it
revenue = 394.32
revenue


# In[ ]:


# Let's confirm the datatype for our variable
# Note that the datatype is "float" which stands for floating points
# Floating points are real numbers with a decimal point dividing the integer and fractional parts
type(revenue)


# In[ ]:


# Let's define and display the third entry in the table and assign an integer to it
num_employees = 154000
num_employees


# In[ ]:


# Let's confirm the datatype for our variable
# Note that the output is "int" which stands for integer 
# Integers are whole numbers (no decimals) that could be positive or negative
type(num_employees)


# In[ ]:


# Let's define and display the last element in the table 
pays_dividend = True
pays_dividend


# In[ ]:


# "bool" stands for Boolean which is a datatype that has one of two possible values: True or False
type(pays_dividend)


# In[ ]:


# After we define variables, we can then perform math operations on them
# Math operations can be easily performed in Python
# Addition (+), Subtraction (-), Multiplication (*), Division (/) 

# Let's assume that the number of employees increased by 100 
# Note that we overwrite the previous value of "num_employees" with the new value
num_employees = num_employees + 100
num_employees


# In[ ]:


# Let's assume that the number of employees has now doubled
# We will learn how to store tablular data efficiently later in the course using Pandas library
num_employees = num_employees * 2
num_employees


# **PRACTICE OPPORTUNITY:** 
# - **Assume that you have \\$5000 in your brokerage account and you decided to invest the entire amount in Procter & Gamble (P&G) stock which is trading at \\$142.5 per share. Complete the following tasks:** 
#     - **1. Write a Python code that defines two variables for the account balance and P&G stock price. Feel free to select any valid variable names**
#     - **2. Confirm variables datatypes**
#     - **3. Calculate number of shares that you can buy with the available balance in your account**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # PRACTICE OPPORTUNITY SOLUTION

# **PRACTICE OPPORTUNITY SOLUTION:** 
# - **Assume that you have \\$5000 in your brokerage account and you decided to invest the entire amount in Procter & Gamble (P&G) stock which is trading at \\$142.5 per share. Complete the following tasks:** 
#     - **1. Write a Python code that defines two variables for the account balance and P&G stock price. Feel free to select any valid variable names**
#     - **2. Confirm variables datatypes**
#     - **3. Calculate number of shares that you can buy with the available balance in your account**

# In[ ]:


# Define the account balance 
balance = 5000
balance


# In[ ]:


# Confirm the datatype which is integer
type(balance)


# In[ ]:


# Define the price per share
price = 142.5 
price


# In[ ]:


# Confirm the datatype which is float
type(price)


# In[ ]:


# Calculate the number of shares by dividing the brokerage balance by P&G stock price 
# Place the answer in num_shares
num_shares = balance/price
num_shares 


# In[ ]:


# Note that you can round your answer to the nearest integer by using the round function
round(num_shares)


# # EXCELLENT JOB
