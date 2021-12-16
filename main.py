import secrets
with open("input.txt") as f:
    participants = [line.rstrip() for line in f]
print(f"{secrets.choice(participants)} is the winner!")