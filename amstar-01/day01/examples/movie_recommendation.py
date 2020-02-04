# Movie Recommendation Engine

import random

# Movie Database

m_pg = ['frozen', 'brave', 'lion king', 'jurassic park', 'aladin']
m_13 = ['avengers', 'dark knight', 'transformers', 'fast and furious', 'inception']
m_18 = ['revanent', 'john wick', 'joker', 'rambo: last blood', 'conjuring']

# Take the user data

name = input('Enter your name: ')
age  = int(input('Enter your age: '))

# Make two choices from the movie data base
# based on the user age

if ( age < 13 ):
    mv1 = random.choice(m_pg)
    mv2 = random.choice(m_pg)
elif ( 13 <= age < 18 ): #(age >= 13 and age < 18)
    mv1 = random.choice(m_13)
    mv2 = random.choice(m_pg + m_13)
else:
    mv1 = random.choice(m_18)
    mv2 = random.choice(m_pg + m_13 + m_18)

# Give the recommendation

print('Hello, ', name)
print('Recommended Movies: ')
print('1. ', mv1)
print('2. ', mv2)
