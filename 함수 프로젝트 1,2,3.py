#!/usr/bin/env python
# coding: utf-8

# In[24]:


#프로젝트 1 전화번호를 가려주는 시스템
numbers = '010-12345-23456'
def change_num(numbers):

    return numbers.replace(numbers[-5:],'#####')

change_num(numbers)


# In[1]:


#프로젝트2  리스트 평탄화
a = [[1, 2], 3, [[4, 5, 6], 7], 8, 9]
def flatten(data):
    output =[]
    for i in data:
        if type(i) == list:
            output += flatten(i)
        else:
            output.append(i)
            
    return output
flatten(a)


# In[10]:


#프로젝트 3 10 이하의 숫자만 곱해주는 함수
def int_divider(x, y):
    if x % 1== 0 and y % 1 ==0:
        answer = x/y
    else: 
        print("정수만 계산 가능합니다")
        answer = None
    return answer
int_divider(10,3)


# In[9]:


#프로젝트 
def mul(*values):
    output = 1
    for num in values:
        if num <= 10:
            output *= num
        else: 
            pass
    return output
mul(3, 12, 10)


# In[23]:





# In[ ]:




