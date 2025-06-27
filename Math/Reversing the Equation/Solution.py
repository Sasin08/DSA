def reverseEqn(self, s):
  temp=""
  res=""
  for i in s[::-1]:
    if i.isdigit():
      temp=temp+i
    else:
      res=res+temp[::-1]
      res=res+i
      temp=""
  if temp:
    res=res+temp[::-1]
  return res
