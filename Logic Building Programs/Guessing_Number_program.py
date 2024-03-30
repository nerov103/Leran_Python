from random import randrange

random_number = randrange(1, 10)
agin = 5
user_input = "Guess a number between 1 and 10:"

while agin>0:
    user_gess=int(input(user_input))

    if user_input==random_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif user_gess<random_number:
        print(f"Your guess is too low")
    else:
        print("Your guess is too hight")
    agin -=1

if agin==0:
    print(f"Sorry! You're out of guess, The correct number was {random_number}")