import random
import time

wb = [
    "apple", "grape", "chair", "brain", "flame", "stone", "water", "shine", "earth", "sword", "plant", "cloud",
    "clock", "flash", "storm", "beach", "robot", "light", "dream", "frame", "world", "angel", "guard", "blend",
    "voice", "focus", "pilot", "study", "shape", "drift", "lunar", "quest", "shiny", "power", "track", "grain",
    "flint", "watch", "piano", "blast", "spike", "flame", "beach", "earth", "sport", "punch", "bloom", "front",
    "clock", "spice", "plant", "storm", "study", "sport", "guard", "blend", "draft", "punch"
]

w = random.choice(wb)
print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.")
time.sleep(2)

for a in range(6):
    g = input(f"Attempt {a + 1}/6: ").lower()
    if len(g) < 5:
        print("Not enough letters")
        time.sleep(1.5)
        continue
    elif len(g) > 5:
        print("Only 5-letter words")
        time.sleep(1.5)
        continue
    elif not g.isalpha():
        print("Letters only")
        time.sleep(1.5)
        continue
    f = ""
    for i in range(5):
        if g[i] == w[i]:
            f += "🟩"
        elif g[i] in w:
            f += "🟨"
        else:
            f += "⬛️"
    print(f)
    time.sleep(2)
    if f == "🟩🟩🟩🟩🟩":
        print("\033[32m" + f"Congratulations! You guessed ‘{w}’ correctly." + "\033[0m")
        break
else:
    print("\033[31m" + f"Unfortunate! The word was ‘{w}’." + "\033[0m")
