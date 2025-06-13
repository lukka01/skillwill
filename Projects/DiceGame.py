
import random
while True:
    choice = input('Roll the dice (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f" you have rolled: {die1}, and {die2} ")
    elif choice == 'n':
        print("game over")
        break
    else:
        print('shens dedas sheveci')









