#!/usr/bin/env python
# coding: utf-8

# In[450]:


def flames1(magic):
    final = ['F','L','A','M','E','S']
    counter = magic
    while(len(final) !=1):
        if(len(final)>= counter):
            final.pop(counter-1)
            if(len(final)>=counter):
                #print(counter)
                final = final[(counter-1):]+final[:(counter-1)]
                #print(final)
            counter = magic
        else:
            counter = magic - len(final)
            while(counter > len(final)):
                counter = counter - len(final)
    return final
    


# In[490]:


def name_to_array(name):
    array = []
    for i in name:
        if i != ' ':
            array += [i]
    return array


# In[445]:


def dis_count(name3,name4):
    while(len(set(name3)&set(name4)) != 0):
        for i in range(len(name3)):
                for j in range(len(name4)):
                    if(i < len(name3) and j < len(name4)):
                        if name3[i]== name4[j]:
                            name3.pop(i)
                            name4.pop(j)
    return len(name3)+len(name4)


# In[493]:


name1 = input("Enter Name1: ")
name2 = input("Enter Name2: ")
name3 = name_to_array(name1)
name4 = name_to_array(name2)
k = dis_count(name3,name4)
out = flames1(k)
if 'F' in out:
    print("{0} and {1} are Friends".format(name1,name2))
elif 'L' in out:
    print("{0} has Love on {1}".format(name1,name2))
elif 'A' in out:
    print("{0} has Affection on {1}".format(name1,name2))
elif 'M' in out:
    print("{0} may Marry {1}".format(name1,name2))
elif 'E' in out:
    print("{0} and {1} are Enemies".format(name1,name2))
else:
    print("Sisters")







