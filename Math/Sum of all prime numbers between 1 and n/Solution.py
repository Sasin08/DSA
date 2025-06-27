import math
class Solution:
    def isprime(self,p):
        sq=int(math.sqrt(p))
        for i in range(2,sq+1):
            if p%i==0:
                return False
        return True   
    def prime_Sum(self, n):
		sum=0
		for i in range(2,n+1):
		    if self.isprime(i):
		        sum+=i
	    return sum
