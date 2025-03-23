vocales="aeiouAEIOU"
p=input()
p=p.lower()
p1=""
p2=""
for i in p:
    if i not in vocales:
        p1+=i
for i in p1:
    p2+="."+i
print(p2)