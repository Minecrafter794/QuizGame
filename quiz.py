import random
import time

#INITIAL VARIABLES
score1 = int(0)
score2 = int(0)
score3 = int(0)
score4 = int(0)
question = random.randint(1, 4)
rqa = random.randint(1, 5)
rqb = random.randint(1, 5)
rqc = random.randint(1, 5)
rqd = random.randint(1, 5)
qnum = 0

#INTRO AND CONFIG
print('Welcome to the Quiz Game.')
time.sleep(1)
sm = input("Singleplayer or Multiplayer? (s or m): ")
if sm == "m":
    teams = input("Are you doing Teams? (y or n): ")
    if teams == "y":
        players = int(input("How many Teams? up to 4 please: "))
        name_yn = input("Would You like to input team names? (y or n): ")
        if name_yn == "y":
            name1 = input("Team 1's name: ")
            name2 = input("Team 2's name: ")
            if players >= 3:
                name3 = input("Team 3's name: ")
                if players >= 4:
                    name4 = input("Team 4's name: ")
        else:
            name1 = "Team 1"
            name2 = "Team 2"
            name3 = "Team 3"
            name4 = "Team 4"
    else:
        players = int(input("How many Players? up to 4 please: "))
        name_yn = input("Would You like to input your names? (y or n): ")
        if name_yn == "y":
            name1 = input("Player 1's name: ")
            name2 = input("Player 2's name: ")
            if players >= 3:
                name3 = input("Player 3's name: ")
                if players >= 4:
                    name4 = input("Player 4's name: ")
        else:
            name1 = "Player 1"
            name2 = "Player 2"
            name3 = "Player 3"
            name4 = "Player 4"
else:
    name_yn = input("Would you like to input your name? (y or n): ")
    if name_yn == "y":
        name1 = input("Enter your name: ")
    else:
        name1 = "Player"
length = int(input("How Many Questions?: "))
print()
print("-----THE RULES-----")
time.sleep(2)
print()
print("You will be given a random Multiple Choice Question. Type in your answer and press enter to submit it. You will be given points based on your answer. If you get the Correct answer, you will be given 1 point. if you type in the wrong answer, you don't get a point. if you type in an invalid answer, you lose a point. DO NOT USE CAPITAL LETTERS. At the end of the game, final scores will be revealed. Also there is a known bug where questions may repeat themselves.")
print()
time.sleep(10)
start = input("Press Enter to start the game.")

#QUESTIONS

#-------------------------------------------------
def questiontemp():
    print()
    print("Question " + str(qnum) + ": ")
    time.sleep(4)
    print("A: ")
    print("B: ")
    print("C: ")
    print("D: ")
    time.sleep(3)
#-------------------------------------------------

def q1a():
    print()
    print("Question " + str(qnum) + ": Which of these people is NOT in the Minecraft Movie?")
    time.sleep(4)
    print("A: Steve Carell")
    print("B: Jennifer Coolidge")
    print("C: Jemaine Clement")
    print("D: Emma Myers")
    time.sleep(3)
    
def q2a():
    print()
    print("Question " + str(qnum) + ": Fill in the blank: When Wer'e done, _____________________. - Shadow")
    time.sleep(4)
    print("A: Ther'e won't be anything left")
    print("B: We will conquer the world")
    print("C: We will go to Wendy's")
    print("D: I WILL DESTROY ALL OF YOU")
    time.sleep(3)
    
def q3a():
    print()
    print("Question " + str(qnum) + ": Which One is Brainrot?")
    time.sleep(4)
    print("A: Skibidi Toilet")
    print("B: Among us")
    print("C: Kai Cenat")
    print("D: Gamblecore")
    time.sleep(3)
    
def q4a():
    print()
    print("Question " + str(qnum) + ": Which is NOT a real MCU movie?")
    time.sleep(4)
    print("A: Spider Man 3")
    print("B: Deadpool & Wolverine")
    print("C: Spider Man: No Way Home")
    print("D: The Incredible Hulk")
    time.sleep(3)
    
def q5a():
    print()
    print("Question " + str(qnum) + ": Which one was NOT a US President?")
    time.sleep(4)
    print("A: Alexander Hamilton")
    print("B: John Quincy Adams")
    print("C: Donald Trump")
    print("D: Martin Van Buren")
    time.sleep(3)
    
def q6a():
    print()
    print("Question " + str(qnum) + ": Fill in the blank: And now it's time for ___________________!")
    time.sleep(4)
    print("A: Fast Money")
    print("B: Wheel of Fortune")
    print("C: Squid Game")
    print("D: Protests")
    time.sleep(3)

def q1b():
    print()
    print("Question " + str(qnum) + ": Who won the 1st Super Bowl?")
    time.sleep(4)
    print("A: Miami Dolphins")
    print("B: Green Bay Packers")
    print("C: Kansas City Chiefs")
    print("D: Chicago Bears")
    time.sleep(3)
    
def q2b():
    print()
    print("Question " +str(qnum) + ": Is the One Piece real?")
    time.sleep(4)
    print("A: No")
    print("B: Yes")
    print("C: Not Revealed Yet")
    print("D: What the heck is a One Piece?")
    time.sleep(3)
    
def q3b():
    print()
    print("Question " +str(qnum) + ": Who is the current NFL Commissioner?")
    time.sleep(4)
    print("A: Pete Rozelle")
    print("B: Rodger Goodell")
    print("C: Paul Tagliabue")
    print("D: Tom Brady")
    time.sleep(3)
    
def q4b():
    print()
    print("Question " +str(qnum) + ": Which is the name of the salmon-killing company in Splatoon?")
    time.sleep(4)
    print("A: New Squidbeak Splatoon")
    print("B: Grizzco Industries")
    print("C: Alterna Space Program")
    print("D: Ammo Knights")
    time.sleep(3)
    
def q5b():
    print()
    print("Question " +str(qnum) + ": When did Minecraft's Nether Update Release?")
    time.sleep(4)
    print("A: March 13, 2020")
    print("B: June 23, 2020")
    print("C: November 30, 2020")
    print("D: October 31, 2020")
    time.sleep(3)
    
def q6b():
    print()
    print("Question " + str(qnum) + ": Which Youtuber has the most subscribers?")
    time.sleep(4)
    print("A: T Series")
    print("B: MrBeast")
    print("C: Dream")
    print("D: Pinkfong")
    time.sleep(3)
    
def q1c():
    print()
    print("Question " + str(qnum) + ": Who is the CURRENT voice of Mario?")
    time.sleep(4)
    print("A: Charles Martinet")
    print("B: Chris Pratt")
    print("C: Kevin Afghani")
    print("D: Captain Lou Ablano")
    time.sleep(3)
    
def q2c():
    print()
    print("Question " +str(qnum) + ": What software was Gamblecore created on?")
    time.sleep(4)
    print("A: Mario Paint")
    print("B: MS Paint")
    print("C: Flipnote Studio")
    print("D: Adobe Photoshop")
    time.sleep(3)
    
def q3c():
    print()
    print("Question " + str(qnum) + ": When did Minecraft release?")
    time.sleep(4)
    print("A: April 5, 2016")
    print("B: November 17, 2011")
    print("C: May 17, 2009")
    print("D: October 8, 2011")
    time.sleep(3)
    
def q4c():
    print()
    print("Question " + str(qnum) + ": Who is considered the Father of Genetics?")
    time.sleep(4)
    print("A: Ben Franklin")
    print("B: Isaac Newton")
    print("C: Gregor Mendel")
    print("D: Trevor Lawrence")
    time.sleep(3)
    
def q5c():
    print()
    print("Question " + str(qnum) + ": When did the Wii U and 3DS online servers shut down?")
    time.sleep(4)
    print("A: September 9, 2023")
    print("B: May 1, 2024")
    print("C: April 8, 2024")
    print("D: August 10, 2023")
    time.sleep(3)
    
def q6c():
    print()
    print("Question " + str(qnum) + ": What is the name of the guy from BrainBuffet?")
    time.sleep(4)
    print("A: Derrick Bartley")
    print("B: Bob Withers")
    print("C: Rob Schwartz")
    print("D: Monkey D. Luffy")
    time.sleep(3)

def q1d():
    print()
    print("Question " +str(qnum) + ": Where will Super Bowl 59 be played?")
    time.sleep(4)
    print("A: Levi's Stadium, San Francisco")
    print("B: SoFi Stadium, Los Angeles")
    print("C: Allegiant Stadium, Las Vegas")
    print("D: Ceasers Superdome, New Orleans")
    time.sleep(3)
    
def q2d():
    print()
    print("Question " +str(qnum) + ": What is the name of the EU act that Apple hates?")
    time.sleep(4)
    print("A: Protecting Europeans from Foreign Adversary Controlled Applications Act")
    print("B: No Apple Act")
    print("C: AI Act")
    print("D: Digital Markets Act")
    time.sleep(3)
    
def q3d():
    print()
    print("Question " +str(qnum) + ": How much HP does a Minecraft Bedrock Wither have?")
    time.sleep(4)
    print("A: 200")
    print("B: 300")
    print("C: 450")
    print("D: 600")
    time.sleep(3)
    
def q4d():
    print()
    print("Question " +str(qnum) + ": What is the tallest building in the world?")
    time.sleep(4)
    print("A: Shanghai Tower")
    print("B: Empire State Building")
    print("C: Merdeka 118")
    print("D: Burj Khalifa")
    time.sleep(3)
    
def q5d():
    print()
    print("Question " +str(qnum) + ": Who is the current CEO of Disney?")
    time.sleep(4)
    print("A: Walt Disney")
    print("B: Bob Chapek")
    print("C: Josh D'Amaro")
    print("D: Bob Iger")
    time.sleep(3)
            
def q6d():
    print()
    print("Question " + str(qnum) + ": Fill in the Blank: I... am _____________.")
    time.sleep(4)
    print("A: Bond. James Bond")
    print("B: The GOAT")
    print("C: Him")
    print("D: Steve")
    time.sleep(3)
    
#MULTIPLAYER GAME
if sm == "m":
    print("-------------------------------------------------------------------------------------")
    qnum = 1
    for i in range(length):
        question = random.randint(1, 4)
        if question == 1:
            rqa = random.randint(1, 6)
            rqb = random.randint(1, 6)
            rqc = random.randint(1, 6)
            rqd = random.randint(1, 6)
            if rqa == 1:
                q1a()
            elif rqa == 2:
                q2a()
            elif rqa == 3:
                q3a()
            elif rqa == 4:
                q4a()
            elif rqa == 5:
                q5a()
            else:
                q6a()
            print()
            answer1 = input(name1 + ", Enter your answer choice: ")
            answer2 = input(name2 + ", Enter your answer choice: ")
            if players >= 3:
                answer3 = input(name3 + ", Enter your answer choice: ")
                if players >= 4:
                    answer4 = input(name4 + ", Enter your answer choice: ")
            print()
            print(name1 + ",")
            time.sleep(2)
            if answer1 == "a":
                print("Your Answer is Correct!")
                score1 = score1 + 1
            elif answer1 == "b" or answer1 == "c" or answer1 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score1 = score1 -1
            time.sleep(1)
            print("Your score is currently " + str(score1) + " points.")
            time.sleep(3)
            print()
        
            print(name2 + ",")
            time.sleep(2)
            if answer2 == "a":
                print("Your Answer is Correct!")
                score2 = score2 + 1
            elif answer2 == "b" or answer2 == "c" or answer2 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score2 = score2 - 1
            time.sleep(1)
            if score2 == 1:
                print("Your score is currently " + str(score2) + " point.")
            else:
                print("Your score is currently " + str(score2) + " points.")
            time.sleep(3)
            print()
            
            if players >= 3:
                print(name3 + ",")
                time.sleep(2)
                if answer3 == "a":
                    print("Your Answer is Correct!")
                    score3 = score3 + 1
                elif answer3 == "b" or answer3 == "c" or answer3 == "d":
                    print("Your Answer is Incorrect.")
                else:
                    print("Your Answer is Invalid.")
                    score3 = score3 - 1
                time.sleep(1)
                if score3 == 1:
                    print("Your score is currently " + str(score3) + " point.")
                else:
                    print("Your score is currently " + str(score3) + " points.")
                time.sleep(3)
                print()
                
                if players >= 4:
                    print(name4 + ",")
                    time.sleep(2)
                    if answer4 == "a":
                        print("Your Answer is Correct!")
                        score4 = score4 + 1
                    elif answer4 == "b" or answer4 == "c" or answer4 == "d":
                        print("Your Answer is Incorrect.")
                    else:
                        print("Your Answer is Invalid.")
                        score4 = score4 - 1
                    time.sleep(1)
                    if score4 == 1:
                        print("Your score is currently " + str(score4) + " point.")
                    else:
                        print("Your score is currently " + str(score4) + " points.")
                    time.sleep(3)
                    print()
            print("The Correct answer was A.")
            time.sleep(3)
        elif question == 2:
            rqa = random.randint(1, 6)
            rqb = random.randint(1, 6)
            rqc = random.randint(1, 6)
            rqd = random.randint(1, 6)
            if rqb == 1:
                q1b()
            elif rqb == 2:
                q2b()
            elif rqb == 3:
                q3b()
            elif rqb == 4:
                q4b()
            elif rqb == 5:
                q5b()
            else:
                q6b()
            print()
            answer1 = input(name1 + ", Enter your answer choice: ")
            answer2 = input(name2 + ", Enter your answer choice: ")
            if players >= 3:
                answer3 = input(name3 + ", Enter your answer choice: ")
                if players >= 4:
                    answer4 = input(name4 + ", Enter your answer choice: ")
                    if players >= 5:
                        answer5 = input(name5 + ", Enter your answer choice: ")
                        if players >= 6:
                            answer6 = input(name6 + ", Enter your answer choice: ")
                            if players >= 7:
                                answer7 = input(name7 + ", Enter your answer choice: ")
                                if players >= 8:
                                    answer8 = input(name8 + ", Enter your answer choice: ")
            print()
            print(name1 + ",")
            time.sleep(2)
            if answer1 == "b":
                print("Your Answer is Correct!")
                score1 = score1 + 1
            elif answer1 == "c" or answer1 == "a" or answer1 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score1 = score1 - 1
            time.sleep(1)
            print("Your score is currently " + str(score1) + " points.")
            time.sleep(3)
            print()
        
            print(name2 + ",")
            time.sleep(2)
            if answer2 == "b":
                print("Your Answer is Correct!")
                score2 = score2 + 1
            elif answer2 == "c" or answer2 == "a" or answer2 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score2 = score2 - 1
            time.sleep(1)
            if score2 == 1:
                print("Your score is currently " + str(score2) + " point.")
            else:
                print("Your score is currently " + str(score2) + " points.")
            time.sleep(3)
            print()
            
            if players >= 3:
                print(name3 + ",")
                time.sleep(2)
                if answer3 == "b":
                    print("Your Answer is Correct!")
                    score3 = score3 + 1
                elif answer3 == "c" or answer3 == "a" or answer3 == "d":
                    print("Your Answer is Incorrect.")
                else:
                    print("Your Answer is Invalid.")
                    score3 = score3 - 1
                time.sleep(1)
                if score3 == 1:
                    print("Your score is currently " + str(score3) + " point.")
                else:
                    print("Your score is currently " + str(score3) + " points.")
                time.sleep(3)
                print()
                
                if players >= 4:
                    print(name4 + ",")
                    time.sleep(2)
                    if answer4 == "b":
                        print("Your Answer is Correct!")
                        score4 = score4 + 1
                    elif answer4 == "c" or answer4 == "a" or answer4 == "d":
                        print("Your Answer is Incorrect.")
                    else:
                        print("Your Answer is Invalid.")
                        score4 = score4 - 1
                    time.sleep(1)
                    if score4 == 1:
                        print("Your score is currently " + str(score4) + " point.")
                    else:
                        print("Your score is currently " + str(score4) + " points.")
                    time.sleep(3)
                    print()
            print("The Correct answer was B.")
            time.sleep(3)
        elif question == 3:
            rqa = random.randint(1, 6)
            rqb = random.randint(1, 6)
            rqc = random.randint(1, 6)
            rqd = random.randint(1, 6)
            if rqc == 1:
                q1c()
            elif rqc == 2:
                q2c()
            elif rqc == 3:
                q3c()
            elif rqc == 4:
                q4c()
            elif rqc == 5:
                q5c()
            else:
                q6c()
            print()
            answer1 = input(name1 + ", Enter your answer choice: ")
            answer2 = input(name2 + ", Enter your answer choice: ")
            if players >= 3:
                answer3 = input(name3 + ", Enter your answer choice: ")
                if players >= 4:
                    answer4 = input(name4 + ", Enter your answer choice: ")
                    if players >= 5:
                        answer5 = input(name5 + ", Enter your answer choice: ")
                        if players >= 6:
                            answer6 = input(name6 + ", Enter your answer choice: ")
                            if players >= 7:
                                answer7 = input(name7 + ", Enter your answer choice: ")
                                if players >= 8:
                                    answer8 = input(name8 + ", Enter your answer choice: ")
            print()
            print(name1 + ",")
            time.sleep(2)
            if answer1 == "c":
                print("Your Answer is Correct!")
                score1 = score1 + 1
            elif answer1 == "b" or answer1 == "a" or answer1 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score1 = score1 - 1
            time.sleep(1)
            print("Your score is currently " + str(score1) + " points.")
            time.sleep(3)
            print()
        
            print(name2 + ",")
            time.sleep(2)
            if answer2 == "c":
                print("Your Answer is Correct!")
                score2 = score2 + 1
            elif answer2 == "b" or answer2 == "a" or answer2 == "d":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score2 = score2 - 1
            time.sleep(1)
            if score2 == 1:
                print("Your score is currently " + str(score2) + " point.")
            else:
                print("Your score is currently " + str(score2) + " points.")
            time.sleep(3)
            print()
            
            if players >= 3:
                print(name3 + ",")
                time.sleep(2)
                if answer3 == "c":
                    print("Your Answer is Correct!")
                    score3 = score3 + 1
                elif answer3 == "b" or answer3 == "a" or answer3 == "d":
                    print("Your Answer is Incorrect.")
                else:
                    print("Your Answer is Invalid.")
                    score3 = score3 - 1
                time.sleep(1)
                if score3 == 1:
                    print("Your score is currently " + str(score3) + " point.")
                else:
                    print("Your score is currently " + str(score3) + " points.")
                time.sleep(3)
                print()
                
                if players >= 4:
                    print(name4 + ",")
                    time.sleep(2)
                    if answer4 == "c":
                        print("Your Answer is Correct!")
                        score4 = score4 + 1
                    elif answer4 == "b" or answer4 == "a" or answer4 == "d":
                        print("Your Answer is Incorrect.")
                    else:
                        print("Your Answer is Invalid.")
                        score4 = score4 - 1
                    time.sleep(1)
                    if score4 == 1:
                        print("Your score is currently " + str(score4) + " point.")
                    else:
                        print("Your score is currently " + str(score4) + " points.")
                    time.sleep(3)
                    print()
            print("The Correct answer was C.")
            time.sleep(3)
        else:
            rqa = random.randint(1, 6)
            rqb = random.randint(1, 6)
            rqc = random.randint(1, 6)
            rqd = random.randint(1, 6)
            if rqd == 1:
                q1d()
            elif rqd == 2:
                q2d()
            elif rqd == 3:
                q3d()
            elif rqd == 4:
                q4d()
            elif rqd == 5:
                q5d()
            else:
                q6d()
            print()
            answer1 = input(name1 + ", Enter your answer choice: ")
            answer2 = input(name2 + ", Enter your answer choice: ")
            if players >= 3:
                answer3 = input(name3 + ", Enter your answer choice: ")
                if players >= 4:
                    answer4 = input(name4 + ", Enter your answer choice: ")
                    if players >= 5:
                        answer5 = input(name5 + ", Enter your answer choice: ")
                        if players >= 6:
                            answer6 = input(name6 + ", Enter your answer choice: ")
                            if players >= 7:
                                answer7 = input(name7 + ", Enter your answer choice: ")
                                if players >= 8:
                                    answer8 = input(name8 + ", Enter your answer choice: ")
            print()
            print(name1 + ",")
            time.sleep(2)
            if answer1 == "d":
                print("Your Answer is Correct!")
                score1 = score1 + 1
            elif answer1 == "c" or answer1 == "a" or answer1 == "b":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score1 = score1 - 1
            time.sleep(1)
            print("Your score is currently " + str(score1) + " points.")
            time.sleep(3)
            print()
        
            print(name2 + ",")
            time.sleep(2)
            if answer2 == "d":
                print("Your Answer is Correct!")
                score2 = score2 + 1
            elif answer2 == "c" or answer2 == "a" or answer2 == "b":
                print("Your Answer is Incorrect.")
            else:
                print("Your Answer is Invalid.")
                score2 = score2 - 1
            time.sleep(1)
            if score2 == 1:
                print("Your score is currently " + str(score2) + " point.")
            else:
                print("Your score is currently " + str(score2) + " points.")
            time.sleep(3)
            print()
            
            if players >= 3:
                print(name3 + ",")
                time.sleep(2)
                if answer3 == "d":
                    print("Your Answer is Correct!")
                    score3 = score3 + 1
                elif answer3 == "c" or answer3 == "a" or answer3 == "b":
                    print("Your Answer is Incorrect.")
                else:
                    print("Your Answer is Invalid.")
                    score3 = score3 - 1
                time.sleep(1)
                if score3 == 1:
                    print("Your score is currently " + str(score3) + " point.")
                else:
                    print("Your score is currently " + str(score3) + " points.")
                time.sleep(3)
                print()
                
                if players >= 4:
                    print(name4 + ",")
                    time.sleep(2)
                    if answer4 == "d":
                        print("Your Answer is Correct!")
                        score4 = score4 + 1
                    elif answer4 == "c" or answer4 == "a" or answer4 == "b":
                        print("Your Answer is Incorrect.")
                    else:
                        print("Your Answer is Invalid.")
                        score4 = score4 - 1
                    time.sleep(1)
                    if score4 == 1:
                        print("Your score is currently " + str(score4) + " point.")
                    else:
                        print("Your score is currently " + str(score4) + " points.")
                    time.sleep(3)
                    print()
            print("The Correct answer was D.")
            time.sleep(3)
        qnum = qnum + 1
        print("-------------------------------------------------------------------------------------")
    print()
    print("That is all the questions. Final scores will be revealed shortly.")
    time.sleep(5)
    print()
    print(name1 + ", your final score is " + str(score1) + " points.")
    time.sleep(3)
    print(name2 + ", your final score is " + str(score2) + " points.")
    time.sleep(3)
    if players >= 3:
        print(name3 + ", your final score is " + str(score3) + " points.")
        time.sleep(3)
        if players >= 4:
            print(name4 + ", your final score is " + str(score4) + " points.")
            time.sleep(3)
    
#SINGLEPLAYER GAME
else:
    print("-------------------------------------------------------------------------------------")
    qnum = 1
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqa == 1:
        q1a()
    elif rqa == 2:
        q2a()
    elif rqa == 3:
        q3a()
    elif rqa == 4:
        q4a()
    else:
        q5a()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "a":
        print("Your Answer is Correct!")
        score1 = 1
    elif answer == "b" or answer == "c" or answer == "d":
        print("Your Answer is Incorrect.")
        score1 = 0
    else:
        print("Your Answer is Invalid.")
        score1 = -1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was A.")
    time.sleep(3)

    print("-------------------------------------------------------------------------------------")
    qnum = 2
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqc == 1:
        q1c()
    elif rqc == 2:
        q2c()
    elif rqc == 3:
        q3c()
    elif rqc == 4:
        q4c()
    else:
        q5c()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "c":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "b" or answer == "a" or answer == "d":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was C.")
    time.sleep(3)
    
    print("-------------------------------------------------------------------------------------")
    qnum = 3
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqb == 1:
        q1b()
    elif rqb == 2:
        q2b()
    elif rqb == 3:
        q3b()
    elif rqb == 4:
        q4b()
    else:
        q5b()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "b":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "c" or answer == "a" or answer == "d":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was B.")
    time.sleep(3)
    
    print("-------------------------------------------------------------------------------------")
    qnum = 4
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqd == 1:
        q1d()
    elif rqd == 2:
        q2d()
    elif rqd == 3:
        q3d()
    elif rqd == 4:
        q4d()
    else:
        q5d()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "d":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "c" or answer == "a" or answer == "b":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was D.")
    time.sleep(3)
    print("-------------------------------------------------------------------------------------")
    qnum = 5
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqb == 1:
        q1b()
    elif rqb == 2:
        q2b()
    elif rqb == 3:
        q3b()
    elif rqb == 4:
        q4b()
    else:
        q5b()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "b":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "c" or answer == "a" or answer == "d":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was B.")
    time.sleep(3)
    print("-------------------------------------------------------------------------------------")
    qnum = 6
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqa == 1:
        q1a()
    elif rqa == 2:
        q2a()
    elif rqa == 3:
        q3a()
    elif rqa == 4:
        q4a()
    else:
        q5a()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "a":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "b" or answer == "c" or answer == "d":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was A.")
    time.sleep(3)
    print("-------------------------------------------------------------------------------------")
    qnum = 7
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqc == 1:
        q1c()
    elif rqc == 2:
        q2c()
    elif rqc == 3:
        q3c()
    elif rqc == 4:
        q4c()
    else:
        q5c()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "c":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "b" or answer == "a" or answer == "d":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was C.")
    time.sleep(3)
    print("-------------------------------------------------------------------------------------")
    qnum = 8
    rqa = random.randint(1, 5)
    rqb = random.randint(1, 5)
    rqc = random.randint(1, 5)
    rqd = random.randint(1, 5)
    if rqd == 1:
        q1d()
    elif rqd == 2:
        q2d()
    elif rqd == 3:
        q3d()
    elif rqd == 4:
        q4d()
    else:
        q5d()
    print()
    answer = input("Enter your answer choice: ")
    print()
    print(name1 + ",")
    time.sleep(2)
    if answer == "d":
        print("Your Answer is Correct!")
        score1 = score1 + 1
    elif answer == "c" or answer == "a" or answer == "b":
        print("Your Answer is Incorrect.")
    else:
        print("Your Answer is Invalid.")
        score1 = score1 - 1
    time.sleep(1)
    if score1 == 1:
        print("Your score is currently " + str(score1) + " point.")
    else:
        print("Your score is currently " + str(score1) + " points.")
    time.sleep(3)
    print()
    print("The Correct answer was D.")
    time.sleep(3)