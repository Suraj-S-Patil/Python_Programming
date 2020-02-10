#Program to calculate Simple Interest

print("Enter the principal amount, rate and time period: ")
princ=int(input())
rate=float(input())
time=float(input())
si=(princ*rate*time)/100
print(f"The simple interest for given data is: {si}.")
