# ...existing code...
import random

print("Welcome to Fruit Clicker (Secetindere Edition)!")
a = input("Do you want to play? (y/n): ").strip().lower()
clicks = 0

# fruits and counts
fruit_counts = {
    "banana": 0,
    "apple": 0,
    "mango": 0,
    "orange": 0,
    "pineapple": 0,
    "dragonfruit": 0
}

points = 0
base_price = 10  # banana price
rank = 1  # starts at The Noob

# drop chances (weights) - adjust to tune rarity
drop_weights = {
    "banana": 70,
    "apple": 15,
    "mango": 7,
    "orange": 4,
    "pineapple": 2,
    "dragonfruit": 1
}

# pricing rules: some are 2x banana, some banana + 100, etc.
def current_prices():
    return {
        "banana": base_price,
        "apple": base_price * 2,          # 2x banana
        "mango": base_price + 100,        # banana + 100
        "orange": int(base_price * 2),    # 2x banana (example)
        "pineapple": base_price + 100,    # banana + 100 (example)
        "dragonfruit": int(base_price * 3) + 200  # rarer, much more
    }

def rank_name(r):
    if r <= 1:
        return "The Noob"
    if r >= 100:
        return "The G.O.A.T."
    # optional named milestones
    if r >= 90:
        return "Legend"
    if r >= 50:
        return "Pro"
    if r >= 10:
        return "Experienced"
    return f"Rank {r}"

# start only if user answered yes
if a == "y":
    while True:
        b = input("Press e to click, c to check status, s to sell, q to quit, u to upgrade, or h for help: ").strip().lower()
        if b == "e":
            clicks += 1
            print(f"You have clicked {clicks} times")
            if clicks >= 100:
                # grant one fruit per 100 clicks; rarer fruits possible according to drop_weights
                fruits_list = list(drop_weights.keys())
                weights = [drop_weights[f] for f in fruits_list]
                fruit = random.choices(fruits_list, weights=weights, k=1)[0]
                fruit_counts[fruit] += 1
                clicks -= 100
                print(f"You have gotten a {fruit}! You now have {fruit_counts[fruit]} {fruit}(s)")
        elif b == "c":
            prices = current_prices()
            counts_str = ", ".join(f"{k}: {v}" for k, v in fruit_counts.items())
            price_str = ", ".join(f"{k}: {p}" for k, p in prices.items())
            print(f"Fruits -> {counts_str}")
            print(f"Points: {points}")
            print(f"Rank: {rank} ({rank_name(rank)})")
            print(f"Prices -> {price_str}")
        elif b == "s":
            total_fruits = sum(fruit_counts.values())
            if total_fruits > 0:
                prices = current_prices()
                earned = sum(fruit_counts[f] * prices[f] for f in fruit_counts)
                points += earned
                breakdown = ", ".join(f"{f} x{fruit_counts[f]} @ {prices[f]} = {fruit_counts[f]*prices[f]}" for f in fruit_counts)
                print(f"Sold fruits: {breakdown}")
                print(f"Total earned: {earned} points!")
                for f in fruit_counts:
                    fruit_counts[f] = 0
            else:
                print("No fruits to sell.")
        elif b == "q":
            print("Thank you for playing. Goodbye!")
            break
        elif b == "u":
            COST_INCREASE_BASE = 50
            COST_RANK_UP = 200
            print("Upgrade Menu:")
            print(f"1) Increase banana base price (+5) - Cost: {COST_INCREASE_BASE} points")
            print(f"2) Rank up (+1) - Cost: {COST_RANK_UP} points")
            print("3) Show drop chances")
            choice = input(f"Choose upgrade (1/2/3) or press Enter to cancel (you have {points} points): ").strip()
            if choice == "":
                print("Upgrade cancelled.")
            else:
                try:
                    choice_num = int(choice)
                except ValueError:
                    print("Invalid choice. Enter 1, 2 or 3.")
                    choice_num = None

                if choice_num == 1:
                    cost = COST_INCREASE_BASE
                    print(f"Attempting banana price upgrade: you have {points}, cost is {cost}.")
                    if points >= cost:
                        points -= cost
                        base_price += 5
                        prices = current_prices()
                        print(f"Upgraded! -{cost} points. New prices -> Banana: {prices['banana']}, Apple: {prices['apple']}, Mango: {prices['mango']}")
                        print(f"Points remaining: {points}")
                    else:
                        print(f"Not enough points to upgrade banana price. You have {points}, need {cost}.")
                elif choice_num == 2:
                    cost = COST_RANK_UP
                    print(f"Attempting rank up: you have {points}, cost is {cost}.")
                    if points >= cost:
                        points -= cost
                        rank += 1
                        print(f"Rank increased to {rank} ({rank_name(rank)}). -{cost} points.")
                        print(f"Points remaining: {points}")
                    else:
                        print(f"Not enough points to rank up. You have {points}, need {cost}.")
                elif choice_num == 3:
                    total = sum(drop_weights.values())
                    for f, w in drop_weights.items():
                        pct = w / total * 100
                        print(f"{f}: {w} weight ({pct:.1f}% chance)")
                elif choice_num is not None:
                    print("Invalid upgrade selection.")
        elif b == "h":
            print("E: Click to gather clicks (100 clicks -> 1 fruit of a randomized type)")
            print("C: Check your current fruits, points, prices and rank")
            print("S: Sell your fruits for points (sells all types)")
            print("U: Upgrade menu (banana price, rank up, show drop chances)")
            print("Q: Quit the game")
            print("")
            print("Notes:")
            print("- Some fruits are worth 2× banana, others are banana + 100, etc.")
            print("- Drop chances are randomized according to configured weights.")
        else:
            print("Invalid input.")
else:
    print("Okay, maybe next time. Goodbye!")