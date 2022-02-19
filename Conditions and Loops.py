# Problem: Conditions from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

a = 4825
b = 9741
result = 0
for i in range(a,b+1):
  if i % 2 == 1:
    result += i
print (result)
