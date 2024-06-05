# Edge search bot
# Makes you real money , fr

import keyboard, random
from time import sleep

c = {"end":"\033[0m", "red":"\033[1;31m", "green":"\033[1;32m", "blue":"\033[1;33m"}

press = lambda key: keyboard.press_and_release(key)
type = lambda k: keyboard.write(str(k))
randInt = lambda i, k: random.randint(i, k)
wordList = """Valorant PRX GenG sentinels 100T Leviatan aspas You are my sun kid I am not a pi rizz from ohio plus fanum tax in and ending the kerala india swift paket
            porche supra car bike modi edge microsoft paper cardboard go insert""".split()
# wordList = "sinx + cosx - tanx / cotx + secx / sec^2x + cos^2x + sin^2x - tan^2x - sec^2x =".split()

def search(remainingSearches: int) -> None:
    press('ctrl + l')
    sleep(0.2)
    for word in range(7):
        word = random.choice(wordList)
        for letter in word:
            type(letter)
            sleep(random.choice([0.08, 0.1, 0.13]))
        type(" ")
    type(remainingSearches)
    press('enter')

mode = input(f"\nEnter {c['red']}[Device]{c['end']} {c['blue']}[CurrentPoints]{c['end']}: ").split()
totalPoints = 60 if mode[0] != "pc" else 90
searchesToDo = int((totalPoints - int(mode[1]))/3)

print(f"\nInitializing bot...\nSearches To Do = {searchesToDo}")
# Startup delay
press('alt + tab')
sleep(1)

for i in range(0, searchesToDo):
    search(remainingSearches=searchesToDo-i)
    sleep(4.20)

print(f"\nSearches done.. {c['green']}adios{c['end']}")
# keyboard.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))