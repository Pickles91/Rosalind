# Problem: Dictionaries  from ROSALIND
# Author: Steven Sommer
# Date: 4/8/2022


#Problem
#Given: A string s of length at most 10000 letters.
#Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.



message = input ('Enter the string : ') #taking user input
message = message.split(' ')    #spliting each message and creating a list
count={}   #declearing count dict for counting number of occurences

for character in message:     #looping through all elements in message
    count.setdefault(character, 0)   #setting the default for each character
    count[character] = count[character] + 1   #incrementing the coount of that character

or i in count.keys():    #looping through all key in count
    print(i,count[i])    #printing key and value