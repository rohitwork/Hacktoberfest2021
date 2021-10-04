#’Enter the numbers to check’
n=int(input())
m=int(input())
import math 
sum_n=1 + n  #sum of divisor of n 
sum_m=1 + m  #sum of divisor of m
i=2 
j=2 
#finding divisor
while(i<=math.sqrt(n)):
    if(n%i==0):
        if(n//i==i):
            sum_n+=i 
            
        else:
            sum_n+=i + n//i 
            
    i=i+1 
    
while(j<=math.sqrt(m)):
    if(m%j==0):
        if(m//j==j):
            sum_m+=j
            
        else:
            sum_m+=j + m//j 
            
    j=j+1 
if(sum_n/n==sum_m/m):
    print(‘Yes’ , n , ‘,’ , m ,‘ are friendly Pair’) 
else:
    print(‘No’, n , ‘,’ , m ,‘ are not friendly Pair’)
