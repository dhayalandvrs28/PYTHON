n = int(input("Enter Range : "))
l = []
for i in range(n):
   ele = input(f"Enter Element {i+1} ; ")
   l.append(ele)
s = len(l)
l1 = []
while s>0:
   l1.append(l[s-1])
   s = s-1
print("Reversed List :", end = '')
print(l1)
