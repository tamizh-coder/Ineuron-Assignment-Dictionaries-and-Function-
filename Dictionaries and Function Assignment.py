#!/usr/bin/env python
# coding: utf-8
### Q1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle from user should be defined in the parentclass and function to calculate the area should be defined in subclass.
# In[1]:


class Triangle:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def area(self):
        s=(self.i+self.j+self.k)/2
        area=(s*(s-self.i)*(s-self.j)*(s-self.k))**0.5
        return area
    
i=float(input("Enter a length of side i:"))
j=float(input("Enter a length of side j:"))
k=float(input("Enter a length of side k:"))
tri=Triangle(i,j,k)

print("Area of trianle is {}".format(tri.area()))

### Q1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
# In[6]:


def filter_long_word(list_1,n):
    list_2=[]
    for i in range(0,len(list_1)):
        if len(list_1[i])>n:
            list_2.append(list_1[i])
    return list_2
list_3=['mohan','raj','loke','apple','sweet']
n=int(input("Enter a value for n:-"))
lst=filter_long_word(list_3,n)
print("List of words longer than {}".format(n))
print(lst)

# Q2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.
# In[8]:


def find_length(list_1):
    new_list=[]
    for i in range (0,len(list_1)):
        new_list.append(len(list_1[i]))
    return new_list
list_2=['ab','cde','erty']
length_lst=find_length(list_2)
print(length_lst)

### Q2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
# In[9]:


def vowel(x):
    if len(x)==1:
        if x in ('a','e','i','o','u','A','E','I','O','U'):
            return True 
        else:
            return False
    else:
        print('Type only one letter')
    
print(vowel('a'))
print(vowel('s'))
print(vowel('al'))


# In[ ]:




