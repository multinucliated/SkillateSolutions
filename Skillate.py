#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
Getting the input from the user 
first_Val will contain the actual strnig
and 
second value will get the NER for the previous string 
"""

first_Val = input("Enter your 1st string :")
second_Val = input("Enter your 2nd string :")

"""
Replacing the characters B- & I-
"""
second_Val = second_Val.replace("B-", "")
second_Val =second_Val.replace("I-", "")


# In[7]:


"""
Splitting and getting the list of the word , on space count !
"""
first_Val = first_Val.split(" ")
second_Val = second_Val.split(" ")


# In[8]:


"""
INitiazliing the dictionary 
"""
dict_data = {'Degree': [],
 'Insitute': [] ,
 'Company': [],
 'Location': [],
 'Title': [],
 'Major': [],
 'Others': []
}


# In[9]:


"""
Creating the loop , in which it will lool for every word from the first_val and look for the NEW word from the 
second_val variable and if it is found it will append to that dictionary key 
"""

for val in range( 0 , len(first_Val)):
    if second_Val[val] == "DEG":
        dict_data["Degree"].append(first_Val[val])
    elif second_Val[val] == "INS":
        dict_data["Insitute"].append(first_Val[val])
    elif second_Val[val] == "COM":
        dict_data["Company"].append(first_Val[val])
    elif second_Val[val] == "LOC":
        dict_data["Location"].append(first_Val[val])
    elif second_Val[val] == "TIT":
        dict_data["Title"].append(first_Val[val])
    elif second_Val[val] == "MAJ":
        dict_data["Major"].append(first_Val[val])
    elif second_Val[val] == "OTH":
        dict_data["Others"].append(first_Val[val])
        


# In[11]:


"""
Displaying the result
"""
print(dict_data)


# In[ ]:




