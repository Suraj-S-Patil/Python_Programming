a=int(input("Enter a number: "))
b=2
if a=={0,1}:
    print("Given number is not a prime number.")
elif a==2:
    print("Given number is a prime number.")
else:
    for n in range(2,a):
        b+=1
        if a%n==0:
            break
        else:
            continue
    if b==a:
        print("Given number is a prime number.")
    else:
        print("Given number is not a prime number.")