s=input("enter string: ")
d={}
for ch in s:
   d[ch]=d.get(ch,0)+1
for i,j in d.items():
   print(i,"===>",j,"times")
