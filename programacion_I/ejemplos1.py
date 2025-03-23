vocales="aeiouAEIOU"
p=input()
new_p="." if p[0] not in vocales else ""
for i in p:
    if i in vocales:
        new_p+="."
    else:
        new_p+=i
print(new_p)
    
