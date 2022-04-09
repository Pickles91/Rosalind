# Problem: Conditions from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

#Problem
#Pre-Condition: Two positive integers a and b (a<b<10000).
#Post Condition: The sum of all odd integers from a through b, inclusively.

a = 4825
b = 9741
result = 0

for i in range(a,b+1):
  if i % 2 == 1:
   result += i
   
print (result)
