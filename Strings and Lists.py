# Problem: Strings and Lists from ROSALIND
# Author: Steven Sommer
# Date: 2/18/2022

#Problem
#Pre-Condition:   A string s of length at most 200 letters and four integers a, b, c and d.
#Post Condition:  The slice of this string from indices a through b and c through d (with space in between), inclusively. 
#                 In other words, we should include elements s[b] and s[d] in our slice.

s = "FB4AYnXPXpKUv5n3oi9aHaiFVanCardiocranius0VjeOsIEMVK0W7DY7WVVpio80KGwYW1CAHTyq03cXl1UjyYnS1se78jhEqEV4PmCPzuXnLzATNxQCGF6zpwH44x8vZ5aOHyJqoivyTmeansLy2n0tekrIUFF8IBzt1zcg4hDs9QTg40Ps."
a = 27
b = 39
c = 142
d = 146

print (s[a:b+1] + " " + s[c:d+1])

