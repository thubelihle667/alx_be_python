import random 

secrete_number = random.randint(1,10)

guess = int(input("Guess a number from 1 to 10: "))

match guess:
    case guess : secrete_number:
        print("Congratulations, you gessed it!")
        
    case guess < secrete_number:
        print("Oops, your guess is a bit low. Give it another shot!")
        
    case guess > secrete_number:
        print("Oops, your guess is a bit high. try again!")
        
        if guess >< secrete_number:
            print("Do you want to play again?")
        
    case _:
        print("Invalid entry. Please try again.")