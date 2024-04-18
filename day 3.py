#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=[1,2,3,4,5,6]
print(a)
print(a[3])
a[3]="Floki"
print(a)
print(a[3])


# In[8]:


arr=[11,12,13,14,"PSV",16,17]
for x in range(0,7):
    print(arr[x])


# class list(MutableSequnece[_T]):
# @overload
# def sort() #used to sort in ascending order
# def copy() #used to copy
# def append() # used to add element at the end
# def pop()
# def index()
# def count() #counts the no.of duplicates
# def insert() #
# def remove()
# tuple #similar to FINAL concept in JAVA

# In[18]:


x=[2,3,41,13,6]
y=x.copy()
print(y)
print(x.index(3))
print(len(x))
x.sort(reverse=True)
print(x)
for a in y:
    print(a)


# In[20]:


n=int(input("Enter the length of list:"))
a=[]
for x in range(0,n):
    x=input()
    a.append(x)
print(a)


# In[ ]:


L=[int(item) for item in (input("Enter the Elements of the lists: ").split())]


# In[31]:


a=[11,12,13,14,15,16]
#n=len(a)
for x in range((len(a)-1),-1,-1):
    print(a[x])


# In[ ]:


list=[11,12,13,14,15,16]
for x in range(len(list)


# Dictionary 
# 
# key and value
# 
# key value pairs

# In[35]:


D={1:"Magic Moment",2:"Royal Challengers",3:"Jack Daniel",4:"Black Dog"}
print(D) #prints the directories with keys and its values
print(D.keys()) #prints the keys 
print(D.values()) #prints the value for the respective keys
print(D.items()) #prints both keys and its values
print(D.get(4))  #prints a particular value of given key
print(D[3])      #similar to d.get()


# In[36]:


my_dict = {}
def add_to_dict(key, value):
    if key not in my_dict:
        my_dict[key] = value
    else:
        print("Key {0} is already exist".format(my_dict[key]))
num_pairs = int(input("Enter the number of key-value pairs you want to add: "))
for _ in range(num_pairs):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    add_to_dict(key, value)
print("Final Dictionary:", my_dict)


# In[40]:


a=[12,13,14,15,11,18,19,17,16,20]
print("list is:",a)
n=int(input("Enter the index value:"))
try:
    print(a[n])
except:
     print("Index out of range")
else:
    print("Value found")
finally:
    print("Error Handled...")


# In[ ]:




