import random
import time
import os
import datetime

Blue = "\033[1;34m"
White = "\033[0;37m"

def menu():
  os.system('clear')
  print(Blue+"COUNTDOWN\n"+White)
  print("Letters game or numbers game?")
  gametype = input()
  if (gametype == "letters") or (gametype == "l") or (gametype == "Letters") or (gametype == "L"):
    lettersgame()
  elif (gametype == "numbers") or (gametype == "n") or (gametype == "Numbers") or (gametype == "N"):
    numbersgame()
  else:
    print("Sorry, that is not an option")
    menu()

def lettersgame():
  consonants = ["B","B","C","C","C","D","D","D","D","D","D","F","F","G","G","G","H","H","J","K","L","L","L","L","L","M","M","M","M","N","N","N","N","N","N","N","N","P","P","P","P","Q","R","R","R","R","R","R","R","R","R","S","S","S","S","S","S","S","S","S","T","T","T","T","T","T","T","T","T","V","W","X","Y","Z"]
  vowels = ["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","I","I","I","I","I","I","I","I","I","I","I","I","I","O","O","O","O","O","O","O","O","O","O","O","O","O","U","U","U","U","U",]

  gameboard = []
  
  for i in range(0,9):
    print("Consonant (c) or vowel (v)?")
    letterchoice = input()
    if letterchoice == "c":
      x = random.randint(0,73)
      gameboard.append(consonants[x])
      print(gameboard)
    elif letterchoice == "v":
      x = random.randint(0,66)
      gameboard.append(vowels[x])
      print(gameboard)
    else:
      print("I'll just take that as a consonant...")
      x = random.randint(0,73)
      gameboard.append(consonants[x])
      print(gameboard)

  os.system('clear')

  print("Your letters:\n")
  for i in range(0,9):
    print(gameboard[i], end=" ")
  print("\n")

  letterscountdown()


def numbersgame():
  small = ["1","2","3","4","5","6","7","8","9","10"]
  large = ["25","50","75","100"]

  print("How many large?")
  no_of_large = int(input())
  if not (0 <= no_of_large <= 4):
    print("Sorry, that is not an option")
    numbersgame()

  gameboard = []
  for i in range(0,no_of_large):
    x = random.randint(0,(len(large)-1))
    gameboard.append(large[x])
    large.pop(x)
  for i in range(0,(6-no_of_large)):
    gameboard.append(small[random.randint(0,9)])

  os.system('clear')

  print("Your numbers:\n")
  for i in range(0,6):
    print(gameboard[i], end=" ")
  print("\n")
  target = random.randint(100,999)
  print("And the target is " + str(target))

  numberscountdown()

def lettersscores():
  os.system('clear')
  file = open("LettersScores","r")
  print(file.read() + "\n")
  file.close()

  print("Do you want to play again? (y/n)")
  again = input()
  if again == "y":
    menu()


def numbersscores():
  os.system('clear')
  file = open("NumbersScores","r")
  print(file.read() + "\n")
  file.close()
    
  print("Do you want to play again? (y/n)")
  again = input()
  if again == "y":
    menu()



def letterscountdown():
  print("Start now!")
  time.sleep(26)
  print("Ddu du")
  time.sleep(1)
  print("Ddu du")
  time.sleep(1)
  print("Du du du du")
  time.sleep(1)
  print("Booo")
  time.sleep(1)
  print()
  #input score
  print("Please enter your score (how many letters were in your longest word)")
  score = int(input())
  #get date
  date = datetime.datetime.now()
  #append score to text file
  file = open("LettersScores","a")
  file.write("\n" + str(date.strftime("%x")) + ": " + str(score))
  file.close()

  print("Do you want to play again or view your scores? (play/view)")
  again = input()
  if (again == "play") or (again == "p"):
    menu()
  elif (again == "view") or (again == "v"):
    lettersscores()

def numberscountdown():
  print("Start now!")
  time.sleep(26)
  print("Ddu du")
  time.sleep(1)
  print("Ddu du")
  time.sleep(1)
  print("Du du du du")
  time.sleep(1)
  print("Booo")
  time.sleep(1)
  print()
  #input score
  print("Please enter your score (10 points for getting the target exactly, 7 for being 1-5 away, 5 for being 6-10 away, and 0 otherwise)")
  score = int(input())
  #get date
  date = datetime.datetime.now()
  #append score to text file
  file = open("NumbersScores","a")
  file.write("\n" + str(date.strftime("%x")) + ": " + str(score))
  file.close()

  print("Do you want to play again or view your scores? (play/view)")
  again = input()
  if (again == "play") or (again == "p"):
    menu()
  elif (again == "view") or (again == "v"):
    numbersscores()

menu()