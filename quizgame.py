'''
This program is to understand working with if else statements in python mainly.
quit() :- It works as an exit() cmd in python. Whenever it is encountered, we get exited from our program.
Here, We will be asking some questions and based on the correct answers we will get some marks.

'''

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower()[0] != "y":
    print("Bye!!!")
    quit()


print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
