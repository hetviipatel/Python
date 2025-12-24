# 1. Takes two integers as input
# 2. Swaps them without a temp variable
# 3. Checks if both are even or odd
# 4. Tells which one is greater after swapping

n1 = int(input("enter first number="))
n2 = int(input("enter second number="))

#swapping
n1 = n1+n2
n2 = n1-n2
n1 = n1-n2
print("after swapping first number=",n1)
print("after swapping second number=",n2)

#checking even or odd
if(n1%2==0 and n2%2==0):
    print("both numbers are even")
elif(n1%2!=0 and n2%2!=0):
    print("both numbers are odd")
else:
    print("one number is even and other is odd")

#checking greater number after swapping
if(n1>n2):
    print("first number is greater")
else:
    print("second number is greater")
