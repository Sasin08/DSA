def gcd(self,a:int,b:int):
        if b==0:
            return a
        return self.gcd(b,a%b)
def lcmAndGcd(self, a : int, b : int) -> list[int]:
        List=[0]*2
        List[1]=self.gcd(a,b)
        List[0]=int((a*b)/List[1])
        return List
