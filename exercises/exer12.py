# Python quiz program
questions = (("1. What is the programming language with faster compile time ?"),
             ("2. What is the most popular ai for assignments ?"),
             ("3. Who is smart comparatively ?"),
             ("4. What phone does Fattah own ?"))
options = (("a) Python b) Java c) C++ d) C#"),
           ("a) Gemini b) Claude sonnet c) Grok d) Chatgpt"),
           ("a) Fattah b) Joshua c) Raj d) Kartik"),
           ("a) Galaxy S25 b) Iphone 16 c) Nokia d) Nothing 3a"))
answers = ("c","a","a","d")

guesses = []
score = 0
question_num = 0
# n=0 

for question in questions:
    print("----------------------------")
    print(question)
    print(options[question_num])
    guess = input("Enter (a,b,c,d): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1
print("--------------------------------")
print("            RESULTS             ")
print("--------------------------------")
print("Answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()
print("Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()
print("----------------------------------")
print(f"Your total score is {score}/4 !")


# for question in questions:
#     print("------------------------------")
#     print(question)
#     print(options[n])
    
#     ans = input("\nChoose your option: ")
#     if ans.lower() == answers[n]:
#         print("Correct!")
#         score+=1
#     else:
#         print("Incorrect")
#     n+=1

# print(f"You got {score}/4 !")