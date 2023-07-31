import random
print("Mahd's High-Low Game")
range = int(input(f"The range of the game is 1 to: "))
hint = random.randint(1, range)
secret_number = random.randint(1, range)
print("Guess if the secret number is higher, lower, or the same as:", hint)
x = input("Put your answer here: ")
if x == "lower" and secret_number < hint:
    print("Congratulations, you won! The number was:", secret_number)

elif x == "higher" and secret_number > hint:
    print("Congratulations, you won! The number was:", secret_number)

elif x == "same" and secret_number == hint:
    print("Congratulations, the number was the same! ")

else:
    print("You were wrong, the correct number was:", secret_number)
