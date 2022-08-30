#!/usr/bin/env python
# coding: utf-8

# # Class 1 - All Topics

# # List of all Magic Cell commands

# In[2]:


get_ipython().run_line_magic('lsmagic', '')


# # single and double quotation difference in python

# In[20]:


string_1 = 'I love apple\'s product'
string_2 = "I love apple's product"
string_3 = "He says, \"you are a good man.\""
string_4 = 'He says, "you are a good man."'

print(string_1)
print(string_2)
print(string_3)
print(string_4)


# # Writing and saving another python file 

# In[18]:


get_ipython().run_cell_magic('writefile', 'test.py', 'a = 5\n\ndef num_sum(a, b):\n    return a+b\n\ndef num_minus(a, b):\n    return a-b\n')


# # import another module or file

# In[19]:


num1, num2 = 10, 15;

import test

print(test.a)


# # Running different ipynb file

# In[15]:


get_ipython().run_line_magic('run', '"test.ipynb"')


# # Importing python module/ file from another directory

# In[16]:


import sys

sys.path.insert(1, '/Users/Dayan/test.py')

from test import num_sum

num1 = 100; num2 = 200;

print(num_sum(num1, num2))


# # Variable Scope (LEGB - Local, Enclosing, Global, Built-In)

# ## 1. Globa Scope

# In[3]:


num1 = 10 # Global Scope

def testing_fun():
    
    print(num1) # printing num1 global variable 
    
    return 'successfully run'

print(testing_fun())
num1


# ## 2.1 Local Scope

# In[5]:


num1 = 10 # Global Scope

def testing_fun():
     
    num1 = 20 # Local Scope
    print(num1) # printing num1 global variable 
    
    return 'successfully run'

testing_fun()

print(num1)


# ### 2.1.1 Accessing Global Variable in Local Scope

# In[9]:


num1 = 10 # Global Scope

def testing_fun():
    
    global num1 
    print(num1) # printing num1 global variable 
    
    return 'successfully run'

testing_fun()

print(num1)


# ## 3. Enclosing Scope

# In[4]:


def func1():
    num1 = 5.5 # Enclosing
    def func2():
        num2 = 3.4 # Local Scope
        print(num1)        
        print(num2)
    
    func2()
    
func1()


# ## 4. Built-In Scope

# In[20]:


test1 = round(4.2557, 1) # Global Scope

def outer_func():
    test2 = round(4.2) # Enclosing Scope
    
    def inner_func():
        test3 = round(3.12354, 3) # Local Scope
        print('test3 =', test3)
        print('test2 =', test2)
    inner_func()
    
    print('test1 =', test1, ', test2 =', test2)
    
outer_func()

