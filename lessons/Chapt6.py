#String indexing
# [start : end : step]
credit_number = "1234-5678-9012-3456"

print(credit_number[2])

print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])

print(credit_number[-2])

print(credit_number[::2]) #Prints every second character
print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"Last 4 digits : {last_digits}")

#lets reverse credit number
credit_number = credit_number[::-1]
print(f"Reversed : {credit_number}")