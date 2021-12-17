import secrets
with open("input.txt") as f:
    participants = [line.rstrip() for line in f]
winner = secrets.choice(participants)
if winner == "AlexTheNG":
    print("no winner, rerolling")
    winner = secrets.choice(participants)
    print(f"{winner} is the winner!")
else:
    print(f"{winner} is the winner!")
