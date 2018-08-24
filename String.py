'''String

You are given a String  of size , consisting of lowercase English characters. Now, you need to select a single English lowercase alphabet, and delete all occurences of it from the given string 
Considering you do the mentioned exactly once over the given string, what is the minimum possible length of the resultant string ?

Input Format :

The first line contains a single integer N. The next line contains a String  of length  consisting of lowercase Englsh characters.

Output Format :

Print the required answer on a single line

Constraints :

Note that the Expected Output feature of Custom Invocation is not supported for this contest. '''

Code:


import collections
import operator

n = int(input())
a = input()

s = a[:n]

b = list(s)   #list created

freq = collections.Counter(b)

c = max(freq.items(), key = operator.itemgetter(1))[0]
d = max(freq.values())

print(len(b) - d)
        
