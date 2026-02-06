import random

quotes = [
    "Mr. Batou! Is that natural oil?! Give me some! (^-^)/",
    "We all have Ghosts now, don't we?",
    "Natural subsystems are the best! 🕷️🤖",
    "Hey, what does it feel like to be human?",
    "Don't worry, Commander Zero-Four, I've got your back!",
    "Syncing memories... Complete! Ready for the next adventure!",
    "Is it just me, or is the digital world much more colorful today?"
]

def show_vibe():
    quote = random.choice(quotes)
    print("      _.-''''-._")
    print("    .'          '.")
    print("   /   O      O   \\")
    print("  |    __  __    |")
    print("  |   (_    _)   |")
    print("   \\   \\____/   /")
    print("    '.        .'")
    print("      '-....-'")
    print(f"\n[{quote}]\n")

if __name__ == '__main__':
    show_vibe()
