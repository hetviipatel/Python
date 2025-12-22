n1 = int(input("enter first number="))
n2 = int(input("enter second number="))

#swapping
n1 = n1+n2
n2 = n1-n2
n1 = n1-n2
print("after swapping first number=",n1)
print("after swapping second number=",n2)

if(n1%2==0 and n2%2==0):
    print("both numbers are even")
elif(n1%2!=0 and n2%2!=0):
    print("both numbers are odd")
else:
    print("one number is even and other is odd")
  
if(n1>n2):
    print("first number is greater")
else:
    print("second number is greater")
