import re

str1='''

name: jack - age :23 - avg:85
name: joh - age :50 - avg:56
name: Roth - age :20 - avg:80
name: Helen - age :50 - avg:90
'''
# Terminal :re.Match object; span=(2, 31),match='name: jack - age :23 - avg:85'>
# res=re.search(r'name: jack - age :23 - avg:85', str1)
# print(res)


#Terminal:['name: jack - age :23 - avg:85']
# res=re.findall(r'name: jack - age :23 - avg:85', str1)
# print(res)


#

# str1='''

# name:jack-age:23-avg:85
# name:joh-age:50-avg:56
# name:Roth-age:20-avg:80
# name:Helen-age:50-avg:90
# '''
#Terminal:['name:', 'name:', 'name:', 'name:']
# res=re.findall(r'name:', str1)
# print(res)

#Terminal:['n', 'a', 'm', 'e', 'j', 'a', 'c', 'k', 'a', 'g',
# 'e', '2', '3', 'a', 'v', 'g', '8', 
# '5', 'n', 'a', 'm', 'e', 'j', 'o', 'h', 'a', 'g', 'e', 
# '5', '0', 'a', 'v', 'g', '5', '6', 'n', 'a', 'm', 'e', 
# 'R', 'o', 't', 'h', 'a', 'g', 'e', '2', '0', 'a', 'v',
# 'g', '8', '0', 'n', 'a', 'm', 'e', 'H', 'e', 'l', 'e',
# 'n', 'a', 'g', 'e', '5', '0', 'a', 'v', 'g', '9', '0']

# res=re.findall(r'\w', str1)
# print(res)






#['', '', 'name', '', '', 'jack', '', '', '', 'age',
# '', '', '23', '', '', '', 'avg', '', '85', '', 'name', 
# '', '', 'joh', '', '', '', 'age', '', '', '50', '', '', 
# '', 'avg', '', '56', '', 'name', '', '', 'Roth', '', '',
# '', 'age', '', '', '20', '', '', '', 'avg', '', '80', '',
# 'name', '', '', 'Helen', '', '', '', 'age', '', '', '50',
# '', '', '', 'avg', '', '90', '', '']

# res=re.findall(r'\w*', str1)
# print(res)




#['name', 'jack', 'age', '23', 'avg', '85', 'name', 'joh', 
# 'age', '50', 'avg', '56', 'name', 'Roth', 'age', '20', 
# 'avg', '80', 'name', 'Helen', 'age', '50', 'avg', '90']

# res=re.findall(r'\w+', str1)
# print(res)


# [('jack', '23'), ('joh', '50'), ('Roth', '20'), ('Helen', '50')]
# res=re.findall(r'name:(\w+)-age:(\d+)', str1)
# print(res)






#[('jack', '23', '85'), ('joh', '50', '56'), ('Roth', '20', '80'),
# ('Helen', '50', '90')]

# res=re.findall(r'name:(\w+)-age:(\d+)-avg:(\d+)', str1)
# print(res)




#('jack', '23', '85')
# ('joh', '50', '56')
# ('Roth', '20', '80')
# ('Helen', '50', '90')
# res=re.findall(r'name:(\w+)-age:(\d+)-avg:(\d+)', str1)
# for item in res:
#     print(item)




#CSV :Comma Separate  Value:(sub:substitue)
#jack ,23 ,85
# joh ,50 ,56
# Roth ,20 ,80
# Helen ,50 ,90

# res=re.sub(r'name:(\w+)-age:(\d+)-avg:(\d+)','\g<1> ,\g<2> ,\g<3>', str1)
# print(res)




#jack ,23 ,85
# joh ,50 ,56
# Roth ,20 ,80
# Helen ,50 ,90
#a file is created with the content below:
# res="name,age,avg"
# res+=re.sub(r'name:(\w+)-age:(\d+)-avg:(\d+)','\g<1> ,\g<2> ,\g<3>', str1)
# print(res)





#a file is created with the content below:
#name,age,avg

# jack ,23 ,85
# joh ,50 ,56
# Roth ,20 ,80
# Helen ,50 ,90

# res="name,age,avg" #csv  first line is the name of  columns
# res+=re.sub(r'name:(\w+)-age:(\d+)-avg:(\d+)','\g<1> ,\g<2> ,\g<3>', str1) #+= means add to res
# with open ('file1.csv','w') as file1:
#     file1.write(res)


























