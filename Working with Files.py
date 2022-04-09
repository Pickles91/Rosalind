# Problem: Working with Files from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

#Problem
#Pre-Condition: A file containing at most 1000 lines.
#Post Condition: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

i = 1
f = open('rosalind_ini5.txt')
for line in f.readlines():
    if i % 2 == 0 :
        print (line)
    i += 1
