import random
TobeGuessed = random.randint(1,10)
#Vasta nyt muistaisin että tässä on true ja false noin toimivia (olen koodannut c# enne ja python on vähän epäymmärettävä minulle sen jälkeen, sori)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == TobeGuessed:
        print("You guessed right!")
        break
    elif guess > TobeGuessed:
        print("You guessed higher!")
    elif guess < TobeGuessed:
        print("You guessed lower!")