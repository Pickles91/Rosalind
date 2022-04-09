# Problem: Complementing a Strand of DNA from ROSALIND
# Author: Steven Sommer
# Date: 4/8/2022

#Problem
#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Pre-Condition: A DNA string s of length at most 1000 bp.
#Post Condition: The reverse complement sc of s.


nucleotide = input("Please Enter DNA String :  ")      # Store the user input as a String
basePair = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' , 'G' : 'C'}  # Dictionary to store the nucleotide base pairs
reverseComplement = " " # Initialise the result string as empty
    
for base in nucleotide:  # For each of the nucleotide base in the input
    reverseComplement += basePair[base]   # Add the paired base corresponding to the current base to the resultant string
    
print (reverseComplement[::-1]) # # Reverse the resultant string