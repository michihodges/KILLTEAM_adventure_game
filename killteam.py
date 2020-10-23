# MODULES
import random

# RAVEN GUARD
def name_generator(batch):
    first_names = ['Aajz', 'Kyrin', 'Vykus', 'Tryris', 'Ordias', 'Navaer', 'Syras', 'Aevar', 'Reszan', 'Vorkyl']
    surnames = ['Kaed', 'Solari', 'Solaq', 'Qeld', 'Korvaedyn', 'Vannes', 'Torvaec', 'Klayde', 'Moradus', 'Ordaris']
    for character in range(batch):
        first_name = random.choice(first_names)
        surname = random.choice(surnames)
        print(first_name, surname)

name_generator(3)