def evenlyDivides(self, n):
        sn=str(n)
        s=[]
        for i in sn:
            if i!='0':
                s.append(i)
        count=0
        for j in s:
            j=int(j)
            if n%j==0:
                count+=1
        return count
