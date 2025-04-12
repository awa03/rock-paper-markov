import random
import os

cache = {"r": 0, "p": 0, "s": 0}
entries = 0

counters = {
    "r": "p",  # paper beats rock
    "p": "s",  # scissors beats paper
    "s": "r"   # rock beats scissors
}

emojis = {
    "r": "🪨", 
    "p": "📜",  
    "s": "✂"  
}

def get_counter_move():
    if entries == 0:
        return random.choice(list(cache))

    items = list(cache)
    counts = list(cache.values())
    probabilities = [count / entries for count in counts]
    
    predicted_user_move = random.choices(items, weights=probabilities, k=1)[0]
    return counters[predicted_user_move]

def get_emoji_rep(move):
    global emojis
    return emojis[move]

def main():
    global cache, entries
    while True:
        user_choice = input("choose: r, p, s → ").lower()
        os.system("clear")

        if user_choice not in ["r", "p", "s"]:
            print("Invalid input, try again.")
            continue

        your_move = get_emoji_rep(user_choice)
        print(f"You chose: {your_move}")

        bot_move = get_counter_move()
        bot_move = get_emoji_rep(bot_move)
        print(f"Computer chose: {bot_move}")

        if user_choice == bot_move:
            print("It's a tie!")

        elif (
            (user_choice == "r" and bot_move == "s") or
            (user_choice == "p" and bot_move == "r") or
            (user_choice == "s" and bot_move == "p")
        ):
            print("You win!")

        else:
            print("You lose!")

        cache[user_choice] += 1
        entries += 1

        
main()

