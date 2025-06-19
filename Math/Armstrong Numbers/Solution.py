def armstrongNumber (self, n): 
        num=0
        for i in str(n):
            i=int(i)
            num += i*i*i
        return True if(n==num) else False
