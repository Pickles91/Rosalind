# Problem: Working with Files from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

i = 1
f = open('rosalind_ini5.txt')
for line in f.readlines():
    if i % 2 == 0 :
        print (line)
    i += 1