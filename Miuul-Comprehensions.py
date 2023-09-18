#!/usr/bin/env python
# coding: utf-8

# # List Comprehension

# In[31]:


salaries = [1000,2000,3000]
def new_salary(x):
    return x*20/100 + x
for salary in salaries:
    print(new_salary(salary))


# In[32]:


null_list=[]
for salary in salaries:
    null_list.append(new_salary(salary))
print(null_list)
   


# In[33]:


null_list=[]
for salary in salaries:
    if salary>2000:
        null_list.append(new_salary(salary))
    else:
        print("zam yok")
print(null_list)


# In[34]:


[new_salary(salary) if salary <2000 else new_salary(salary*2) for salary in salaries]


# In[35]:


[salary*2 for salary in salaries if salary <3000 ]


# In[36]:


students=["John","Mark","Venessa","Mariam"]
students_no = ["John","Venessa"]
[student.lower() if student in students_no else student.upper()  for student in students]


# # Dict Comprehension
# 

# In[37]:


dictionary={
    'a':1,
    'b':2,
    'c':3,
}
dictionary.keys()


# In[38]:


dictionary.values()


# d

# In[39]:


dictionary.items()


# In[40]:


{k:v**2 for (k,v) in dictionary.items()}


# In[41]:


{k.upper(): v for (k,v) in dictionary.items()}


# In[42]:


import numpy as np
numbers=range(10)
new_dict= {}


# In[43]:


{k:k**2 for k in numbers if k%2==0}


# # List & Dict Comprehension Uygulamalar 

# Bir veri setindeki degisken isimlerini degistirmek 

# In[44]:


#before
#['total','not_spending','ins_alcohol']
#after
#['TOTAL','NOT_SPENDING','INS_ALCOHOL']


# In[45]:


import seaborn as sns 
df=sns.load_dataset("car_crashes")


# In[46]:


A=[]
for col in df.columns:
    print(col.upper())



# In[47]:


#df=sns.load_dataset("car_crashes")
#df.columns = [col.upper() for col in columns]


# 

# In[48]:


[col for col in df.columns if "INS" in col]


# In[49]:


["FLAG" + col for col in df.columns if "INS" in col ]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




