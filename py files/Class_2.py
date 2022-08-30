#!/usr/bin/env python
# coding: utf-8

# ***
# ## Assignment 1: Do following types of string formatting with % operator in either ipynb or py file:  
# 1. character %c 
# 2. string %s 
# 3. integer %d, %i 
# 4. octal %o     
# 5. hexadecimal %x 
# 6. floating point number %f 
# 7. floating point number in scientific notation %e, %E 
# ***

# # 1. Global Scope and Buit-in Scope difference
# ### * To access built-in attributes and functions importing does not required. To access global function and variables of other files/modules you need to import that file in the current file.  

# ### 1.1 Built-in Function has no need to be imported.

# In[1]:


round(4.434567, 3) # round is a built-in function and no need to import its file or library


# ### 1.2 Importing Global Variable of Class_1.py file to use it in Class_2.ipynb

# In[8]:


# importing global variable test1 of Class_1.py file

from Class_1 import test1
print(test1)


# ### 1.2 Importing Global Variable of Class_1.ipynb file to use it in Class_2.ipynb

# In[3]:


get_ipython().system('pip install import_ipynb # installation of the library for importing from ipynb file')


# In[4]:


import import_ipynb
from Class_1 import test1 # importing global variable test1 of Class_1.ipynb file

print(test1)


# # 2. Compiler and Interpreter and their difference
# 
# ## Link: <a href="https://www.geeksforgeeks.org/difference-between-compiler-and-interpreter/">Difference between Compiler and Interpreter</a>
# 
# <img src="https://www.astateofdata.com/wp-content/uploads/2019/09/python-code-copiler-machine-code.png" style="width: 49.5%; display: inline-block;"> <img src="https://csharpcorner-mindcrackerinc.netdna-ssl.com/article/why-learn-python-an-introduction-to-python/Images/last2.png" style="width: 49.5%; display: inline-block;">

# # 3. String Formatting
# 
# ### Link: 1. <a href="https://www.geeksforgeeks.org/string-formatting-in-python/#:~:text=Formatting%20with%20%25%20Operator.,Formatting%20with%20String%20Template%20Class">String formatting in Python</a> 
# ### Link: 2. <a href="https://www.freecodecamp.org/news/format-specifiers-in-c/">Format Specifiers in C</a>
# 
# ## 3.1. String Formatting using %

# In[5]:


teacher = "Dayan"
student = "Zareef"

print('%s is the teacher of this class. \
%s is the most attentive student of his class.' % (teacher, student))


# ## 3.2 String Formatting using % for floating point value

# In[6]:


PI = 3.141592
print("%.3f is the value of PI" %PI)


# ## 3.2 String Formatting using % for character, octal, hexadecimal
# 
# ### a = 97 (Decimal) = 1100001 (Binary)

# In[7]:


print("Charcter of ASCII Code 97 is = %c" %97)
print("Octal Number of ASCII Code 97 is = %o" %97)
print("Hexa Decimal Number of ASCII Code 97 is = %x" %97)

