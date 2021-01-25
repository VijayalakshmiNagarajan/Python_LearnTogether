#1+2^2/2 +3^3/3+......+n^n/n

n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    a=float(i**i)/i
    s=s+a
print("The sum of series is",s)
