import random


# yield statement is like the return statement
# yield returns a Generator


def vowels():
    #return ['a', 'e', 'i', 'o', 'u']

    yield "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"



def create_emoticon_generator(n):  # (#$^)
    i = n
    while i > 0:
        strings = "!@#$^*_-=+?/,.:;~"
        grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]
        grp = random.choice(grouped_strings)
        face_strings_list = [random.choice(strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon) # (@!!)
        yield emoticon
        i -= 1


if __name__ == "__main__":

    letters = vowels() # letters is going to be a generator
    letters2 = vowels()
    print(letters, type(letters))
    print('First for loop:')
    for i in letters:
        print(i)
    print('Second for loop:')
    for i in letters2:
        print(i)
    print('Third for loop:')
    for i in letters2:
            print(i)
    print('Fourth for loop:')
    for i in vowels():
            print(i)

    print('Using the next function')
    letters = vowels()
    print(next(letters))
    print(next(letters))
    print(next(letters))

    print('Doing something else')
    print(next(letters))
    print(next(letters))


    g = create_emoticon_generator(10)
    print([next(g) for i in range(10)])

    g = create_emoticon_generator(10)
    print([next(g) for i in range(8)])
    print(next(g), next(g))
