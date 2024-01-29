points = 0
questions_num = 8
import time
#introduction
print("Welcome to my soccer quiz")
name = input("What's your name: ")
playing = input(f"Do you want to play {name}: ")

if playing.lower() != "yes":
    quit()

#q1
answer = input("1. Which player has won the most Ballon d'Or? \na. Messi \nb. Cristiano Ronaldo \nc. Platini\nd. Ronaldo Nazario\n")
if answer == "a":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else: 
    time.sleep(1)
    print('Wrong. Hint: He is Argentine')
    time.sleep(1)

print("-----------------------")
#q2
answer = input("2. Which country has won the most World Cups? \na. Argentina\nb. Brazil\nc. Germany\nd. France\n")
if answer == "b":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: It's in South America.")
    time.sleep(1)

print("-----------------------")
#q3
answer = input("3. What club has won the most Champions League titles and how many did they won?\na. Milan: 7\nb. Milan: 11\nc. Real Madrid: 22\nd. Real Madrid: 14\n")
if answer == "d":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: The club has won more than 10.")
    time.sleep(1)

print("-----------------------")
#q4
answer = input("4. How many metres is the penalty spot from the goal?\na. 11 m\nb. 10 m\nc. 7 m\nd. 15 m\n")
if answer == "a":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: It's more than 10 metres.")
    time.sleep(1)

print("-----------------------")
#q5
answer = input("5. What soccer club's nickname is 'The Blues'?\na. Everton\nb. Man United\nc. Chelsea\nd. PSG\n")
if answer == "c":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: The club is in London.")
    time.sleep(1)

#q6
print("-----------------------")
answer = input("6. How many goals has Ronaldo scored?\na. 872\nb. 873\nc. 1027\nd. 869\n")
if answer == "b":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: It's less than 1000.")
    time.sleep(1)

print("-----------------------")
#q7
answer = input("7. Which player scored the fastest hat-trick in the Premier League?\na. Lionel Messi\nb. Rivaldo\nc. Cristiano Ronaldo\nd. Sadio Mane\n")
if answer == "d":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: He was a Southhampton player.")
    time.sleep(1)

print("-----------------------")
#q8
answer = input("8. Which club has won the most Premier League titles?\na. Man City\nb. Liverpool\nc. Man United\nd. Arsenal\n")
if answer == "c":
    time.sleep(1)
    print('Correct')
    points += 1
    time.sleep(1)
else:
    time.sleep(1)
    print("Wrong. Hint: It's a northern English club.")
    time.sleep(1)

#display score if points is equal or more than 6
if points > 6:
    print(f"Congratulations {name}. You have gotten {points} out of 8, and are a true soccer fan.")
    print(f"Percentage: {(points/questions_num) * 100}%")

#display score if points is between 3 and 6
elif points >= 3 and points <= 6:
    print(f"Good job {name}. You have gotten {points} out of 8. You are a casual soccer fan.")
    print(f"Percentage: {(points/questions_num) * 100}%")

#display score if points is less than 3
elif points < 3:
    print(f"You have gotten only {points} out of 8. Do you even watch soccer {name}?")
    print(f"Percentage: {(points/questions_num) * 100}%")

#play again
playing.input("Play again?")
if playing.lower() != "yes":
    quit()
