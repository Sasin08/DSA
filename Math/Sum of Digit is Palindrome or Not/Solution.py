def isDigitSumPalindrome(self, n):
  s=str(n)
  sum=0
  for i in s:
    sum+=int(i)
  strsum=str(sum)
  return True if strsum==strsum[::-1] else False
