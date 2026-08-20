s=input("enter the string :")
v={'a','e','i','o','u'}
d={}
for ch in s:
   if ch in v:
      d[ch]=d.get(ch,0)+1
for i,j in sorted(d.items()):
   print(i,"-",j)
