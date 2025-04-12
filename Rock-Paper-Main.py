from machine import Pin
import utime
import random

Lose = Pin(15,Pin.OUT)
Win = Pin(16,Pin.OUT)

cache = ["r", "p", "s"]
entries = 0

counters = {
    "r": "p",  # paper beats rock
    "p": "s",  # scissors beats paper
    "s": "r"   # rock beats scissors
}


def ResetLeds():
    Leds = [Win,Lose]
    for Led in Leds:
        Led.value(0)

def get_counter_move():
    return random.choice(cache)

def main():
    global cache, entries
    while True:
        user_choice = input("choose: r, p, s → ").lower()
        
        if user_choice not in ["r", "p", "s"]:
            print("Invalid input, try again.")
            continue

        bot_move = get_counter_move()
        print(f"Computer chose: {bot_move}")

        if user_choice == bot_move:
            print("It's a tie!")
             
        elif (
            (user_choice == "r" and bot_move == "s") or
            (user_choice == "p" and bot_move == "r") or
            (user_choice == "s" and bot_move == "p")
        ):
            print("You win!")
            Win.value(1)
            utime.sleep(1)
        
        else:
            print("You lose!")
            Lose.value(1)
            utime.sleep(1)
            
        cache.append(user_choice)
        entries += 1
        ResetLeds()
main()



