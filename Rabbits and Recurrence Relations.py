# Problem: Rabbits and Recurrence Relations from ROSALIND
# Author: Steven Sommer
# Date: 4/8/2022

# Problem
# Pre-conditions: Positive integers n≤40 and k≤5.
# Post Conditions: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

from math import sqrt


def k_recurrence_relation(n, k):
    if n < 40:
        if n == 0 or n == 1:
            return n
        else:
            return k_recurrence_relation(n - 1, k) + k * k_recurrence_relation(n - 2, k)
    else:
        return round((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n*sqrt(5))

def main():
    FILEPATHREAD = "rosalind_fib.txt"
    FILEPATHWRITE = "rosalind_fib-output.txt"
    
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read().split(" ")
        
        with open(FILEPATHWRITE, "w") as fw:
            fw.write(str(k_recurrence_relation(int(data[0]), int(data[1]))))
            return print("\nThe recurrence relational dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))
        
if __name__ == "__main__":
    main()