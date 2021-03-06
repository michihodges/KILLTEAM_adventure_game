# MODULES
import time
import random

# PRINT PAUSE
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# INTRO
def intro():
    print_pause("Welcome to KILL TEAM Name Generator!")
    print_pause("Pick your faction:")
    print_pause("Adeptus Astartes, Imperial")

# RAVEN GUARD
def name_generator(batch):
    first_names = ['Aajz', 'Kyrin', 'Vykus', 'Tryris', 'Ordias', 'Navaer', 'Syras', 'Aevar', 'Reszan', 'Vorkyl']
    surnames = ['Kaed', 'Solari', 'Solaq', 'Qeld', 'Korvaedyn', 'Vannes', 'Torvaec', 'Klayde', 'Moradus', 'Ordaris']

    n = 0
    while n < batch:
        first_name = random.choice(first_names)
        surname = random.choice(surnames)
        print(first_name, surname)
        n += 1

intro()
name_generator(3)