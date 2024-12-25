import random

def generate_compliment():
    compliments = [
        "You're as bright as a star!",
        "You have a great sense of humor!",
        "You're a coding wizard!",
        "You make the world a better place!",
        "You're a ray of sunshine!"
    ]
    return random.choice(compliments)

print(generate_compliment())
