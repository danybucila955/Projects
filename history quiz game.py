print("Hello, It's my first project!")
print("Welcome to the most epic game in the world! It's a history quiz!:))")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay,let's play!")
correct_answers = 0
incorrect_answers = 0
question1 = input("First world war began in which year? ")
if question1 == str(1914):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question2 = input("First World War ended in which year? ")
if question2 == str(1918):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question3 = input("Second World War started in which year? ")
if question3 == str(1939):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question4 = input("Second World War ended in which year? ")
if question4 == str(1945):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question5 = input("Who won World War I? ")
if question5.lower() == str("allies"):
    print("Correct!")
    correct_answers += 1
elif question5.lower() == str("the allies"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question6 = input("Who won World War II? ")
if question6.lower() == str("allies"):
    print("Correct!")
    correct_answers += 1
elif question6.lower() == str("the allies"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question7 = input("What is considered the largest empire in history? ")
if question7.lower() == str("mongol"):
    print("Correct!")
    correct_answers += 1
elif question7.lower() == str("mongol empire"):
    print("Correct!")
    correct_answers += 1
elif question7.lower() == str("mongols"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question8 = input("Who was the first ruler of the Mongol Empire? ")
if question8.lower() == str("genghis khan"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question9 = input("During World War II, Allied troops stormed the beaches of Normandy. Which country is Normandy in? ")
if question9.lower() == str("france"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

question10 = input("What was the capital city of the Inca Empire? ")
if question10.lower() == str("cusco"):
    print("Correct!")
    correct_answers += 1
else:
    print("Sorry,Wrong answer...")
    incorrect_answers += 1

print("Congrats!! You scored:")
print("Correct Answers: "+str(correct_answers))
print("Incorrect Answers: "+str(incorrect_answers))
print("Your percentage is: "+ str((correct_answers/10) * 100)+"%")