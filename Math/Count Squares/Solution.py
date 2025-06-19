def countSquares(self, n):
        i=1
        count=0
        while i*i < n:
            count+=1
            i+=1
        return count
