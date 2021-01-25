a=[]
for i in range(1,11):
    a.append(i)
print("The list from 1 to 10\n",a)
for j in a:
    if j%2==1:
        a.remove(j)
print("List after removing odd numbers\n",a)
