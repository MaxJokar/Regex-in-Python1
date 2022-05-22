import re

# 1.find a name   "max" :max
# str1=" jack george max philip rose max   dany   karl   donald   joe    andy "
# res=re.search(r'max', str1)
# print(res)
# print(res.group())


# 2.find evey max everything end with space :max philip rose maxdany   karl   donald   joe    andy
# str1=" jack george max philip rose maxdany   karl   donald   joe    andy "
# res=re.search(r'max.+\s', str1)
# print(res)
# print(res.group())



#3.find every max then stop the first space( lazy '?'):max philip
# str1=" jack george max philip rose maxdany   karl   donald   joe    andy "
# res=re.search(r'max.+?\s', str1)
# print(res)
# print(res.group())



#4 FINDALL method:a list is output:bring all max from str1:['max', 'max']
# str1=" jack george max philip rose maxdany   karl   donald   joe    andy "
# res=re.findall(r'max', str1)
# print(res)


# ['ma', 'ma']
# str1=" jack george max philip rose maxdany   karl   donald   joe    andy "
# res=re.findall(r'm.+?', str1)
# print(res)

#['max ', 'maxdany '] all start with  m   and have space
# str1=" jack george max philip rose maxdany   karl   donald   joe    andy "
# res=re.findall(r'm.+?\s', str1)
# print(res)



# brings all those things start with 78:['789878', '78987876544455']
# str1='''
# dany@gmail.com
# 123
# Daniel@yahoo.com
# 236
# George@hotmail.com
# 789878
# Mikee@hotmail.com
# 78987876544455



# '''
# numbers=re.findall(r'78\d+', str1)
# print(numbers)



#['785555', '789999']
str1='''
# dany@gmail.com
# 123
# Daniel@yahoo.com
# 236
# George@hotmail.com
# 78333
# Mikee@hotmail.com
# 785555
# Helen@hotmail.com
# 7899999999999


# '''
# numbers=re.findall(r'78\d{4}', str1)
# print(numbers)


#['78899']
# str1='''
#  dany@gmail.com
# 78899
#  Daniel@yahoo.com
# 7777
#  123Jack @hotmail.com
#  783
#  Mikee@hotmail.com
#  785
#  Helen@hotmail.com
#  7891
#  '''

# crtEmail=re.findall(r'7\d{4}', str1)
# print(crtEmail)



#['dany@gmail.com', 'Daniel@yahoo.com', 'Mikee@hotmail.com', 'Helen@hotmail.com']
# Get emails everything,+must have @ any character one dot for com
# str1='''
#  dany@gmail.com
# 78899
#  Daniel@yahoo.com
# 7777
#  123Jack @hotmail.com
#  783
#  Mikee@hotmail.com
#  785
#  Helen@hotmail.com
#  7891
#  '''

# crtEmail=re.findall(r'\w+\@.+\..{2,3}', str1)
# print(crtEmail)





#didnt bring:123Jack @hotmail.com783
# ['dany@gmail.com', 'Daniel@yahoo.com', 'Mikee@hotmail.com', 'Helen@hotmail.com']
# str1='''
#  dany@gmail.com
# 78899
#  Daniel@yahoo.com
# 7777
#  123Jack @hotmail.com
#  783
#  Mikee@hotmail.com
#  785
#  Helen@hotmail.com
#  7891
#  '''

# crtEmail=re.findall(r'[a-zA-Z]+\@.+\..{2,3}', str1)
# print(crtEmail)



#<callable_iterator object at 0x00000106B5097400>
# dany@gmail.com
# Daniel@yahoo.com
# Mikee@hotmail.com
# Helen@hotmail.com
# str1='''
#  dany@gmail.com
# 78899
#  Daniel@yahoo.com
# 7777
#  123Jack @hotmail.com
#  783
#  Mikee@hotmail.com
#  785
#  Helen@hotmail.com
#  7891
#  '''

# crtEmail=re.finditer(r'[a-zA-Z]+\@.+\..{2,3}', str1)
# print(crtEmail)
# for item in crtEmail:
#     print(item.group()) # must use group cuz it come as a  object ,


#Terminal:
# ######99
#  Daniel@yahoo.com
######7
#  123Jack @hotmail.com
 ######
#  Mikee@hotmail.com
 ######
#  Helen@hotmail.com
 ######1

#method(SUB) for substitution :search the patter in str1 then ,when you 
#find it  replace it with '####'
str1='''
 dany@gmail.com
78899
 Daniel@yahoo.com
7777
 123Jack @hotmail.com
 783
 Mikee@hotmail.com
 785
 Helen@hotmail.com
 7891
 '''

crtEmail=re.sub(r'7\d{2}','######' ,str1)
print(crtEmail)


























































































  




























