print("Welcome to Laveena's Galaxy Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's start:)")
score = 0

answer = input("Which planet is closest to Sun? ")
if answer.lower() == "mercury":
    print("Bingo! That's Correct")
    score+=1
else:
    print("Oops! That's wrong:(")

answer = input("Solar system is located in which Galaxy? ")
if answer.lower() == "milkyway":
    print("Bingo! That's Correct")
    score+=1
else:
    print("Oops! That's wrong:(")

answer = input("Which planet is the largest in the solar system? ")
if answer.lower() == "jupiter":
    print("Bingo! That's Correct")
    score+=1
else:
    print("Oops! That's wrong:(")

answer = input("Which star is at the center of our Solar system? ")
if answer.lower() == "sun":
    print("Bingo! That's Correct")
    score+=1
else:
    print("Oops! That's wrong:(")

answer = input("What is the shape of Milkyway? ")
if answer.lower() == "spiral":
    print("Bingo! That's Correct")
    score+=1
else:
    print("Oops! That's wrong:(")

print("You got " + str(score) + " questions correct!")

quit()
