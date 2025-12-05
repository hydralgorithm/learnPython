# COMPOUND INTEREST CALCULATOR

P = float(input("Enter initial principle amount: "))
while P<=0:
    print("Principle cannot be less than or equal to 0!")
    P = float(input("Enter initial principle amount: "))

R = float(input("Enter rate of interest: "))
while R<=0:
    print("Rate of interest cannot be less than or equal to 0!")
    R = float(input("Enter rate of interest: "))

T = float(input("Enter time in years: "))
while T<=0:
    print("Time cannot be less than or equal to 0!")
    T = float(input("Enter time in years: "))


SI = (P*R*T)/100
CI = (P*pow(1+(R/100),T)) - P
print(f"Your Compound Interest = {CI: .2f}")
print(f"Your Simple Interest = {SI: .2f}")