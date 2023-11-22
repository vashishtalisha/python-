#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1.Reverse a list in Python
n=int(input())
li=[int(x) for x in input().split()]
def rev_list(li):
    for i in range(len(li)//2):
        li[i],li[len(li)-i-1]=li[len(li)-i-1],li[i]
    print(li)
rev_list(li)    


# # There are four collection data types in the Python programming language:
# 
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# 

# In[ ]:


#.Write a Python program to clone or copy a list.
li=[1,2,3,6,8]
clone_li=[]
for ele in li:
    clone_li.append(ele)
print(clone_li)    


# In[56]:


#sort list in ascending order
li=[1,7,-9,5,4]
li.sort(reverse=True)
li
    


# In[ ]:


#25. Write a Python program to print the numbers of a specified list after removing even numbers from it.
n=int(input())
li=[] 
for _ in range(n):
    li.append(int(input()))
li=[x for x in li if x%2!=0]
li


# In[ ]:





# In[ ]:


# Check if a list contains an element
n=int(input())
j=input() 
li=[] 
for _ in range(n):
    li.append(input())
if j in li: 
    print("yes")
else: 
    print("no")


# In[ ]:


#.Write a Python program to check if a list is empty or not.
li=[]
if not li:
    print("empty")


# In[40]:


#.accepts a list from the user and prints alternate elements of the list.
li=[]
n=int(input())
for _ in range(n):
    li.append(input())
print(li[::2])
    


# In[ ]:


#to display max value of the list.
li=[]
n=int(input())
for _ in range(n):
    li.append(input())
max=li[0]
for i in li:
    if i>=max:
        max=i
print(max)
    


# ### 2.Concatenate two lists index-wise
# li1=['a','b','c','d']
# li2=['a','b','c','d' ]
# li=[]
# for i in range(len(li1)):
#     li.append(li1[i]+li2[i])
# li

# In[43]:


#or
li1=['a','b','c','d']
li2=['a','b','c','d' ]
li=[i+j for i,j in zip(li1,li2)]
li


# In[46]:


#3.Turn every item of a list into its square
li=['1','2','3','4']
li=[int(i)**2 for i in li]
li


# In[14]:


#concatenate two list as:
# hello,dear
# sir,mam
# hello sir ,hello mam ,dear sir, dear mam
li=['hello','dear']
l=['sir','mam']
li1=[]
for i in range(len(li)):
    for j in range(len(l)):
        li1.append(li[i]+" "+l[j])
li1


# In[16]:


#or
li2=[x+" "+y for x in li for y in l]
li2


# In[47]:


#.Iterate both lists simultaneously
li1=['a','b','c','d']
li2=['a','b','c','d' ]
for i,j in zip(li1,li2):
    print(i,j)


# In[48]:


#.Remove empty strings from the list of strings
li=['as','g',' ','','gty']
li.remove('')
li


# In[57]:


#.Add new item to list after a specified item
n=int(input())
m=int(input())
i=int(input())
li=[]
for _ in range(n):
    li.append(input())

li.insert(i,m)
li


# In[ ]:


# .Write a Python program to remove duplicates from a list
n=int(input())
li=[int(x) for x in input().split()]
#create an empty list for unique items
unique_li=[]
for ele in li:
    if ele not in unique_li:
        unique_li.append(ele)
print(unique_li)        


# In[ ]:


#another method
n=int(input())
li=[int(x) for x in input().split()]
li=list(set(li))
print(li)
#DRAWBACK:isme order lost ho skta hai


# In[ ]:





# In[24]:


#.Replace list’s item with new value if found
li=[1,2,3,5]
i=li.index(3)
# li.insert(i,49)
li[i]=49
li


# In[34]:


#.Remove all occurrences of a specific item from a list.
l=[1,1,2,3,1,4, 1,1,5,1]
# for i in l:
#     if i==1:
#         l.remove(i)....WRONG
li=[i for i in l if i!=1]
li


# In[1]:


#.linear search
# input no. of elements in a list
# input list elements
# input no. to search
n=int(input())
li=[int(x) for x in input().split()]
g=int(input())
if g in li:
    print(li.index(g))
else:
    print(-1)


# In[39]:


#Take 10 integer inputs from user and store them in a list. 
#Again ask user to give a number. Now, tell user whether that number is present in list or not.
#also print index at which it is present
n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
m=int(input())
for i in li:
    if i==m:
        print("yes")
        print(li.index(i))
        break
else:
    print("no")


# In[41]:


# take 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.
li=[0,1,2,3,4,5,6,7,8,9,10,0,-890]
zero=0
odd=0
even=0
pos=0
neg=0
for i in li:
    if i==0:
        zero=zero+1
    if i>0:
        pos=pos+1
    if i<0:
        neg=neg+1
    if i%2==0:
        even=even+1
    if i%2!=0:
        odd=odd+1
print(zero,pos,neg,even,odd)


# In[6]:


#average of items of a list
l=[1,2,3,4,5]

sum=0
for i in l:
    sum = sum+i
avg=sum/len(l)
print(avg)


# In[51]:


#Write a program to check if elements of a list are same or not it read from front or back(PALINDROME).
li=[1,2,3,4,2,1]
for i in li:
    if li[i]!=li[len(li)-i-1]:
        print("no")
        break
else:
    print("yes")


# In[ ]:


#WAP that rotates the element of alist.


# In[7]:


#.Write a Python program to sum all the items in a list.
n=int(input())
li=[int(x) for x in input().split()]
sum=0
for i in range(len(li)):
    sum=sum+li[i]
print(sum)    
    


# In[9]:


#.Write a Python program to multiply all the items in a li
n=int(input())
li=[int(x) for x in input().split()]
mul=1
for i in range(len(li)):
    mul=mul*li[i]
print(mul)    


# In[11]:


#.print every item of list
n=int(input())
li=[int(x) for x in input().split()]
for i in range(len(li)):
    print(li[i],end='')


# In[16]:


#14.swap alternate
N=int(input())
arr=[int(x) for x in input().split()]

def swapAlternate(arr) :
    for i in range(0,len(arr),2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr    
def arg(li):
    li=swapAlternate(arr)
    for i in range(len(li)):
        print(li[i],end=" ")
arg(li)        


# In[ ]:





# In[ ]:





# In[52]:


#7.Extend nested list by adding the sublist


# In[53]:


#17.Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

# li=['aba','abc','efe']
# count=0
# for i in(len(li)):
#     if len(i)>=2 and i[0]==i[-1]:
#         count=count+1
# print(count)  


# In[ ]:





# In[31]:


#21.Write a Python program to find the list of words that are longer than n from a given list of words.
'''
first method to count list items ki length- LOOPS 


'''
n=int(input())
li=['hyu','jiu','mkopi']


new_li=[]
for ele in li:
    count=0
    for letter in ele:
        count=count+1
    if count>n:    
        new_li.append(ele)
        
str(new_li) 
    

'''
WHY IS THIS NOT WORKING IF I INPUT LIST FROM USER???????
'''
        
    


# In[34]:


'''
LIST COMPREHENSION+LEN()
'''
n=int(input())
li=['hyu','jiu','mkopi']


new_li=[ele for ele in li if len(ele)>n]
str(new_li)


# In[66]:


#22.Write a Python function that takes two lists and returns True if they have at least one common member
li1=['e','r','t','y']
n=int(input())
li=[]
for _ in range(n):
    li.append(input())
    
for i,j in li1,li:
    if i==j:
        print(li(j))
    


# In[4]:


#24.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
li=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
li=[x for (i,x) in enumerate(li) if i not in(0,4,5)]
li


# In[12]:


#26.Write a Python program to shuffle and print a specified list.
'''
shuffle() function from the random module is called with the color list as its argument. This function shuffles the elements of the list in-place, i.e.,
it modifies the list directly without returning a new list
'''
from random import shuffle
n=int(input())
li=[] 
for _ in range(n):
    li.append(input())
shuffle(li)
li


# In[ ]:


#27.Write a Python program to generate and 
#print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).


# In[ ]:


# 28.Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
li=[1,2,3,4,5,6]
for i in li:
    if i<=1:
        return False
    elif i==2:
        if i



# In[59]:


#Tina went to a fruit market to buy some fruits. She filled her fruit basket with different types of 
# fruits all together. But the vendor now asked Tina to separate each type of fruit and count them,
# so that he can make the bill. Each type of fruit has a particular number written on it. 
# Tina finds it difficult to do so. Help her to count the number of fruits of each type. 
 
# You have given a list A of size N, which stores the number written on each fruit in the basket.
# Your task it to count the number of fruits of each type.
# Input Format:
# The first line contains an integer N denoting the total number of fruits in the basket 
# The next N line contains N integers in sorted order representing the fruit number on each type of fruit.

# Output Fomrat:
# For each fruit type, print in a new line, print the number written on the fruit and 
# the count of that fruit in the basket separated by space.
'''
BASICALLY COUNT THE SAME NUMBER OF ITEMS IN THE LIST
'''
li=[1,1,1,2,1,3,3,3,2,2,2,2,4,4,1]
for i in li:
    count=0
    for j in li:
        if i==j:
            count=count+1
    print(i,count)


# # geeks for geeks questions

# In[1]:


'''1.Python program to interchange first and last elements in a list'''
li=[1,2,3,4,5]

li[0],li[-1]=li[-1],li[0]
print(li)


# In[2]:


#swapping
li=[1,2,3,4,5]
n=len(li)
temp=li[0]
li[0]=li[n-1]
li[n-1]=temp
li


# In[3]:


# Python3 program to swap using tuple.
# Swap function
def swapList(list):
     
    # Storing the first and last element 
    # as a pair in a tuple variable get
    get = list[-1], list[0]
     
    # unpacking those elements
    list[0], list[-1] = get
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# In[6]:


#using * operand
li=[1,2,3,4,5]
a,*b,c=li
print(a)
print(b)
print(c)
li=[c,*b,a]
li


# In[7]:


#using pop and insert
li=[1,2,3,4,5]
a=li.pop(0)
b=li.pop(-1)
li.append(a)
li.insert(0,b)
li


# In[9]:


#slicing
li=[1,2,3,4,5]
li=li[-1:]+li[1:-1]+li[:1]
li


# In[10]:


'''2.Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. '''
li=[1,2,3,4,5]
a=int(input())
b=int(input())
li[a],li[b]=li[b],li[a]
li


# In[13]:


#enumerate
li=[1,2,3,4,5]
a=int(input())
b=int(input())
for index,ele in enumerate(li):
    if index==a:
        ele1=ele
    if index==b:
        ele2=ele
li[a]=ele2
li[b]=ele1
li


# In[ ]:


'''3.'''


# In[14]:


'''4.ways to find length of a list'''
#len
li=[1,2,3,4,5]
print(len(li))


# In[16]:


#loop
li=[2,3,3,4,5]
count=0
for i in li:
    count+=1
print(count)


# In[17]:


#length_hint
from operator import length_hint


# In[18]:


li=[2,3,3,4,5]
print(length_hint(li))


# In[19]:


#sum
li=[2,3,3,4,5]
print(sum(1 for i in li))


# In[21]:


#recursion
li=[2,3,3,4,5]
def count(li):
    if not li:
        return 0
    return 1+count(li[1:])
count(li)


# In[24]:


#collections counter
from collections import Counter
li=[2,3,3,4,5]
print(sum(Counter(li).values()))


# In[ ]:


'''to check if element exists in a list'''
li=[1,2,3,4,5]


# In[30]:


#in
if 7 in li:
    print(7)
else:
    print(13)


# In[33]:


#loops
for i in li:
    if i==5:
        print('yes')
# else:
#     print('no')


# In[35]:


#any() method
a=any(item in li for item in li)#gives true if no duplicates
print(a)
li2=[1,1,2,3,4]
b=any(i in li2 for i in li2)
b


# In[39]:


'''to print duplicates from a list of integers'''
l=[1,2,3,3,4,5,6,7,6,9]

for i in set(l):
    count=0
    for j in l:
        if j==i:
            count+=1
    if count>1:
        print(i)
    


# In[40]:


# Python program to print duplicates from 
# a list of integers
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniqueList = []
duplicateList = []

for i in lis:
	if i not in uniqueList:
		uniqueList.append(i)
	elif i not in duplicateList:
		duplicateList.append(i)

print(duplicateList)


# In[ ]:




