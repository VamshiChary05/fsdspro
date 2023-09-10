#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TOPIC: String Based Assignment Problem


# In[12]:


#1. Write a program to reverse a string.
x = 'vamshi'


# In[19]:


def rev(s):
    return(s[::-1])


# In[20]:


rev('vamshi')


# In[21]:


#2. Check if a string is a palindrome.
def palindrome(x):
    if x == x[::-1]:
        print('yes its palindrome')
    else:
        print('no its not a palindrome')


# In[22]:


palindrome('malayalam')


# In[27]:


#3. Convert a string to uppercase.
def upp(x):
    print(x.upper())


# In[28]:


upp('vamshi')


# In[29]:


#4. Convert a string to lowercase.
def loww(x):
    print(x.lower())


# In[30]:


loww('MASTER')


# In[39]:


#5. Count the number of vowels in a string.
x = input('enter the string:')
y = 0
for i in x:
    if i in 'aeiouAEIOU':
        y = y+1
print(y)


# In[45]:


#6. Count the number of consonants in a string.
x = input('enter the string:')
y = 0
for i in x:
    if i not in 'aeiouAEIOU':
        y = y+1
print(y)


# In[51]:


#7. Remove all whitespaces from a string.
x = ' I am learning python & sql'
print(x.replace(' ',''))


# In[52]:


#8. Find the length of a string without using the `len()` function.
x = input('enter the string:')
y = 0
for i in x:
    y = y+1
print(y)


# In[54]:


#9. Check if a string contains a specific word.
x  = input('enter the string:')
for i in x:
    if 'python' in x:
        print('yes')
        break
    else:
        print('no')


# In[61]:


#10. Replace a word in a string with another word.
x  = input('enter the string:')
print(x.replace('python','Java'))


# In[79]:


#11. Count the occurrences of a word in a string.
x  = input('enter the string:')
y = 0
for i in x.split():
    if i =='python':
        y = y+1
print(y)


# In[87]:


#12. Find the first occurrence of a word in a string.
x = input('enter the string:')
char = input('enter the word:')
flag = 0
for i in range(len(x)):
    if(x[i] == char):
        flag = 1
        break
if(flag == 0):
    print('not found')
else:
    print('first occurrence of a word in a string position at',i+1)


# In[ ]:




