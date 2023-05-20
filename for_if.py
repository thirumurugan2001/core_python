a=int(input("Enter the  frist number : "))
b=int(input("Enter the  Second number : "))
c=0
for x in range (1,a):
    if b==x:
        print(x)
        print("Matched")
        c=c+1
        break
if c==0:
    print("Unmatched")