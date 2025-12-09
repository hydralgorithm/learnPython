# Exception handling
# We have mainly 3 kinds of errors (zero-div-error, Type error, Value error)

# EXAMPLES OF ERRORS
# 1/0
# 1 + "1"
#  int("pizza")

# Handling of these errors gracefully have 3 steps (try, except, finally)

####### Method 1 of dealing #################
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by 0 IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception: #Checks at end if there any other errors
    print("Something went wrong !")
finally:
    print("Do some cleanup here")


####### Method 2 of dealing #################
# try:
#     number = int(input("Enter a number: "))
#     print(1/number)
# except Exception: #Deal with all exceptions together
#     print("Something went wrong!")