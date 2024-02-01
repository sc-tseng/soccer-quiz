import time

questions_num = 10
points = 0
play_status = True
#introduction
print("Welcome to my soccer quiz")
name = input("What's your name: ")
playing = input(f"Do you want to play, {name} (yes/no): ")

if playing.lower() != "yes":
    play_status = False
    quit()
else:
    play_status = True

####Functions####
#q1
def q1(points):
    time.sleep(2)
    answer = input("1. Which player has won the most Ballon d'Or? \na. Messi \nb. Cristiano Ronaldo \nc. Platini\nd. Ronaldo Nazario\n")
    if answer.lower() == "a" or answer.lower() == "messi":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else: 
        time.sleep(1)
        print('Wrong. Hint: He is Argentine')
        time.sleep(1)
    return points

#q2
def q2(points):
    print("-----------------------")
    answer = input("2. Which country has won the most World Cups? \na. Argentina\nb. Brazil\nc. Germany\nd. France\n")
    if answer.lower() == "b" or answer.lower() == "brazil":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: It's in South America.")
        time.sleep(1)
    return points

#q3
def q3(points):
    print("-----------------------")
    answer = input("3. What club has won the most Champions League titles and how many did they won?\na. Milan: 7\nb. Milan: 11\nc. Real Madrid: 22\nd. Real Madrid: 14\n")
    if answer.lower() == "d" or answer.lower() == "real madrid 14":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: The club has won more than 10.")
        time.sleep(1)
    return points

#q4
def q4(points):
    print("-----------------------")
    answer = input("4. How many metres is the penalty spot from the goal?\na. 11 m\nb. 10 m\nc. 7 m\nd. 15 m\n")
    if answer.lower() == "a" or answer.lower() == "11":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: It's more than 10 metres.")
        time.sleep(1)
    return points

#q5
def q5(points):
    print("-----------------------")
    answer = input("5. What soccer club's nickname is 'The Blues'?\na. Everton\nb. Man United\nc. Chelsea\nd. PSG\n")
    if answer.lower() == "c" or answer.lower() == "chelsea":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: The club is in London.")
        time.sleep(1)
    return points

#q6
def q6(points):
    print("-----------------------")
    answer = input("6. How many goals has Ronaldo scored?\na. 872\nb. 873\nc. 1027\nd. 869\n")
    if answer.lower() == "b" or answer.lower() == "873":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: It's less than 1000.")
        time.sleep(1)
    return points

#q7
def q7(points):
    print("-----------------------")
    answer = input("7. Which player scored the fastest hat-trick in the Premier League?\na. Lionel Messi\nb. Rivaldo\nc. Cristiano Ronaldo\nd. Sadio Mane\n")
    if answer.lower() == "d" or answer.lower() == "mane" or answer.lower() == "sadio mane":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: He was a Southhampton player.")
        time.sleep(1)
    return points

#q8
def q8(points):
    print("-----------------------")
    answer = input("8. Which club has won the most Premier League titles?\na. Man City\nb. Liverpool\nc. Man United\nd. Arsenal\n")
    if answer.lower() == "c" or answer.lower() == "man united":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: It's a northern English club.")
        time.sleep(1)
    return points

#q9
def q9(points):
    print("-----------------------")
    answer = input("9. Which clubs are in the Argentina 'Superclásico' rivalry?\na. Boca Juniors and Independiente\nb. Boca Juniors and River Plate\nc. Racing Club and San Lorenzo de Almagro\nd. Racing Club and River Plate\n")
    if answer.lower() == "b" or answer.lower() == "boca juniors and river plate":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: The two clubs are located in the capital Buenos Aires.")
        time.sleep(1)
    return points

#q10
def q10(points):
    print("-----------------------")
    answer = input("10. Who is the oldest active footballer?\na. Kazuyoshi Miura\nb. Zlatan Ibrahimović\nc. Gianluigi Buffon\nd. Joaquín Sánchez\n")
    if answer.lower() == "a" or answer.lower() == "miura" or answer.lower() == "kazuyoshi miura":
        time.sleep(1)
        print('Correct')
        points += 1
        time.sleep(1)
    else:
        time.sleep(1)
        print("Wrong. Hint: He is a Japanese.")
        time.sleep(1)
    return points

play_status = True
###QUIZ###
while play_status == True:
    
    points = q1(points)
    points = q2(points)
    points = q3(points)
    points = q4(points)
    points = q5(points)
    points = q6(points)
    points = q7(points)
    points = q8(points)
    points = q9(points)
    points = q10(points)
    play_again = input("Play again? ")
    if play_again.lower() == "yes":
        play_status = True
        points = 0
    elif play_again.lower() == "no":
       play_status = False 

#display score if points is equal or more than 8
if points > 8:
    print(f"Congratulations {name}. You have gotten {points} out of {questions_num}, and are a true soccer fan.")
    print(f"Percentage: {(points/questions_num) * 100}%")

#display score if points is between 5 and 8
elif points >= 5 and points <= 8:
    print(f"Good job {name}. You have gotten {points} out of {questions_num}. You like soccer.")
    print(f"Percentage: {(points/questions_num) * 100}%")
#display score if points is between 2 and 5
elif points >= 2 and points < 5:
    print(f"You have gotten {points} out of {questions_num} {name}. You aren't a soccer fan, but you aren't dumb on soccer either.")
    print(f"Percentage: {(points/questions_num) * 100}%")
#display score if points is less than 2
elif points < 2:
    print(f"You have gotten only {points} out of {questions_num}. Do you even watch soccer {name}?")
    print(f"Percentage: {(points/questions_num) * 100}%")
time.sleep(1)

#play again
if play_status == False:
    quit()
